from django.db import models

# Create your models here.
class MemberModel(models.Model):
    
    MEMBERSHIP_CHOICES = [
         ('normal', 'Normal'),
        ('golden', 'Golden'),
        ('premium', 'Premium'),
    ]
    
    name =models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100 )
    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES,default='normal')
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name