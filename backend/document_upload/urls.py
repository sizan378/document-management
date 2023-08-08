from django.urls import path 
from .views import UserDocumentUploadView, AdminDocumentDetailsView


urlpatterns = [
    # http://localhost:8011/api/v1/document-upload/file/upload/
    path(
        route="file/upload/",
        view=UserDocumentUploadView.as_view(),
        name="file_upload_view"
    ),

    # http://localhost:8011/api/v1/document-upload/document/details/admin/
    path(
        route="document/details/admin/",
        view=AdminDocumentDetailsView.as_view(),
        name="document_details_view_all_users"
    ),
]
