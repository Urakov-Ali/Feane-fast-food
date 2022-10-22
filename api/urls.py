from django.urls import path
from .views import MenuSerializerView

urlpatterns = [
    path('all/', MenuSerializerView.as_view())
]
