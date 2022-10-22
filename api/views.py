from django.shortcuts import render
from .serializers import MenuSerializer
from rest_framework.generics import ListCreateAPIView
from my_app.models import Menu

class MenuSerializerView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class MenuIDSerializerView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
