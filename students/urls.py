from django.urls import path
from rest_framework import routers

from students.views import (MajorViewSet, RegionViewSet,
                            StudentsChoicesAPIView, StudentsStatistics,
                            StudentViewSet)

router = routers.SimpleRouter()
router.register(r'students', StudentViewSet)
router.register(r'majors', MajorViewSet)
router.register(r'regions', RegionViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('all-students-choices/', StudentsChoicesAPIView.as_view(),
         name="get_all_students_choices"),
    path('students-stats/', StudentsStatistics.as_view(), name='students_stats')
]
