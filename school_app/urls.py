from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', views.index, name = 'home')
]

urlpatterns += router.urls