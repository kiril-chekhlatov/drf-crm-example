from students.helpers import Genders, Contracts, Statues
from users.helpers import Roles
from users.serializers import AdminUserSerializer

from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from students.serializers import CommentSerializer, MajorSerializer, RegionSerializer, StudentSerializer
from django.contrib.auth.hashers import make_password
from django.core.files.base import ContentFile
from students.factories import StudentFactory

class StudentTests(APITestCase):
    def setUp(self) -> None:
        self.rector_data = {
            'username': 'admin2',
            'password': 'admin2',
            'appointment': 'Appointment',
            'role': Roles.RECTOR_ADMIN,
            'middle_name': 'Middle name',
            'photo': ContentFile(b"...", name="foo.jpeg")
        }
        self.student_data = StudentFactory.build()

        serializer = AdminUserSerializer(data=self.rector_data)
        if serializer.is_valid():
            self.admin = serializer.save()

    def test_creation(self):
        pass