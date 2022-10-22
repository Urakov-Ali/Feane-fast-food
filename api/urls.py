from django.urls import path
from .views import MenuSerializerView, MenuIDSerializerView

urlpatterns = [
    path('all/', MenuSerializerView.as_view()),
    path('<int:pk>/', MenuIDSerializerView.as_view()),
]
