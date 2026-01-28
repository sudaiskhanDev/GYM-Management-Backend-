from django.db import models
from Members.models import MemberModel


class PaymentModel(models.Model):
    
    PAYMENT_STATUS = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    )
    
    member = models.ForeignKey(MemberModel, on_delete=models.CASCADE, related_name='payments')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='paid')
    
    paid_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    
    def __str__(self):
        return f"{self.member.name} - {self.month} - {self.amount}"
     