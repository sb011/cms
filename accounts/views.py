from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *


def signup(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('signin')
		

	context = {'form':form}
	return render(request, 'signup.html', context)

@unauthenticated_user
def signin(request):	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'signin.html', context)

# @login_required(login_url='signin')
def logoutUser(request):
	logout(request)
	return redirect('signin')


@login_required(login_url='signin')
def userPage(request):
	orders=request.user.customer.order_set.all()
	totalorder=orders.count()
	orderdeliverd=orders.filter(status="Delivered").count()
	orderepanging=orders.filter(status="Panding").count()
	context={"orders":orders,"totalorder":totalorder,"orderdeliverd":orderdeliverd,"orderepanging":orderepanging}
	return render(request,'user.html',context)


@login_required(login_url='signin')
def profile(request,id):
	customer=Customer.objects.get(id=id)
	form = CustomerForm(instance=customer)

	if request.method=="POST":
		form=CustomerForm(request.POST,request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context={"form":form}
	return render(request,'profile.html',context)

@login_required(login_url='signin')
@admin_only
def home(request):
	customers=Customer.objects.all()
	orders=Order.objects.all()
	totalorder=Order.objects.all().count()
	orderdeliverd=Order.objects.filter(status="Delivered").count()
	orderepanging=Order.objects.filter(status="Panding").count()
	homedist={"customers":customers,"orders":orders,"totalorder":totalorder,"orderdeliverd":orderdeliverd,"orderepanging":orderepanging}
	return render(request,'dashboard.html',homedist)



@login_required(login_url='signin')
def about(request):
	return render(request,'about.html')




@login_required(login_url='signin')
def products(request):
	qs=Product.objects.all()
	return render(request,'products.html',{"products":qs})



@login_required(login_url='signin')
def customer(request,id):
	
	customer=Customer.objects.get(id=id)
	orders=customer.order_set.all()
	myFilter=OrderFilter(request.GET,queryset=orders)
	orders = myFilter.qs
	totalorder=customer.order_set.all().count()
	context={"customer":customer,"orders":orders,"totalorder":totalorder,"myFilter":myFilter}
	return render(request,'customer.html',context)


@login_required(login_url='signin')
@admin_only
def createcustomer(request):
	form = CustomerForm()
	if request.method=="POST":
		form=CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={"form":form}
	return render(request,"createcustomer.html",context)



@login_required(login_url='signin')
@admin_only
def updatecustomer(request,id):
	customer=Customer.objects.get(id=id)
	form = CustomerForm(instance=customer)

	if request.method=="POST":
		form=CustomerForm(request.POST,instance=customer)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={"form":form}
	return render(request,"createcustomer.html",context)


@login_required(login_url='signin')
@admin_only
def deletecustomer(request,id):
	customer=Customer.objects.get(id=id)
	if request.method== "POST":
		customer.delete()
		return redirect('/')
	context={"customer":customer}
	return render(request,context)

@login_required(login_url='signin')
@admin_only
def createorder(request):
	form = orderform()

	if request.method == "POST":
		form = orderform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={"form":form}
	return render(request,'create_order.html',context)


@login_required(login_url='signin')
@admin_only
def updateorder(request,id):
	order = Order.objects.get(id=id)
	form = orderform(instance=order)

	if request.method == "POST":
		form=orderform(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={"order":order,"form":form}
	return render(request,'create_order.html',context)


@login_required(login_url='signin')
@admin_only
def deleteorder(request,id):
	order=Order.objects.get(id=id)
	if request.method== "POST":
		order.delete()
		return redirect('/')
	context={"order":order}
	return render(request,'delete_order.html',context)