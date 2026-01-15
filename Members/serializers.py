from rest_framework import serializers
from .models import MemberModel

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = '__all__'

    def validate(self, attrs):
        errors = {}

        # Custom message for phone
        if MemberModel.objects.filter(phone=attrs['phone']).exists():
            errors['phone'] = ["This phone number is already in use!"]

        # Custom message for email
        if MemberModel.objects.filter(email=attrs['email']).exists():
            errors['email'] = ["This email is already registered!"]

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
