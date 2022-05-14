from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CustomUser, Seller


class UserTests(APITestCase):
    def setUp(self) -> None:
        # Create a user
        self.user = CustomUser.objects.create_user(
            email="mark@mail.com", first_name="Mark", last_name="Bruen", password="123456"
        )

        # Create a seller
        self.seller = Seller.objects.create(seller_name="Mark Store", profile=self.user)

        # Create a token
        url = reverse_lazy("users:login")
        response = self.client.post(
            "/login/", {"email": "mark@mail.com", "password": "123456"}, format="json"
        )

        # Set the token in the header
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_user_detail(self):
        # set up
        user = CustomUser.objects.create_user(
            email="steve@mail.com", first_name="Steve", last_name="Jobs", password="123456"
        )
        user.save()

        # test
        url = reverse_lazy('users:user-detail', kwargs={'pk': 2})
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

    def test_seller_detail(self):
        url = reverse_lazy("users:seller-detail", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["seller_name"], "Mark Store")
        self.assertEqual(response.data["profile"]["email"], self.user.email)
