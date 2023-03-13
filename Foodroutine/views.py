from django.shortcuts import render
from .forms import *
from django.shortcuts import HttpResponse,redirect
from .models import *
from django.db.models import Q
from userAuth.decorators import loginrequied


@loginrequied
def Log(request,meal_name):

    context = {}

    if request.method == 'POST':

        if 'back' in request.POST:

            return redirect('meallog')
        
        elif 'save' in request.POST:

            forms = Meallogform(request.POST)

            if forms.is_valid():
                user = request.user

                username = user.username

                mealname = request.POST['mealname']

                mealrecipe = forms.cleaned_data.get('Meal_Recipe')

                calories = forms.cleaned_data.get('Meal_calories')

                meallog_inst = Meallog.objects.create(user=user,
                                                    username=username,
                                                    meal_name=mealname,
                                                    meal_recipe=mealrecipe,
                                                    calories=calories)
                
                context['user']=user

                context['meallog_inst'] = meallog_inst

                return render(request,'Foodroutine/Logsave.html',context)    
                
        else:

            return HttpResponse('error at logsave')    

    
    context['form'] = Meallogform()

    context['meal_name'] = meal_name
    
    return render(request,'Foodroutine/Log.html',context)


@loginrequied
def SettargetFoodroutine(request):
    context = {}

    
    if request.method == 'POST':
            
            if 'fromhomepage_settargtfoodroutine_dropdown' in request.POST:

                context['meal'] = request.POST['mealdropdown']

                context['form'] = SettargetFoodroutineform()

                return render(request,'Foodroutine/SettargetFoodroutine.html',context)
            
            elif 'from_save_trgtfoodroutine' in request.POST:
                    user = request.user

                    username = user.username

                    meal = request.POST['meal']

                    form = SettargetFoodroutineform(request.POST)
                    
                    if form.is_valid():
                        mealname_to_set = form.cleaned_data.get('Meal_Recipe')

                        mealcalorie_to_set =form.cleaned_data.get('Meal_calories')

                        if meal == 'breakfast':
                            trgtmeal_inst = Targetfoodroutine.objects.create(user=user,
                                                                                username=username,
                                                                                    breakfast=mealname_to_set,
                                                                                    breakfastcalories=mealcalorie_to_set)
                        elif meal == 'lunch':
                            trgtmeal_inst = Targetfoodroutine.objects.create(user=user,
                                                                                    username=username,
                                                                                    lunch= mealname_to_set,
                                                                                    lunchcalories=mealcalorie_to_set)
                                                                                    
                        elif meal == 'dinner':
                            trgtmeal_inst = Targetfoodroutine.objects.create(user=user,
                                                                                    username=username,
                                                                                    dinner= mealname_to_set,
                                                                                    dinnercalories=mealcalorie_to_set)
                        elif meal == 'snacks':
                            trgtmeal_inst = Targetfoodroutine.objects.create(user=user,
                                                                                    username=username,
                                                                                    snacks= mealname_to_set,
                                                                                    snackscalories=mealcalorie_to_set
                                                                                    )
                        else:

                            return HttpResponse('error at SettargetFoodroutine POST')
                        
                        context['meal'] = meal

                        context['recipe'] = mealname_to_set
                        
                        context['calories'] = mealcalorie_to_set

                        return render(request,'Foodroutine/trgtsave.html',context)
                    
                    else:

                        return HttpResponse(form.errors)
                        
            else:

                return HttpResponse('error at creating model')
    

@loginrequied
def Gethistory(request):

    context = {}

    if request.method == 'POST':

        if 'get_targetfoodroutine_history' in request.POST:

            user_required_meal = request.POST['mealdropdown']

            context = gethistory(request,context,user_required_meal)

            return render(request,'Foodroutine/gethistoryroutine.html',{'context':context,
                                                                        'user_required_meal':user_required_meal,
                                                                        'user':request.user.username})
        


        elif 'get_targetfoodroutine_history_bydate' in request.POST:

            start_date = request.POST['from_date'] 

            end_date = request.POST['to_date']

            if start_date == '' or end_date == '':

                return HttpResponse('Please fill both from and to dates')

            required_part = request.POST['loghistorybydate']

            user_required_meal = request.POST['mealdropdown']

            context = getbydate(request,context,start_date,end_date,user_required_meal)

            return render(request,'Foodroutine/gethistoryroutine.html',{'context':context,
                                                                        'user_required_meal':user_required_meal,
                                                                        'user':request.user.username})
                                                


        elif 'get_loggedmeals_history' in request.POST:

            user_required_meal = request.POST['mealdropdown']

            context = getloghistory(request,context,user_required_meal)

            return render(request,'Foodroutine/gethistoryroutine.html',{'context':context,
                                                                        'user_required_meal':user_required_meal,
                                                                        'user':request.user.username})


        elif 'get_loggedmeals_history_bydate' in request.POST:

            start_date = request.POST['from_date']

            end_date = request.POST['to_date']

            if start_date == '' or end_date == '':

                return HttpResponse('Please fill both from and to dates')

            user_required_meal = request.POST['mealdropdown']

            context = getlogbydate(request,context,start_date,end_date,user_required_meal)

            return render(request,'Foodroutine/gethistoryroutine.html',{'context':context,
                                                                        'user_required_meal':user_required_meal,
                                                                        'user':request.user.username})

        else:

            return HttpResponse('error at gethistory POST')




    return render(request,'Foodroutine/Gethistory.html')        


