from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	age = models.IntegerField(default=20)
	mobilenumber = models.CharField(max_length=10,null=True)
	uimg = models.ImageField(upload_to='Profilepics/',default='profile.jpg')

class Carlist(models.Model):
	y = [('HatchBack','Hatchback'),('Sedan','Sedan'),('SUV','Suv'),('Default','Select Car Type')]
	p = [('AV','Available'),('NA','Not Available'),('Sl','Select Availability')]
	cname = models.CharField(max_length=50)
	ctype = models.CharField(choices=y,default="Default",max_length=12) 
	priceperhour = models.DecimalField(decimal_places=2,max_digits=8)
	cimage = models.ImageField(upload_to='Carimages/',default='cardefault.jpg')
	cavailability = models.CharField(choices=p,default="Sl",max_length=20)

	def __str__(self):
		return self.cname

class Bookings(models.Model):
	d = [('Krishna','Krishna'),('Guntur','Guntur'),('Sl','Select District')]
	s = [('AP','Andhra Pradesh'),('Default','Select State')]
	cid = models.ForeignKey(Carlist,on_delete=models.CASCADE)
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	mbnumber = models.CharField(max_length=10,null=True)
	uid = models.ForeignKey(User,on_delete=models.CASCADE)
	pick_address = models.CharField(max_length=100)
	drop_address = models.CharField(max_length=100)
	dt = models.CharField(choices=d,default="Sl",max_length=20)
	st = models.CharField(choices=s,default="Default",max_length=25)
	pk_date = models.DateField()
	pk_time = models.TimeField()
	dp_date = models.DateField()
	dp_time = models.TimeField()

	def __str__(self):
		return self.email


