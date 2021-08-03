from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
    	return self.name

class Product(models.Model):
    pname = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    pimage = models.ImageField(upload_to='Productimages/',default='sofa.jpg')

class User(AbstractUser):
	age = models.IntegerField(default=20)
	mobilenumber = models.CharField(max_length=10,null=True)
	uimg = models.ImageField(upload_to='Profilepics/',default='sofa.jpg')
	t = [(1,'Guest'),(2,'Manager'),(3,'User')]
	role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f = [(2,'Manager'),(3,'User')]
	roltype = models.IntegerField(choices=f)
	frpfe = models.ImageField(upload_to='Rolereqpics/',default='sofa.jpg')
	is_checked = models.BooleanField(default=False)
	funame = models.CharField(max_length=50)
	fud = models.OneToOneField(User,on_delete=models.CASCADE)


class OnlineFurniture(models.Model):
	fname = models.CharField(max_length=30)
	nitems = models.IntegerField()
	timings = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	frimg = models.ImageField(upload_to='Furnitureimages/',default='sofa.jpg')
	uid=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

	def __str__(self):
		return self.fname

class FitemList(models.Model):
	y = [('NV','Non-Veg'),('VG','Veg'),('Df','Select Item Type')]
	p = [('AV','Available'),('NA','Not Available'),('Sl','Select Availability')]
	finame = models.CharField(max_length=50)
	icategory = models.CharField(choices=y,default="Df",max_length=12) 
	price = models.DecimalField(decimal_places=2,max_digits=8)
	fiimage = models.ImageField(upload_to='Itemimages/',default='sofa.jpg')
	itavailability = models.CharField(choices=p,default="Sl",max_length=20)
	rsid= models.ForeignKey(OnlineFurniture,on_delete=models.CASCADE,default=1)


