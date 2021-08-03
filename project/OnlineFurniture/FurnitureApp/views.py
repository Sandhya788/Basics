from django.shortcuts import render,redirect
from django.http import HttpResponse
from FurnitureApp.forms import FrForm,FitemsForm,UsgForm,Roltype,Rolupd,Pfupd,Chgepwd
from FurnitureApp.models import OnlineFurniture,FitemList,Rolereq,User,Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from OnlineFurniture import settings
# Create your views here.

def home(req):
	w=OnlineFurniture.objects.filter(uid_id=req.user.id)
	t=OnlineFurniture.objects.all()
	s=Product.objects.all()
	return render(req,'files/home.html',{'c':w,'y':t,'pr':s})
def about(req):
	return render(req,'files/about.html')

def contact(req):
	return render(req,'files/contact.html')

def furniturelist(req):
	y = OnlineFurniture.objects.all()
	if req.method == "POST":
		s = FrForm(req.POST)
		if s.is_valid():
			s.save()
			return redirect('/flist')
	
	s=FrForm()
	return render(req,'files/furniturelist.html',{'d':s,'a':y})

def frnupdate(req,j):
	k = OnlineFurniture.objects.get(id=j)
	if req.method == "POST":
		e =FrForm(req.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/flist')
	e = FrForm(instance=k)
	return render(req,'files/frnupdate.html',{'x':e})

def frdel(req,n):
	v = OnlineFurniture.objects.get(id=n)
	if req.method == "POST":
		v.delete()
		return redirect('/flist')
	return render(req,'files/frdelete.html',{'q':v})

def frview(req,a):
	s = OnlineFurniture.objects.get(id=a)
	return render(req,'files/frview.html',{'z':s})

# def fitlist(req):
# 	m = FitemList.objects.all()
# 	if req.method == "POST":
# 		k = FitemsForm(req.POST,req.FILES)
# 		if k.is_valid():
# 			n = k.save(commit=False)
# 			messages.success(req,'{} Item is Added Successfully'.format(n.finame))
# 			n.save()
# 			return redirect('/filist')
# 	k = FitemsForm()
# 	return render(req,'files/fitmlist.html',{'r':k,'s':m})

@login_required
def fitlist(req):
	st = list(OnlineFurniture.objects.filter(uid_id=req.user.id))
	mm = FitemList.objects.all()
	d,i = {},0
	for mp in mm:
		for h in st:
			if mp.rsid_id == h.id:
				d[i] = mp.finame,mp.icategory,mp.price,mp.fiimage,mp.itavailability,mp.id,h.fname
				i = i+1
	if req.method == "POST":
		k = FitemsForm(req.POST,req.FILES)
		if k.is_valid():
			k.save()
			return redirect('/filist')
	k = FitemsForm()
	return render(req,'files/fitmlist.html',{'r':k,'er':st,'s':d.values()})

@login_required
def furitmup(request,d):
	t = FitemList.objects.get(id=d)
	if request.method == "POST":
		z = FitemsForm(request.POST,request.FILES,instance=t)
		if z.is_valid():
			z.save()
			messages.info(request,"{} Item Updated Successfully".format(t.finame))
			return redirect('/filist')
	z = FitemsForm(instance=t)
	return render(request,'files/itemupdate.html',{'s':z})

@login_required
def furitmdl(request,te):
	p = FitemList.objects.get(id=te)
	if request.method == "POST":
		messages.waring(request,"{} Restaurant Deleted Successfully".format(p.finame))
		p.delete()
		return redirect('/filist')
	return render(request,'files/itemdl.html',{'a':p})

@login_required
def furitmvw(request,p):
	n = FitemList.objects.get(id=p)
	return render(request,'files/itmvw.html',{'d':n})

def furusrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'files/usrregister.html',{'t':d})

@login_required
def rolereq(request):
	p = Rolereq.objects.filter(fud_id=request.user.id).count()
	if request.method == "POST":
		k = Roltype(request.POST,request.FILES)
		if k.is_valid():
			y = k.save(commit=False)
			y.fud_id = request.user.id
			y.funame = request.user.username
			y.save()
			return redirect('/')
	k = Roltype()
	return render(request,'files/rolereq.html',{'d':k,'c':p})

@login_required
def gveperm(request):
	u = User.objects.all()
	r = Rolereq.objects.all()
	d = {}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id != m.fud_id:
				continue
			else:
				d[m.id] = m.funame,m.roltype,n.role,n.id,m.id
	return render(request,'files/gvper.html',{'h':d.values()})

@login_required
def gvupd(request,t):
	y = Rolereq.objects.get(fud_id=t)
	d = User.objects.get(id=t)
	if request.method == "POST":
		n = Rolupd(request.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked = 1
			y.save()
			return redirect('/gvper')
	n = Rolupd(instance=d)
	return render(request,'files/gvepermsion.html',{'c':n})

@login_required
def gvdlte(request,m):
	n = Rolereq.objects.get(id=m)
	t = User.objects.get(id=n.fud_id)
	if request.method == "POST":
		n.delete()
		t.role = 1
		t.save()
		return redirect('/gvper')
	return render(request,'files/gvdlte.html',{'d':n})

@login_required
def furpfle(request):
	return render(request,'files/profile.html')

@login_required
def furfeedback(request):
	if request.method == "POST":
		sd = request.POST['snmail'].split(',')
		sm = request.POST['sub']
		mg = request.POST['msg']
		rt = settings.EMAIL_HOST_USER
		dt = send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/')
	return render(request,'files/feedback.html')

@login_required
def furpfleupd(request):
	t = User.objects.get(id=request.user.id)
	if request.method == "POST":
		pfl = Pfupd(request.POST,request.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/frpfle')
	pfl = Pfupd(instance=t)
	return render(request,'files/pfleupdate.html',{'u':pfl})

@login_required
def furchangepwd(request):
	if request.method == "POST":
		k = Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = Chgepwd(user=request)
	return render(request,'files/changepwd.html',{'t':k})

@login_required
def furitemvew(request,s):
	r = FitemList.objects.filter(rsid_id=s)
	return render(request,'files/itemuser.html',{'tq':r})
