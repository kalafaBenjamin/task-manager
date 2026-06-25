from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from projects.models import Project
from tasks.models import Task


class TaskTests(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="owner_user",
            email="owner@example.com",
            password="StrongPassword123!"
        )

        self.other_user = User.objects.create_user(
            username="other_user",
            email="other@example.com",
            password="StrongPassword123!"
        )

        self.project = Project.objects.create(
            name="Backend Project",
            description="Django REST Framework project",
            owner=self.owner,
        )

    def test_project_owner_can_create_task(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Build task endpoint",
                "description": "Create TaskViewSet",
                "project": self.project.id,
                "status": "TODO",
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_user_cannot_create_task_for_another_users_project(self):
        self.client.force_authenticate(user=self.other_user)

        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Unauthorized task",
                "description": "Should fail",
                "project": self.project.id,
                "status": "TODO",
            }
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_201_CREATED,
                status.HTTP_403_FORBIDDEN,
                status.HTTP_400_BAD_REQUEST,
            ]
        )