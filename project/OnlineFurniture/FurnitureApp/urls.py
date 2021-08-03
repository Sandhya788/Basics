from django.urls import path
from FurnitureApp import views
from django.contrib.auth import views as v

urlpatterns=[
	path('',views.home,name='hme'),
	path('abut/',views.about,name='abt'),
	path('cnct/',views.contact,name='cnt'),
	path('flist/',views.furniturelist,name='frlist'),
	path('frup/<int:j>/',views.frnupdate,name='frnup'),
	path('frdlt/<int:n>/',views.frdel,name="frdl"),
	path('frtviw/<int:a>/',views.frview,name="frvw"),
	path('filist/',views.fitlist,name="fits"),
	path('frilstup/<int:d>/',views.furitmup,name="fritup"),
	path('frilstdl/<int:te>/',views.furitmdl,name="fritdl"),
	path('frilstvw/<int:p>/',views.furitmvw,name="fritmv"),
	path('frrg/',views.furusrreg,name="reg"),
	path('login/',v.LoginView.as_view(template_name="files/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="files/logout.html"),name="lgo"),
	path('roltype/',views.rolereq,name="rlrq"),
	path('gvper/',views.gveperm,name="gvpm"),
	path('gvup/<int:t>/',views.gvupd,name="gvup"),
	path('gvpr/<int:m>/',views.gvdlte,name="gvdl"),
	path('frpfle/',views.furpfle,name="frpf"),
	path('frpfupd/',views.furpfleupd,name="frpfup"),
	path('frfdb/',views.furfeedback,name="frfd"),
	path('frchge/',views.furchangepwd,name="frchpd"),
	path('fritmd/<int:s>/',views.furitemvew,name="fritmvu"),
]