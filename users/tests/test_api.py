from users.helpers import Roles

from rest_framework import status

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from users.serializers import AdminUserSerializer
from django.contrib.auth.hashers import make_password
from django.core.files.base import ContentFile


class JwtAPITest(APITestCase):
    def setUp(self) -> None:
        self.super_admin_data = {
            'id': 1,
            'username': 'admin',
            'password': make_password('admin'),
            'is_staff': True,
            'is_superuser': True
        }
        self.data_for_request = {
            'username': 'admin',
            'password': 'admin'
        }
        serializer = AdminUserSerializer(data=self.super_admin_data)
        if serializer.is_valid():
            serializer.save()

    def get_JWT_tokens(self):
        url = reverse('token_obtain_pair')
        data = {'username': self.data_for_request['username'],
                'password': self.data_for_request['password']}
        response = self.client.post(url, data, format='json')
        return response

    def test_creation(self):
        response = self.get_JWT_tokens()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh(self):
        refresh_token = self.get_JWT_tokens().json()['refresh']
        url = reverse('token_refresh')
        data = {'refresh': refresh_token}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AdminUserAPITest(APITestCase):
    def setUp(self) -> None:
        self.super_admin_data = {
            'id': 1,
            'username': 'admin',
            'password': make_password('admin'),
            'is_staff': True,
            'is_superuser': True
        }
        self.payload_data = {
            'username': 'admin2',
            'password': 'admin2',
            'appointment': 'Appointment',
            'role': Roles.RECTOR_ADMIN,
            'middle_name': 'Middle name',
            'photo': ContentFile(b"...", name="foo.jpeg")
        }

        serializer = AdminUserSerializer(data=self.super_admin_data)
        if serializer.is_valid():
            self.super_admin = serializer.save()

    def test_creation(self):
        url = reverse('admin-users-list')
        response = APIClient()
        response.force_authenticate(self.super_admin)
        response_data = response.post(url, self.payload_data)
        self.assertEqual(response_data.status_code, status.HTTP_201_CREATED)
