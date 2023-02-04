from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError


User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=80)
    phone = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=45, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email','phone', 'password']
        
    
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("email exists déjà")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()
        Token.objects.create(user=user)
        return user