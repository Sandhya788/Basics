from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#     	return self.name

# class Product(models.Model):
#     pname = models.CharField(max_length=50)
#     price = models.IntegerField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
#     description = models.CharField(max_length=200, default='' , null=True , blank=True)
#     pimage = models.ImageField(upload_to='Productimages/',default='logo.jpg')


class User(AbstractUser):
	age=models.IntegerField(default=20)
	mobilenumber=models.CharField(max_length=10,null=True)
	uimg=models.ImageField(upload_to='Profilepics/',default='logo.jpg')
	t=[(1,'Guest'),(2,'Manager'),(3,'User')]
	role=models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f = [(2,'Manager'),(3,'User')]
	rltype = models.IntegerField(choices=f)
	pfe = models.ImageField(upload_to='Rolereqpics/',default='logo.jpg')
	is_checked = models.BooleanField(default=False)
	uname = models.CharField(max_length=50)
	ud = models.OneToOneField(User,on_delete=models.CASCADE)

class Funiture(models.Model):
	rname=models.CharField(max_length=30)
	nitems=models.IntegerField()
	timings=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	rsimg=models.ImageField(upload_to='Restaurantimages/',default='logo.jpg')
	uid=models.ForeignKey(User,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.rname
	# @staticmethod
 #    def get_all():
 #    	return Restaurant.objects.all()
		
class Restaurantlist(models.Model):
	y=[('NV','Non-Veg'),('VG','Veg'),('Df','Select Item')]
	p=[('AV','Available'),('NA','Not-Available'),('Sl','Select Availability')]
	iname=models.CharField(max_length=50)
	icategory=models.CharField(choices=y,default="Df",max_length=12)
	iprice=models.DecimalField(decimal_places=2,max_digits=10)
	imimg=models.ImageField(upload_to='Itemimages/',default='logo.jpg')
	itavailability=models.CharField(choices=p,default="Sl",max_length=20)
	rsid= models.ForeignKey(Restaurant,on_delete=models.CASCADE)

	@staticmethod
	def get_all_Restaurantlist_by_categoryid(rsid_id):
		if rsid_id:
			return Restaurantlist.objects.filter(category=rsid_id)
		else:
			return Restaurantlist.get_all_Restaurantlist()


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Restaurantlist, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)
























