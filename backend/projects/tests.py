from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from projects.models import Project


User = get_user_model()


class ProjectTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="owner_user",
            email="test@example.com",
            password="StrongPassword123!",
        )

        self.client.force_authenticate(user=self.user)

        self.project_data = {
            "name": "Website Redesign",
            "description": "Redesign the company website",
            "status": "active",
            "owner": self.user.id,
        }

    def test_authenticated_user_can_create_project(self):
        response = self.client.post(
            "/api/projects/",
            self.project_data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg=response.data,
        )

        project = Project.objects.get(id=response.data["id"])

        self.assertEqual(project.name, "Website Redesign")
        self.assertEqual(project.owner, self.user)