from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAdminUser

schema_view = get_schema_view(
    openapi.Info(
        title="Document Management API",
        default_version="v1",
        description="API Documentation",
        terms_of_service="#",
        contact=openapi.Contact(email="sizanmahmud08@gmail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=[IsAdminUser],
)

admin.site.site_header = "Document Management Admin"
admin.site.site_title = "Document Management System"
admin.site.index_title = "Document Management Admin Portal"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
]

# swagger url endpoints setup
urlpatterns += [
        path(
            "",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
        path("admin/", admin.site.urls),
        # django debug toolbar package
        path("__debug__/", include("debug_toolbar.urls")),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
