from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class ActiveItemViewSet(viewsets.ModelViewSet):
    queryset = ActiveItem.objects.all()
    serializer_class = ActiveItemSerializer