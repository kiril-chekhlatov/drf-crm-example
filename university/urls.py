from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("", include("students.urls")),
                path("", include("users.urls")),
            ]
        ),
    ),
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
]
urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
