from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from .models import Loan, Repayment
from .serializers import LoanSerializer, RepaymentSerializer
from .permissions import IsOwnerOrAdmin

class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Loan.objects.all()
        return Loan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        loan = self.get_object()
        if loan.status != 'PENDING':
            return Response(
                {'error': 'Only pending loans can be approved'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Calculate weekly repayment amount
        weekly_amount = loan.amount / loan.term
        current_date = timezone.now().date()

        # Create repayment schedule
        repayments = []
        for week in range(loan.term):
            due_date = current_date + timedelta(weeks=week + 1)
            repayments.append(Repayment(
                loan=loan,
                due_date=due_date,
                amount=weekly_amount
            ))

        # Save repayments
        Repayment.objects.bulk_create(repayments)

        # Update loan status
        loan.status = 'APPROVED'
        loan.approved_at = timezone.now()
        loan.save()

        return Response(LoanSerializer(loan).data)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        loan = self.get_object()  # Get the loan object
        if loan.status != 'PENDING':
            return Response(
                {'error': 'Only pending loans can be rejected'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update loan status to 'REJECTED'
        loan.status = 'REJECTED'
        loan.rejected_at = timezone.now()  # Optional: Add rejection timestamp
        loan.save()

        return Response(LoanSerializer(loan).data)


class RepaymentViewSet(viewsets.ModelViewSet):
    serializer_class = RepaymentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Repayment.objects.all()
        return Repayment.objects.filter(loan__user=self.request.user)

    @action(detail=True, methods=['post'])
    def make_payment(self, request, pk=None):
        repayment = self.get_object()
        amount = Decimal(request.data.get('amount', 0))

        if repayment.status == 'PAID':
            return Response(
                {'error': 'This repayment has already been paid'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if amount < repayment.amount:
            return Response(
                {'error': 'Payment amount must be at least the scheduled amount '},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Mark repayment as paid
        repayment.status = 'PAID'
        repayment.paid_at = timezone.now()
        repayment.save()

        # Check if all repayments are paid
        loan = repayment.loan
        if not loan.repayments.filter(status='PENDING').exists():
            loan.status = 'PAID'
            loan.save()

        return Response(RepaymentSerializer(repayment).data)
