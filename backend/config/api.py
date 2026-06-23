from rest_framework.routers import DefaultRouter

from projects.views import ProjectViewSet
from tasks.views import TaskViewSet
from tasks.views import CommentViewSet

router = DefaultRouter()

router.register(
    "projects",
    ProjectViewSet
)

router.register(
    "tasks",
    TaskViewSet
)

router.register(
    "comments",
    CommentViewSet
)

urlpatterns = router.urls