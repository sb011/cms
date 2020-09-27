
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class orderform(forms.ModelForm):
	class Meta:
		model=Order
		fields=("customer","product","status")

		widgets={
			"customer":forms.Select(attrs = {"class":"form-control"}),
			"product":forms.Select(attrs = {"class":"form-control"}),
			"status":forms.Select(attrs = {"class":"form-control"}),
		}

class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=("name","phone","email","profile_pic")

	# widgets={
	# 		"name":forms.CharField(attrs = {"class":"form-control"}),
	# 		"phone":forms.CharField(attrs = {"class":"form-control"}),
	# 		"email":forms.CharField(attrs = {"class":"form-control"}),
	# 	}

class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']