from django.urls import path
from . import views 

urlpatterns = [

    path('mainpage/',views.Mainpage,name='main'),

    path('Auth/',views.Auth,name='auth'),

    path('Createuser/',views.Createuser,name='createuser'),

    path('logout/',views.Userlogout,name='logout')


]