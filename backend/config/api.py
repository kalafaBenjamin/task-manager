from rest_framework.routers import DefaultRouter

from projects.views import ProjectViewSet
from tasks.views import TaskViewSet
from tasks.views import CommentViewSet

router = DefaultRouter()

router.register(
    "projects",
    ProjectViewSet,
    basename="project"
)

router.register(
    "tasks",
    TaskViewSet,
    basename="task"
)

router.register(
    "comments",
    CommentViewSet,
    basename="comment"
)

urlpatterns = router.urls