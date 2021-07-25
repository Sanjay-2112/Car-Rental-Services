from django import forms
from car.models import Carlist,User,Bookings
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class Carform(forms.ModelForm):
	class Meta:
		model = Carlist
		fields = ["cname","ctype","priceperhour","cimage","cavailability"]
		widgets = {
		"cname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Car Name",
			}),
		"ctype":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select type of Car",
			}),
		"priceperhour":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Price/hour",
			}),
		"cavailability":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UserRegistrationForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Retype the Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}

class Profileupdate(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","age","mobilenumber","uimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Age",
			}),
		"mobilenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update MobileNumber",
			}),
		}

class Changepassword(PasswordChangeForm):
	class Meta:
		model = User
		fields = "__all__"

class BookForm(forms.ModelForm):
	class Meta:
		model = Bookings
		fields = ["cid","fname","lname","email","mbnumber","pick_address","drop_address","dt","st","pk_time","pk_date","dp_time","dp_date"]
		widgets = {
		"cid":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"fname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter First Name",
			}),
		"lname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Email",
			}),
		"mbnumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter MobileNumber",
			}),
		"pick_address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Pick-up Address",
			"rows":3,
			}),
		"drop_address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Drop Address",
			"rows":3,
			}),
		"dt":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select District",
			}),
		"st":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select State",
			}),
		"pk_time":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Pick-up Time Date",
			"type":"Time",
			}),
		"pk_date":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Pick-up Date",
			"type":"Date"
			}),
		"dp_time":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Drop Time",
			"type":"Time",
			}),
		"dp_date":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Drop Date",
			"type":"Date"
			}),
		}