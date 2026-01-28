from rest_framework import serializers
from .models import PaymentModel

class PaymentSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.name', read_only=True)
    member_phone = serializers.CharField(source='member.phone', read_only=True)

    class Meta:
        model = PaymentModel
        fields = [
            'id',
            'member_name',
            'member_phone',
            'amount',
            'month',
            'status',
            'paid_at'
        ]
        read_only_fields = ['paid_at']
