from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class RegisterUserTests(APITestCase):
    def test_user_can_register(self):
        url = reverse("register")

        payload = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "StrongPassword123!",
            "password_confirm": "StrongPassword123!",
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(User.objects.filter(email="test@example.com").exists())