from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.factories import AdminUserFactory, SuperUserFactory
from users.serializers import AdminUserSerializer


class JwtAPITest(APITestCase):
    def setUp(self) -> None:
        self.super_admin = SuperUserFactory.create()
        self.payload_data = {
            'username': self.super_admin.username,
            'password': 'password'
        }

    def get_JWT_tokens(self):
        url = reverse('token_obtain_pair')
        data = self.payload_data
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
        self.super_admin = SuperUserFactory.create()
        self.admin = AdminUserFactory.stub()
        self.created_admin = AdminUserFactory.create()
        self.payload_data = {
            'username': self.admin.username,
            'password': self.admin.password,
            'appointment': self.admin.appointment,
            'role': self.admin.role,
            'middle_name': self.admin.middle_name,
            'photo': self.admin.photo
        }

    def test_creation(self):
        url = reverse('admin-users-list')
        response = APIClient()
        response.force_authenticate(self.super_admin)
        response_data = response.post(url, self.payload_data)
        self.assertEqual(response_data.status_code, status.HTTP_201_CREATED)

    def test_get_all_object(self):
        url = reverse('admin-users-list')
        response = APIClient()
        response.force_authenticate(self.super_admin)
        response_data = response.get(url)
        self.assertEqual(response_data.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data.json()), 2)

    def test_retrive(self):
        url = reverse('admin-users-detail', args={self.created_admin.id})
        response = APIClient()
        response.force_authenticate(self.super_admin)
        response_data = response.get(url)
        self.assertEqual(response_data.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.json()['id'], self.created_admin.id)

    def test_delete(self):
        url = reverse('admin-users-detail', args={self.created_admin.id})
        response = APIClient()
        response.force_authenticate(self.super_admin)
        response_data = response.delete(url)
        self.assertEqual(response_data.status_code, status.HTTP_204_NO_CONTENT)

