from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):
    """insert user login info inside jwt access token payload"""

    @classmethod
    def get_token(cls, user_info):
        token = super().get_token(user_info)

        token["user_id"] = user_info.id
        token["phone_number"] = user_info.phone_number

        return token
