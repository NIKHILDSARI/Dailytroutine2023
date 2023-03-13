from django.urls import path
from . import views
urlpatterns=[
                

                path('FoodrourineHistory/',views.Gethistory,name='foodroutine-history'),

                path('log/<str:meal_name>/',views.Log,name='log'),

                path('setfoodrouitne/',views.SettargetFoodroutine,name='setroutine')

                
]