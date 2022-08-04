from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
	path('', HomeView.as_view(), name ='home'),
	path('about/', AboutView.as_view(), name ='about'),
	path('book/', BookView, name ='book'),
	path('menu/', menuView, name ='menu'),
	path('create_product/', ProductCreateView.as_view(), name ='addPro'),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

