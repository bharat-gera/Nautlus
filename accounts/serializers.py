from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.core.validators import MinLengthValidator

User=get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(validators=[MinLengthValidator(6)])

    def validate_email(self, value):
        value = value.lower()
        return value


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('name', 'email','password',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

    def validate_password(self, value):
        password = value
        for validator in [MinLengthValidator(6)]:
            validator(password)
        return value

    def validate_email(self, value):
        value= value.lower()
        email = value
        if email and User.objects.filter(email=email).count():
            raise serializers.ValidationError("Email already registered")
        return value

class PassChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField()
    new_password = serializers.CharField(validators=[MinLengthValidator(6)])

    def validate(self, attrs):
        old_password = attrs['old_password']
        new_password = attrs['new_password']
        if old_password == new_password:
            raise serializers.ValidationError('old and new password are same')
        return attrs
