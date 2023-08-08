from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from user.models import User
from user.serializers.registration_serializer import UserDetailsSerializer


class AdminUsersListView(ListAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = UserDetailsSerializer
    queryset = User.objects.all()