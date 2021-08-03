#from django.forms import ModelForm
from RestApp.models import Restaurant,Restaurantlist,User,Rolereq
from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class ReForm(forms.ModelForm):
	class Meta:
		model=Restaurant
		fields=['rname','nitems','timings','rsimg','address']
		widgets={
		"rname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant Name",
			}),
		"nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Number of Items Available in Restaurant",
			}),
		'timings':forms.TimeInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Timings",
			"type":"time"
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":5,
			}),
		}

class ItemsForm(forms.ModelForm):
	class Meta:
		model=Restaurantlist
		fields=['rsid','iname','icategory','iprice','itavailability','imimg']#__all__
		widgets={
		"rsid":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Restaurants",
			# "readonly":True,
			}),
		"iname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant Item",
			}),
		"icategory":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Item Category",
			}),
		"iprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Item Price",
			}),
		"itavailability":forms.Select(attrs={
			"class":"form-control my-2"
			}),
		}

class UsgForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Password",
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Confirm Password",
		}))
	class Meta:
		model=User
		fields=["username"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter name",
			}),
		}


class Rltype(forms.ModelForm):
	class Meta:
		model=Rolereq
		fields=['uname','rltype','pfe']
		widgets={
		'rltype':forms.Select(attrs={
			'class':'form-control my-2',
			}),
		}


class Rlupd(forms.ModelForm):
	class Meta:
		model=User
		fields=['username',"role"]
		widgets={
		'username':forms.TextInput(attrs={
			'class':'form-control my-2',
			"readonly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Pfupd(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','age','mobilenumber','uimg']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update first_name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update last_name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update age",
			}),
		"mobilenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update mobilenumber",
			}),
		}

class Changepwd(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter old Password",
		}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter New Password",
		}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter  New Confirm Password",
		}))
	class Meta:
		model=User
		# fields="__all__"
		fields=['old_password','new_password1','new_password2']
# class Pfe(forms.ModelForm):
# 	class Meta:
# 		model=User
# 		fields= __all__




