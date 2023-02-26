from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.views import get_protected_file

schema_view = get_schema_view(
    openapi.Info(
        title="University Snippets API",
        default_version='v1',
        description="API Documentation for University Small CRM",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="clofolnet@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
    path('media/protected_files/<field_dir_path>/<filename>',
         get_protected_file, name='get_protected_file'),
]
