from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CustomUser


class UserTests(APITestCase):
    def test_user_detail(self):
        # set up
        user = CustomUser.objects.create_user(
            email="steve@mail.com", first_name="Steve", last_name="Jobs", password="123456"
        )
        user.save()

        # test
        url = reverse_lazy('users:user-detail', kwargs={'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], user.email)
        self.assertEqual(response.data["first_name"], user.first_name)

    def test_user_create(self):
        url = reverse_lazy("users:user-create")
        data = {
            "email": "steve@mail.com",
            "first_name": "Steve",
            "last_name": "Jobs",
            "password": "123456",
            "password2": "123456",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], data["email"])
        self.assertEqual(response.data["first_name"], data["first_name"])
