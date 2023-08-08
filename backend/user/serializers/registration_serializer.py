from rest_framework import serializers

from user.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number",
            "name",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "name": {"required": True, "allow_null": False},
        }

    def save(self):
        user = User(
            phone_number=self.validated_data["phone_number"],
            name=self.validated_data["name"],
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user
