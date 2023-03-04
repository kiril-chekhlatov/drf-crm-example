import factory

from users.models import AdminUser
from django.contrib.auth.hashers import make_password
from users.helpers import Roles
from django.core.files.base import ContentFile
from factory import fuzzy


class AdminUserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'username%d' % n)
    password = factory.Sequence(lambda n: 'password%d' % n)
    role = fuzzy.FuzzyInteger(low=1, high=len(Roles.ROLE_CHOICES))
    middle_name = factory.Sequence(lambda n: 'middle_name %d' % n)
    appointment = factory.Sequence(lambda n: 'appointment %d' % n)
    photo = factory.LazyAttribute(
        lambda _: ContentFile(b'...', name="lol.jpeg")
    )

    class Meta:
        model = AdminUser


class SuperUserFactory(factory.django.DjangoModelFactory):
    username = 'super_admin'
    password = make_password('password')
    is_staff = True
    is_superuser = True

    class Meta:
        model = AdminUser
