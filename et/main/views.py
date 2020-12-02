from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Offer
from .forms import Add_offer, User_Registration_Form, User_Login_Form



def index(request, category = None):
	
	if category == None:

		list_offers = Offer.objects.all()[::-1]

		return render(request, 'index.html', {'products': list_offers, 'category': 'Все категории'})

	elif category == 'mm':

		list_offers = Offer.objects.filter(category='Мясная продукция')

		return render(request, 'index.html', {'products': list_offers, 'category': 'Мясная продукция'})



def add_offer_form(request):

	form = Add_offer()

	return render(request, 'form.html', {'add_offer': form})


def add_offer(request):
	
	if request.method == 'POST':

		form = Add_offer(request.POST, request.FILES)

		if form.is_valid():

			offer = Offer()

			cd = form.cleaned_data

			offer.title = cd['title']
			offer.name = request.user
			offer.price = cd['price']
			offer.category = cd['category']
			offer.description = cd['description']
			offer.place = cd['place']
			offer.img = cd['img']


			offer.save()

			return HttpResponse('<h1>successful</h1>')

		else:
			return HttpResponse('Error in form')

	else:
		return HttpResponse('Error in method')


def Register_User_form(request):

	form = User_Registration_Form()

	return render(request, 'form.html', {'register': form})


def Register_User(request):
	
	if request.method == 'POST':

		form = User_Registration_Form(request.POST)

		if form.is_valid():

			user = User()

			cd = form.cleaned_data

			user.username = cd['username']
			user.email = cd['email']
			user.set_password(cd['password'])

			user.save()

			return HttpResponse('<h1>Successful</h1>')

		else:
			return HttpResponse('Error in form')

	else:
		return HttpResponse('Error in request')


def Login_User_form(request):

	form = User_Login_Form()

	return render(request, 'form.html', {'login': form})


def Login_User(request):

	if request.method == 'POST':

		form = User_Login_Form(data=request.POST)

		if form.is_valid():

			print('Form is valid')

			cd = form.cleaned_data

			user = authenticate(username = cd['username'], password = cd['password'])

			print('authenticate is success')

			if user is not None:

				if user.is_active:

					login(request, user)

					return HttpResponse('<h1>Successful</h1>')

				else:
					return HttpResponse('Disabled account')

			else:
				return HttpResponse('Account is not register')

		else:
			return HttpResponse('Invalid data.')

	else:
		return HttpResponse('Error in request')


def view_profile(request):

	try:
		user = User.objects.get(username = request.user)
		user_offers = Offer.objects.filter(name = request.user)
		
		return render(request, 'profile.html', {'user': user, 'offers': user_offers})

	except Exception as e:
		return HttpResponse('You should login')
		