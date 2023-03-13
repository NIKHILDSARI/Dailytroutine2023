from django.urls import path,include
from . import views
urlpatterns=[      
             
                    path('Exercises-history/',views.Gethistory,name='exercises-history'),


                    path('Targetexercises/',views.targetexercisesroutine,name = 'Targetexercises'),

                    
                    
                    path('logexercises/',views.Logexercises,name = 'logexercises'),
                    

                    
                    path('workoutlogger/<str:selected_exercises>/',views.Workoutlogger,name = 'workoutlogger'),

                

]