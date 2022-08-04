from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import *
from django.core.paginator import Paginator
from .tests import telegram_bot_send_message
from django.urls import reverse_lazy


class HomeView(ListView):
	model =Menu
	template_name ='home.html'

class AboutView(TemplateView):
	template_name ='about.html'


def menuView(request):
	if request.user.is_authenticated:
		customer = request.user 
		print(request.user)
		order, created = Order.objects.get_or_create(customer=customer, complete =False)
		items  = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items =[]
		order ={'get_cart_total':0, 'get_cart_items':0}
		cartItems =order['get_cart_items'] #by which function it should calculate

	obj = Menu.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,2)
	try:
		page = p.page(page_n)
	except Exception:
		page = p.page(1)
	context = {
		'page' : page,
		'cartItems': cartItems
	}
	return render(request, 'menu.html',context)

def BookView(request):
	if request.method == 'POST':
		name =request.POST.get('name', None)
		phone =request.POST.get('phone', None)
		email =request.POST.get('email', None)
		message =request.POST.get('message', None)
		user =Comment.objects.create(
			userName =name,
			phone =phone,
			email =email,
			message =message
			)
		user.save()
		telegram_bot_send_message(f"Ismi: {user} \nTel raqam: {phone} \nE-mail: {email} \nMijoz fikri: {message}")

	return render( request =request, template_name ='book.html' )

class ProductCreateView(CreateView):
	model =Menu
	template_name ='addPro.html'
	fields ='__all__'
	success_url =reverse_lazy('home')













