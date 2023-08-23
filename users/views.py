from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.helpers import create_choices_dict
from core.permissions import IsSuperUser
from core.serializers import ChoiceFieldSerializer
from users.helpers import Roles
from users.models import AdminUser
from users.serializers import (
    AdminUserSerializer,
    TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer,
)


class AdminUserViewSet(ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (
        IsAuthenticated,
        IsSuperUser,
    )


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UsersChoicesAPIView(APIView):
    _choices_list = (Roles,)

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
            data = {"error": e}
            code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=data, status=code)
