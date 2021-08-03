from django.forms import ModelForm
from FurnitureApp.models import OnlineFurniture,FitemList,User,Rolereq
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class FrForm(ModelForm):
	class Meta:
		model = OnlineFurniture
		# fields = "__all__"
		fields = ["fname","nitems","timings","frimg","address"]
		widgets = {
		"fname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Furniture Name",
			}),
		"nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Number of Items available in Restaurant",
			}),
		"timings":forms.TimeInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter timings",
			"type":"time",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":3,
			}),
		}


class FitemsForm(forms.ModelForm):
	class Meta:
		model = FitemList
		fields = ['rsid','finame','icategory','price','itavailability','fiimage']
		widgets = {
		"rsid":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Furnitures"
			}),
		"finame":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Item Name",
			}),
		"icategory":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Item",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Price",
			}),
		'itavailability':forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Confirm Password",
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

class Roltype(forms.ModelForm):
	class Meta:
		model = Rolereq
		fields = ["funame","roltype","frpfe"]
		widgets = {
		"roltype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Rolupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Pfupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","age","mobilenumber","uimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
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
			"placeholder":"Update Mobile Number",
			}),
		}

class Chgepwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Old Password"
		}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Password",
		}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]