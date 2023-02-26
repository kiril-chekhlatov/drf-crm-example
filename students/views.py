from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.helpers import create_choices_dict
from core.serializers import ChoiceFieldSerializer
from students.helpers import Contracts, Genders, Statues
from students.models import Major, Region, Student
from students.serializers import (MajorSerializer, RegionSerializer,
                                  StudentSerializer,
                                  StudentStatisticsSerializer)
from core.permissions import IsAdminUser, IsRectorUser


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.prefetch_related(
        'comments').select_related('major', 'region')
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, )


class MajorViewSet(ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = (IsAuthenticated,
                          IsRectorUser, )


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAuthenticated,
                          IsRectorUser, )


class StudentsChoicesAPIView(APIView):
    _choices_list = (Genders, Contracts, Statues)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ChoiceFieldSerializer,
        }
    )
    def get(self, request):
        try:
            data = create_choices_dict(self._choices_list)
            code = status.HTTP_200_OK
        except Exception as e:
            data = {'error': str(e)}
            code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data, status=code)


class StudentsStatistics(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser,
                          IsRectorUser, )

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: StudentStatisticsSerializer,
        }
    )
    def get(self, request):
        try:
            data = Student.get_statistics()
            code = status.HTTP_200_OK
        except Exception as e:
            data = {'error': str(e)}
            code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=data, status=code)
