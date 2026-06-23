from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Task, Comment
from .serializers import (
    TaskSerializer,
    CommentSerializer
)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "project",
        "assigned_to",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "title",
    ]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer