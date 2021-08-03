from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm
from RestApp.models import Restaurant
# Create your views here.


def home(r):
	return render(r,'app/home.html')
def about(r):
	return render(r,'app/about.html')
def contact(r):
	return render(r,'app/contact.html')

def login(r):
	return render(r,'app/login.html')


def restlist(r):
	y=Restaurant.objects.all()
	if r.method=="POST":
		t=ReForm(r.POST)
		if t.is_valid():
			t.save()
			return redirect('/rlist')
	t=ReForm()
	return render(r,'app/restaurantlist.html',{'q':t,'a':y})

def rstup(r,m):
	k=Restaurant.objects.get(id=m)
	if r.method=="POST":
		e=ReForm(r.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/rlist')
	e=ReForm(instance=k)
	return render(r,'app/restupdate.html',{'x':e})

def rstdl(r,s):
	g=Restaurant.objects.get(id=s)
	if r.method=="POST":
		g.delete()
		return redirect('/rlist')
	#w=ReForm()
	return render(r,'app/restdelete.html',{'i':g})













