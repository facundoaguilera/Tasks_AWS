from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TeamViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
