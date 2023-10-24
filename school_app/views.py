from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


def index(request): 
    return HttpResponse('<h1>Django Include URLs</h1>')