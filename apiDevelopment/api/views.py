from django.shortcuts import render
from rest_framework import viewsets
from .serializers import tempSerializer
from .models import tempModel
# Create your views here.

class tempViewSet(viewsets.ModelViewSet):
    queryset = tempModel.objects.all()
    serializer_class = tempSerializer