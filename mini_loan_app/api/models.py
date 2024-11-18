from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from decimal import Decimal

class Loan(models.Model):
    LOAN_STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('PAID', 'Paid'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    term = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=10, choices=LOAN_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Loan #{self.id} - {self.user.username} - {self.amount}"

class Repayment(models.Model):
    REPAYMENT_STATUS = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
    )

    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='repayments')
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=REPAYMENT_STATUS, default='PENDING')
    paid_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f"Repayment #{self.id} for Loan #{self.loan.id}"