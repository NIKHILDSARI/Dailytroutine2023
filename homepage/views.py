from django.shortcuts import render,redirect
from django.http import HttpResponse
from userAuth.decorators import loginrequied

# Create your views here.
@loginrequied
def Homepage(request):
    
    context = {}


    if request.method == 'POST':


        if 'set_workout_routine' in request.POST :
            
            return redirect('Targetexercises')
        
        elif 'logout' in request.POST:

            return redirect('logout')
    
        elif 'start_workout' in request.POST:

            return redirect('logexercises')
    
        elif 'Foodroutine_history' in request.POST:

            return redirect('foodroutine-history')
        
        elif 'loguser_meal' in request.POST:

            meal_name = str(request.POST['mealdropdown'])

            return redirect('log',meal_name)
        
        elif 'user_exercises-history' in request.POST:

            return redirect('exercises-history')
        
        else:

            return HttpResponse('error at Homepage')
        
    context['user'] = request.user.username

    return render(request,'Homepage/homepage.html')
    