from rest_framework import permissions

from users.helpers import Roles


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return False


class IsAdminUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.role in (Roles.ADMIN, Roles.MARKETING_ADMIN, Roles.MARKETING_ADMIN):
            return True
        return False


class IsRectorUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == Roles.RECTOR_ADMIN:
            return True

        return False
