from django.urls import path
from rest_framework import routers

from students.views import (
    MajorViewSet,
    RegionViewSet,
    StudentsChoicesAPIView,
    StudentsStatistics,
    StudentViewSet,
)

router = routers.SimpleRouter()
router.register(r"students", StudentViewSet, basename="student-view")
router.register(r"majors", MajorViewSet, basename="major-view")
router.register(r"regions", RegionViewSet, basename="region-view")
urlpatterns = router.urls

urlpatterns += [
    path(
        "all-students-choices/",
        StudentsChoicesAPIView.as_view(),
        name="get_all_students_choices",
    ),
    path("students-stats/", StudentsStatistics.as_view(), name="students_stats"),
]
