from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=250)
    password = serializers.CharField(min_length=8)
    username = serializers.CharField(min_length=3)


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8)
    username = serializers.CharField(min_length=3)


class LogoutSerializer(serializers.Serializer):
    # token = Token.objects.get().key
    pass
