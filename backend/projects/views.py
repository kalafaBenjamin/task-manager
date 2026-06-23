from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "name",
    ]

    def get_queryset(self):
        return Project.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)