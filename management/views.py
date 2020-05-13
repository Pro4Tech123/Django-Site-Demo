from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.

from .models import *
from .forms import *
from .decorators import *




@authorized
def registerPage(request):

	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			
			return redirect('login')


	context = {'form':form}
	return render(request, 'management/register.html', context)

@authorized
def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)

		if user is not None:
			login(request, user)
			return redirect('home')

		else:
			messages.info(request, 'Username or Password is incorrect')

	context = {}
	return render(request, 'management/login.html', context)


def logoutUser(request):

	logout(request)
	return redirect('login')



def home(request):

	return render(request, 'management/index.html')


def checkout(request, pk):

	product = Product.objects.get(id=pk)

	return render(request, 'management/checkout.html', {'product': product})

def paymentcomplete(request):
	body = json.loads(request.body)

	product = Product.objects.get(id=body['productId'])

	order = Order.objects.create(
		product=product
		)

	print('Body:', body)
	response = {
		'order_id': order.id,
		'product_id': product.id,
		'message': 'Payment Completed!'
		}

	return JsonResponse(response)


def menu(request):

	products = Product.objects.all()

	breakfast = Product.objects.filter(categories__name="Breakfast")

	lunch = Product.objects.filter(categories__name="Lunch")

	dinner = Product.objects.filter(categories__name="Dinner")


	context = {'products': products, 'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner}

	return render(request, 'management/menu.html', context)




def about(request):

	return render(request, 'management/about.html')

def contact(request):

	return render(request, 'management/contact.html')

def blog(request):

	return render(request, 'management/blog.html')

def reservation(request):

	return render(request, 'management/reservation.html')