from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'username': {'min_length': 3}, 'password': {
            'write_only': True, 'min_length': 8}, 'email': {'required': True, 'allow_blank': False}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])

        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user

        raise serializers.ValidationError('Incorrect credentials.')