@loginrequied
def gethistory(request,context,user_required_meal)-> dict:
    user = request.user

    count = 0

    trgthistory_inst = reversed(Targetfoodroutine.objects.filter(user=user))

    for i in trgthistory_inst:

        meal_data= {}
        
        date = i.date

        if user_required_meal == 'Breakfast':
            meal = i.breakfast

            calories = i.breakfastcalories
        elif user_required_meal == 'Lunch':
            meal = i.lunch
            calories = i.lunchcalories

        elif user_required_meal == 'Dinner':
            meal = i.dinner
            calories = i.dinnercalories

        elif user_required_meal == 'Snacks':
            meal = i.snacks
            calories = i.snackscalories

        else:

            return HttpResponse('error at gethistory method')
        
        meal_data['date'] = date

        if meal is None:
            meal_data['meal'] = 'No Breakfast Entry on This Day'
            meal_data['calories'] = '0'

        else:
            meal_data['meal'] = meal
            meal_data['calories'] = calories

        count +=1

        context[count] = meal_data
    return context



@loginrequied
def getbydate(request,context,start_date,end_date,user_required_meal):
    user = request.user

    count = 0

    trgthistory_inst = reversed(Targetfoodroutine.objects.filter(Q(user=user) & Q(date__gte=start_date) & Q(date__lte=end_date) ))
    
    for i in trgthistory_inst:

        meal_data= {}
        
        date = i.date

        if user_required_meal == 'Breakfast':
            meal = i.breakfast
            calories = i.breakfastcalories

        elif user_required_meal == 'Lunch':
            meal = i.lunch
            calories = i.lunchcalories

        elif user_required_meal == 'Dinner':
            meal = i.dinner
            calories = i.dinnercalories

        elif user_required_meal == 'Snacks':
            meal = i.snacks
            calories = i.snackscalories

        else:
            return HttpResponse('error at gethistory method')
        
        meal_data['date'] = date

        if meal is None:
            meal_data['meal'] = 'No Breakfast Entry on This Day'
            meal_data['calories'] = '0'

        else:
            meal_data['meal'] = meal
            meal_data['calories'] = calories

        count +=1

        context[count] = meal_data
    return context




@loginrequied
def getloghistory(request,context,user_required_meal):
    user = request.user

    count = 0

    loghistory_inst = reversed(Meallog.objects.filter(Q(user=user) & Q(meal_name=user_required_meal)))

    for i in loghistory_inst:

        meal_data= {}
        
        date = i.date

        meal_data['date'] = date

        if i.meal_recipe is None:
            meal_data['meal'] = 'No Breakfast Entry on This Day'
            meal_data['calories'] = '0'

        else:
            meal_data['meal'] = i.meal_recipe
            meal_data['calories'] = i.calories

        count +=1

        context[count] = meal_data
    return context




@loginrequied
def getlogbydate(request,context,start_date,end_date,user_required_meal):
    user = request.user

    count = 0

    loghistory_inst = reversed(Meallog.objects.filter(Q(user=user) & Q(meal_name=user_required_meal) &
                                                       Q(date__gte=start_date) & Q(date__lte=end_date)))

    for i in loghistory_inst:

        meal_data= {}
        
        date = i.date

        meal_data['date'] = date

        if i.meal_recipe is None:
            meal_data['meal'] = 'No Breakfast Entry on This Day'
            meal_data['calories'] = '0'
        else:
            meal_data['meal'] = i.meal_recipe
            meal_data['calories'] = i.calories

        count +=1

        context[count] = meal_data
    return context
