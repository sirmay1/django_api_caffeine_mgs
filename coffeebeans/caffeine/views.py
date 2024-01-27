from django.shortcuts import render
from rest_framework import viewsets
from .models import Coffee
from .serializers import CoffeeSerializer


class CoffeeView(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer



# Create your views here.






