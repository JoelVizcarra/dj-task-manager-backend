from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet,basename="users")
router.register(r'projects', views.ProjectViewSet,basename="projects")
router.register(r'tags', views.TagViewSet,basename="tags")
router.register(r'states', views.StateViewSet,basename="states")
router.register(r'tasks', views.TaskViewSet,basename="tasks")

urlpatterns = [
    path('', include(router.urls)),
]