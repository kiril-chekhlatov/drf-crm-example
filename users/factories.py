import factory

from users.models import AdminUser


class AdminUserFactory(factory.Factory):
    class Meta:
        model = AdminUser

    username = 'admin'
    password = 'admin'
    role = 1
