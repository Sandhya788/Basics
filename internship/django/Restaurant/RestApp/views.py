from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,ItemsForm,UsgForm,Rltype,Rlupd,Pfupd,Changepwd
from RestApp.models import Restaurant,Restaurantlist,User,Rolereq
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from Restaurant import settings

# Create your views here.


def home(r):
	w=Restaurant.objects.filter(uid_id=r.user.id)
	t=Restaurant.objects.all()
	return render(r,'app/home.html',{'c':w,'y':t})
def about(r):
	return render(r,'app/about.html')
def contact(r):
	return render(r,'app/contact.html')

def login(r):
	return render(r,'app/login.html')

@login_required
def restlist(r):
	y=Restaurant.objects.filter(uid_id=r.user.id)
	if r.method=="POST":
		t=ReForm(r.POST,r.FILES)
		if t.is_valid():
			c=t.save(commit=False)
			c.uid_id=r.user.id
			c.save()
			messages.success(r,"Restaurant Added Successfully")
			return redirect('/rlist')
	t=ReForm()
	return render(r,'app/restaurantlist.html',{'q':t,'a':y})

@login_required
def rstup(r,m):
	k=Restaurant.objects.get(id=m)
	if r.method=="POST":
		e=ReForm(r.POST,r.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(r,"{} Restaurant Updated Successfully".format(k.rname))
			return redirect('/rlist')
	e=ReForm(instance=k)
	return render(r,'app/restupdate.html',{'x':e})

@login_required
def rstdl(r,s):
	g=Restaurant.objects.get(id=s)
	if r.method=="POST":
		messages.info(r,"{} Restaurant Deleted Successfully".format(g.rname))
		g.delete()
		return redirect('/rlist')
	return render(r,'app/restdelete.html',{'i':g})

@login_required
def rstvw(r,a):
	s=Restaurant.objects.get(id=a)
	return render(r,"app/restview.html",{'z':s})

@login_required
def ritems(re):
	st=list(Restaurant.objects.filter(uid_id=re.user.id))
	mm=Restaurantlist.objects.all()	
	d,i={},0
	for mp in mm:
		for h in st:
			if mp.rsid_id==h.id:
				d[i]=mp.iname,mp.icategory,mp.iprice,mp.imimg,mp.itavailability,mp.id,h.rname
				i=i+1
	if re.method=="POST":
		u=ItemsForm(re.POST,re.FILES)
		if u.is_valid():
			u.save()
			return redirect('/ritems')
	u=ItemsForm()
	return render(re,'app/restitems.html',{'q':u,'a':st,'m':d.values()})

@login_required
def itemupt(re,p):
	h=Restaurantlist.objects.get(id=p)
	if re.method=="POST":
		d=ItemsForm(re.POST,re.FILES,instance=h)
		if d.is_valid():
			d.save()
			return redirect('/ritems')
	d=ItemsForm(instance=h)
	return render(re,'app/itemupdate.html',{'s':d})

@login_required
def itemdel(r,v):
	l=Restaurantlist.objects.get(id=v)
	if r.method=="POST":
		l.delete()
		return redirect('/ritems')
	return render(r,'app/itemdelete.html',{'i':l})

@login_required
def itemviw(r,y):
	i=Restaurantlist.objects.get(id=y)
	return render(r,"app/itemview.html",{'j':i})


def usrreg(r):
	if r.method=="POST":
		d=UsgForm(r.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d=UsgForm()
	return render(r,'app/usrregister.html',{'t':d})

@login_required
def rolereq(request):
	p=Rolereq.objects.filter(ud_id=request.user.id).count()
	if request.method=="POST":
		k=Rltype(request.POST,request.FILES)
		#y=k.save(commit=False)
		if k.is_valid():
			y=k.save(commit=False)
			y.ud_id=request.user.id
			y.uname=request.user.username
			y.save()
			return redirect('/')
	k = Rltype()
	return render(request,'app/rolereq.html',{'d':k,'c':p})

@login_required
def gveperm(request):
	u=User.objects.all()
	r=Rolereq.objects.all()
	d={}
	for n in u:
		for m in r:
			if n.is_superuser==1 or n.id != m.ud_id:
				continue
			else:
				d[m.id]=m.uname,m.rltype,n.role,n.id
	return render(request,'app/gvper.html',{'h':d.values()})

@login_required
def gvupd(r,t):
	y=Rolereq.objects.get(ud_id=t)
	d=User.objects.get(id=t)
	if r.method=="POST":
		n=Rlupd(r.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked=1
			y.save()
			return redirect('/gvper')
	n=Rlupd(instance=d)
	return render(r,'app/gvepermision.html',{'c':n})

@login_required
def pfle(r):
	return render(r,'app/profile.html')

@login_required
def feedback(r):
	if r.method=="POST":
		sd=r.POST['snmail'].split(',')
		sm=r.POST['sub']
		mg=r.POST['msg']
		rt=settings.EMAIL_HOST_USER
		dt=send_mail(sm,mg,rt,sd)
		if dt==1:
			return redirect('/')
	return render(r,'app/feedback.html')

@login_required
def pfleupd(r):
	t=User.objects.get(id=r.user.id)
	if r.method=="POST":
		pfl=Pfupd(r.POST,r.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/pfle')
	pfl=Pfupd(instance=t)
	return render(r,'app/pfleupdate.html',{'u':pfl})

@login_required
def changepwd(r):
	if r.method=="POST":
		k=Changepwd(user=r.user,data=r.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k=Changepwd(user=r)
	return render(r,'app/changepwd.html',{'t':k})
















































