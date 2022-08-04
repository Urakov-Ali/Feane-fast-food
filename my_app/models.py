from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
	Name =models.CharField(max_length =100)
	Descreption =models.TextField()
	Price =models.CharField(max_length =10)
	Image =models.ImageField(upload_to='image/')

	def __str__(self):
		return self.Name 

class Comment(models.Model):
	userName =models.CharField(max_length =150)
	phone =models.CharField(max_length =20)
	email =models.CharField(max_length =50)
	message =models.TextField()
	date =models.DateTimeField(auto_now_add =True)

	def __str__(self):
		return f'{self.userName}'



#Model for adding the product to the card
class Order(models.Model):
	customer =models.ForeignKey(User, on_delete =models.SET_NULL, blank =True, null =True)
	date_ordered =models.DateTimeField(auto_now_add =True)		
	name =models.CharField(max_length =200, null =True)
	complete =models.BooleanField(default =False, null =True, blank =False)

#for calculating all the products in orderItem(products in card) by the function of get_total below 
	@property #Decorator
	def get_cart_total(self):
		orderitems =self.orderitem_set.all()
		total =sum([item.get_total for item in orderitems])
		return total

	@property #Decorator
	def get_cart_items(self):
		orderitems =self.orderitem_set.all()
		total =sum([item.quantity for item in orderitems])
		return total


	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product =models.ForeignKey(Menu, on_delete =models.SET_NULL, blank =True, null =True)
	order =models.ForeignKey(Order, on_delete =models.SET_NULL, blank =True, null =True)
	quantity =models.IntegerField(default =0, null =True, blank =True)
	date_ordered =models.DateTimeField(auto_now_add =True)	

	@property #Decorator
	def get_total(self):
		total =self.Menu.Price * self.quantity
		return total


	def __str__(self):
		return str(self.id)


# Create your models here.
