from django.shortcuts import render,redirect
from django.http import HttpResponse
from car.forms import Carform,UserRegistrationForm,Profileupdate,Changepassword,BookForm
from car.models import Carlist,User,Bookings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from carrental import settings

# Create your views here.

def home(request):
	return render(request,'app/home.html')

def services(request):
	w = Carlist.objects.all()
	return render(request,'app/services.html',{'i':w})

@login_required
def carlist(request):
	x = Carlist.objects.all()
	if request.method == "POST":
		t = Carform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Car added successfully")
			return redirect('/carlist')
	t = Carform()
	return render(request,'app/carlist.html',{'z':t,'a':x})

@login_required
def carupdate(request,m):
	k=Carlist.objects.get(id=m)
	if request.method == "POST":
		e = Carform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Car updated successfully".format(k.cname))
			return redirect('/carlist')
	f = Carform(instance=k)
	return render(request,'app/carupdate.html',{'y':f})

@login_required
def cardelete(request,n):
	v = Carlist.objects.get(id=n)
	if request.method == "POST":
		messages.info(request,"{} Car deleted successfully".format(v.cname))
		v.delete()
		return redirect('/carlist')
	return render(request,'app/cardelete.html',{'q':v})

@login_required
def carview(request,b):
	s = Carlist.objects.get(id=b)
	return render(request,'app/carview.html',{'c':s})

def registration(request):
	if request.method == "POST":
		r=UserRegistrationForm(request.POST)
		if r.is_valid():
			r.save()
			return redirect('/login')
	r = UserRegistrationForm()
	return render(request,'app/registration.html',{'n':r})

@login_required
def profile(request):
	return render(request,'app/profile.html')

def feedback(request):
	if request.method == "POST":
		sd = request.POST['snmail'].split(',')
		sb = request.POST['sub']
		mg = request.POST['msg']
		rt = settings.EMAIL_HOST_USER
		dt = send_mail(sb,mg,rt,sd)
		if dt == 1:
			return redirect('/home')
	return render(request,'app/feedback.html')

@login_required
def profileupdate(request):
	y = User.objects.get(id=request.user.id)
	if request.method == "POST":
		p = Profileupdate(request.POST,request.FILES,instance=y)
		if p.is_valid():
			p.save()
			return redirect('/profile')
	o = Profileupdate(instance=y)
	return render(request,'app/profileupdate.html',{'g':o})

@login_required
def changepassword(request):
	if request.method == "POST":
		l = Changepassword(user=request.user,data=request.POST)
		if l.is_valid():
			l.save()
			return redirect('/login')
	l = Changepassword(user=request)
	return render(request,'app/changepassword.html',{'h':l})

@login_required
def book(request,a):
	cf = Carlist.objects.filter(id=a)
	if request.method == "POST":
		ca = BookForm(request.POST)
		if ca.is_valid():
			qa = ca.save(commit=False)
			qa.uid_id = request.user.id
			qa.save()
			return redirect('/confirmation')
	ca = BookForm()
	return render(request,'app/book.html',{'u':ca,'aa':cf})

@login_required
def confirmation(request):
	return render(request,'app/confirmation.html')

@login_required
def mybooking(request):
	ss = Bookings.objects.filter(uid=request.user.id)
	return render(request,'app/mybooking.html',{'ck':ss}) 

@login_required
def bookupdate(request,z):
	aq = Bookings.objects.get(id=z)
	if request.method == "POST":
		pp = BookForm(request.POST,instance=aq)
		if pp.is_valid():
			pp.save()
			messages.success(request,"Booking has been Updated")
			return redirect('/mybooking')
	pp = BookForm(instance=aq)
	return render(request,'app/bookupdate.html',{'qw':pp})

@login_required
def bookcancel(request,o):
	tq = Bookings.objects.get(id=o)
	if request.method == "POST":
		messages.info(request,"Booking has been canceled successfully")
		tq.delete()
		return redirect('/mybooking')
	return render(request,'app/bookcancel.html',{'ww':tq})

@login_required
def userbookings(request):
	ff = Bookings.objects.all()
	return render(request,'app/viewuserbookings.html',{'oo':ff})

@login_required
def userbookcancel(request,j):
	tt = Bookings.objects.get(id=j)
	if request.method == "POST":
		messages.info(request,"Booking has been canceled successfully")
		tt.delete()
		return redirect('/Userbookings')
	return render(request,'app/userbookcancel.html',{'rr':tt})

