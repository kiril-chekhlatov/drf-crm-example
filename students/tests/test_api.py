from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from students.factories import (
    CommentFactory,
    MajorFactory,
    RegionFactory,
    StudentFactory,
)
from students.models import Student
from users.factories import AdminUserFactory
from users.helpers import Roles


class StudentTests(APITestCase):
    def setUp(self) -> None:
        self.admin_rector = AdminUserFactory.create(role=Roles.ADMIN)
        self.student = StudentFactory.stub()
        self.student_updated_data = StudentFactory.stub()
        self.created_student = StudentFactory.create()
        self.major = MajorFactory.create()
        self.region = RegionFactory.create()
        self.comment = CommentFactory.create()
        self.studens = StudentFactory.create_batch(10)
        self.payload_data = {
            "contract_type": self.student.contract_type,
            "name": self.student.name,
            "surname": self.student.surname,
            "middle_name": self.student.middle_name,
            "birth_of_date": self.student.birth_of_date,
            "email": self.student.email,
            "address": self.student.address,
            "phone": self.student.phone,
            "passport_series": self.student.passport_series,
            "passport_number": self.student.passport_number,
            "PIN": self.student.PIN,
            "region": self.region.id,
            "authority": self.student.authority,
            "major": self.major.id,
            "gender": self.student.gender,
            "discount": self.student.discount,
            "percent": self.student.percent,
            "discount_from": self.student.discount_from,
            "discount_to": self.student.discount_to,
            "super_contract": self.student.super_contract,
            "super_contract_sum": self.student.super_contract_sum,
            "passport_document": self.student.passport_document,
            "IELTS_document": self.student.IELTS_document,
            "status": self.student.status,
            # 'comments':self.student.comments
        }
        self.data_for_put_update = {
            "contract_type": self.student_updated_data.contract_type,
            "name": self.student_updated_data.name,
            "surname": self.student_updated_data.surname,
            "middle_name": self.student_updated_data.middle_name,
            "birth_of_date": self.student_updated_data.birth_of_date,
            "email": self.student_updated_data.email,
            "address": self.student_updated_data.address,
            "phone": self.student_updated_data.phone,
            "passport_series": self.student_updated_data.passport_series,
            "passport_number": self.student_updated_data.passport_number,
            "PIN": self.student_updated_data.PIN,
            "region": self.region.id,
            "authority": self.student_updated_data.authority,
            "major": self.major.id,
            "gender": self.student_updated_data.gender,
            "discount": self.student_updated_data.discount,
            "percent": self.student_updated_data.percent,
            "discount_from": self.student_updated_data.discount_from,
            "discount_to": self.student_updated_data.discount_to,
            "super_contract": self.student_updated_data.super_contract,
            "super_contract_sum": self.student_updated_data.super_contract_sum,
            "passport_document": self.student_updated_data.passport_document,
            "IELTS_document": self.student_updated_data.IELTS_document,
            "status": self.student_updated_data.status,
            # 'comments':self.student.comments
        }
        self.data_for_patch_update = {
            "name": "patch_updated_name",
        }

    def test_creation(self):
        url = reverse("student-view-list")
        response = APIClient()
        response.force_authenticate(self.admin_rector)
        response_data = response.post(url, self.payload_data)
        self.assertEqual(response_data.status_code, status.HTTP_201_CREATED)

    def test_get_all_object(self):
        url = reverse("student-view-list")
        response = APIClient()
        response.force_authenticate(self.admin_rector)
        response_data = response.get(url)
        student_count = Student.objects.count()
        self.assertEqual(response_data.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data.json()), student_count)

    def test_retrive(self):
        url = reverse("student-view-detail", args={self.created_student.id})
        response = APIClient()
        response.force_authenticate(self.admin_rector)
        response_data = response.get(url)
        self.assertEqual(response_data.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.json()["id"], self.created_student.id)

    def test_update(self):
        url = reverse("student-view-detail", args={self.created_student.id})
        response = APIClient()
        response.force_authenticate(self.admin_rector)
        response_data = response.put(url, data=self.data_for_put_update)
        self.assertEqual(response_data.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.json()["id"], self.created_student.id)
        self.assertEqual(response_data.json()["name"], self.data_for_put_update["name"])

    def test_partical_update(self):
        url = reverse("student-view-detail", args={self.created_student.id})
        response = APIClient()
        response.force_authenticate(self.admin_rector)
        response_data = response.patch(url, data=self.data_for_patch_update)
        self.assertEqual(response_data.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.json()["id"], self.created_student.id)
        self.assertEqual(
            response_data.json()["name"], self.data_for_patch_update["name"]
        )

    def test_delete(self):
        url = reverse("student-view-detail", args={self.created_student.id})
        response = APIClient()
        response.force_authenticate(self.admin_rector)
        response_data = response.delete(url)
        self.assertEqual(response_data.status_code, status.HTTP_204_NO_CONTENT)
