from rest_framework import serializers
from .models import PaymentModel

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'
        read_only_fields = ['paid_at']
        
    def validate(self, attrs):
        member = attrs.get('member')
        month = attrs.get('month')

        # Duplicate payment check (IMPORTANT)
        if PaymentModel.objects.filter(member=member, month=month).exists():
            raise serializers.ValidationError(
                "This member has already paid for this month."
            )

        return attrs
