from django.urls import path
from car import views
from django.contrib.auth import views as v

urlpatterns = [
    path('home/',views.home,name="hm"),
    path('services/',views.services,name="sv"),
    path('carlist/',views.carlist,name="cl"),
    path('carupdate/<int:m>/',views.carupdate,name="cu"),
    path('cardelete/<int:n>/',views.cardelete,name="cd"),
    path('carview/<int:b>/',views.carview,name="cv"),
    path('registration/',views.registration,name="rg"),
    path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
    path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
    path('profile/',views.profile,name="pf"),
    path('profileupdate/',views.profileupdate,name="pfup"),
    path('feedback/',views.feedback,name="fd"),
    path('changepassword/',views.changepassword,name="chpd"),
    path('book/<int:a>/',views.book,name="bk"),
    path('confirmation/',views.confirmation,name="cf"),
    path('mybooking/',views.mybooking,name="mb"),
    path('bookingupdate/<int:z>/',views.bookupdate,name="bu"),
    path('bookcancel/<int:o>/',views.bookcancel,name="bo"),
    path('Userbookings/',views.userbookings,name="ub"),
    path('userbookcancel/<int:j>',views.userbookcancel,name="ubc")
]