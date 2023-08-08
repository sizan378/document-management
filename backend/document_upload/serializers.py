from rest_framework.serializers import ModelSerializer
from .models import DocumentUploadModel
from user.serializers.registration_serializer import UserDetailsSerializer


class DocumentUploadSerializer(ModelSerializer):
    class Meta:
        model = DocumentUploadModel
        fields = [
            "id",
            "created_at",
            "title",
            "description",
            "upload_date",
            "format",
            "user",
        ]


class DocumentDetailsSerializer(ModelSerializer):
    # user = UserDetailsSerializer()
    class Meta:
        model = DocumentUploadModel
        fields = [
            "id",
            "created_at",
            "title",
            "description",
            "upload_date",
            "format",
            "user",
        ]