from projects.services.project_service import (
    ProjectService
)


def perform_create(self, serializer):

    ProjectService.create_project(
        owner=self.request.user,
        data=serializer.validated_data
    )