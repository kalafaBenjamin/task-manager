from projects.models import Project


class ProjectService:

    @staticmethod
    def create_project(owner, data):

        return Project.objects.create(
            owner=owner,
            **data
        )