from rest_framework import serializers
from .models import Loan, Repayment

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = ['id', 'due_date', 'amount', 'status', 'paid_at']
        read_only_fields = ['id', 'paid_at']

class LoanSerializer(serializers.ModelSerializer):
    repayments = RepaymentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Loan
        fields = ['id', 'amount', 'term', 'status', 'created_at', 'approved_at', 'repayments']
        read_only_fields = ['id', 'status', 'created_at', 'approved_at', 'repayments']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan amount must be greater than 0")
        return value

    def validate_term(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan term must be greater than 0")
        return value
