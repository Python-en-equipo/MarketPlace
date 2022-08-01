# not working yet
# from django.urls import reverse_lazy
# from rest_framework import status
# from rest_framework.test import APITestCase

# from users.models import CustomUser, Seller

# import tempfile
# from PIL import Image

# class ImageTest(APITestCase):
#     def setUp(self) -> None:
#         # Create a user
#         self.user = CustomUser.objects.create_user(
#             email="mark@mail.com", first_name="Mark", last_name="Bruen", password="123456"
#         )

#         # Create a seller
#         self.seller = Seller.objects.create(seller_name="Mark Store", profile=self.user)

#         # Create a token
#         url = reverse_lazy("users:login")
#         response = self.client.post(
#             url, {"email": "mark@mail.com", "password": "123456"}, format="json"
#         )

#         # Set the token in the header
#         self.token = response.data["access"]
#         self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

#         # Create an image
#         self.tmp_file = tempfile.NamedTemporaryFile(suffix='.png')
#         image = Image.new('RGB', (100, 100))
#         image.save(self.tmp_file.name)
#         self.params = {

#             "title": "prueba",
#             "description": "prueba",
#             "product_images": self.tmp_file,
#             "price": 1900,
#             "category": "prueba",
#             "stock": 3
#         }
#         self.HTTP_HOST = "localhost:8000"

#     def test_valid_authenticated_post_returns_201(self):
#         url = reverse_lazy("ecommerce:product-list")
#         print(self.params)
#         print(self.HTTP_HOST)
#         response = self.client.post(
#            url, {
#             "title": "prueba",
#             "description": "prueba",
#             "product_images": self.tmp_file,
#             "price": 1900,
#             "category": "prueba",
#             "stock": 3
#         }, format='multipart', HTTP_HOST=self.HTTP_HOST)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
