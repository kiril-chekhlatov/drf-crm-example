from django.urls import path
from rest_framework import routers

from users.views import (AdminUserViewSet, DecoratedTokenObtainPairView,
                         DecoratedTokenRefreshView, UsersChoicesAPIView)

urlpatterns = [
    path('all-users-choices/', UsersChoicesAPIView.as_view(),
         name="get_all_users_choices"),
    path('token/', DecoratedTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
]


router = routers.SimpleRouter()
router.register(r'admin-users', AdminUserViewSet, basename='admin-users')
urlpatterns += router.urls
