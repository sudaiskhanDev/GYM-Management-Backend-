from rest_framework import serializers
from .models import MemberModel

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = '__all__'
        

    def validate(self, attrs):
        errors = {}
        instance = self.instance  # update ke liye

        phone = attrs.get('phone')
        email = attrs.get('email')

        if phone:
            qs = MemberModel.objects.filter(phone=phone)
            if instance:
                qs = qs.exclude(id=instance.id)
            if qs.exists():
                errors['phone'] = ["This phone number is already in use!"]

        if email:
            qs = MemberModel.objects.filter(email=email)
            if instance:
                qs = qs.exclude(id=instance.id)
            if qs.exists():
                errors['email'] = ["This email is already registered!"]

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

