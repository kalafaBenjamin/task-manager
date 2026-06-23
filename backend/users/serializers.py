from django.contrib.auth import authenticate
from users.models import User
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        user = authenticate(
            username=attrs["email"],
            password=attrs["password"]
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid credentials"
            )

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = [
            "email",
            "username",
            "password",
        ]

    def create(self, validated_data):

        password = validated_data.pop(
            "password"
        )

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user