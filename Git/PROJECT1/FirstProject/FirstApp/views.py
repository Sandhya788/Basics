from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
# Create your views here.

def home(request):
	return HttpResponse("hii good evening to all....")

def htmltag(y):
	return HttpResponse("<h2> Hi Welcome To APSSDC Programs</h2>")

def usrnameprint(req,uname):
	return HttpResponse("<h2 style='text-align:center'>Hi Welcome <span style='color:green'>{}</span></h2>".format(uname))

def usernameage(req,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:green;padding:1px'> Hi user <span style='color:yellow'>{}</span> and your age is: <span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(req,eid,enm,eage):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Hi Welcome {} your age is: {} and your id is:{}</h3>".format(enm,enm,eage,eid))

def html(req):
	return render(req,'html/sample.html')

def ytname(req,name):
	return render(req,'html/ytname.html',{'n':name})

def empname(re,ename,id):
	k={'i':id,'n':ename}
	return render(re,'html/empname.html',k)
def studentdetails(r):
	return render(r,'html/std.html')

def internalJS(r):
	return render(r,'html/internalJS.html')

def myform(r):
	if r.method=="POST":
		#print(r.POST)
		uname=r.POST['uname']
		rollno=r.POST['rollno']
		email=r.POST.get('email')
		#print(uname,rollno,email)
		data={'username':uname,'rno':rollno,'emailid':email}
		return render(r,'html/display.html',data)
	return render(r,'html/myform.html')

def bootstrapfun(r):
	return render(r,'html/sampleboot.html')

def btregi(req):
	return render(req,'html/btregst.html')

def register1(r):
	#name="siva"
	#email="siva@gmail.com"
	reg=Register(name="siva1",email="siva123@gmail.com")
	reg.save()
	return HttpResponse("row inserted successfully...")

def register2(re):
	if re.method=='POST':
		name=re.POST['name']
		email=re.POST['email']
		reg=Register(name=name,email=email)
		reg.save()
		return HttpResponse('inserted successfully')
	return render(re,'html/register2.html')

def display(r):
	data=Register.objects.all()
	return render(r,'html/display1.html',{'data':data})
def sview(r,y):
	w=Register.objects.get(id=y)
	return render(r,'html/sviews.html',{'y':w})
	#return HttpResponse('your name is :{} and ur email id is:{}'.format(w.name,w.email))

def supt(r,q):
	t=Register.objects.get(id=q)
	if r.method=="POST":
		na=r.POST['n']
		em=r.POST['e']
		t.name=na
		t.email=em
		t.save()
		return redirect('/display')
	return render(r,'html/supdate.html',{'p':t})


def delete(r,d):
	b=Register.objects.get(id=d)
	if r.method=="POST":
		b.delete()
		return redirect('/display')
	return render(r,'html/sndlt.html',{'z':b})
	#i=Register.objects.get(id=d)
	#i.delete()
	#return HttpResponse('row deleted successfully')























