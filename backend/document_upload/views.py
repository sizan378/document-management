from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import DocumentUploadModel
from .serializers import DocumentUploadSerializer, DocumentDetailsSerializer
from utils.utils import tokenValidation



class UserDocumentUploadView(CreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = DocumentUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = DocumentUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class AdminDocumentDetailsView(ListAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = DocumentDetailsSerializer
    queryset = DocumentUploadModel.objects.all()
    
