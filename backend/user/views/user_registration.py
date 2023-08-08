from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.registration_serializer import UserRegistrationSerializer


class UserRegistrationView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        user_registration_serializer = UserRegistrationSerializer(data=request.data)

        user_registration_serializer.is_valid(raise_exception=True)
        user_registration_serializer.save()
        return Response(
            {"detail": "Congrats, Successfully registered a new user"},
            status=status.HTTP_200_OK,
        )
