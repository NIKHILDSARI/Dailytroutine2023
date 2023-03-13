from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q
from userAuth.decorators import loginrequied

# Create your views here.


@loginrequied
def targetexercisesroutine(request):
    context = {}
    
    if request.method == 'POST':

        if 'save' in request.POST:

            user = request.user

            username = request.user.username

            bodypart_number = int(request.GET.get('bodypart_number'))

            if bodypart_number == 0:

                chestform = Targetchestworkoutform(request.POST)

                if chestform.is_valid():
                   chesttrgt_inst= Targetchestworkout.objects.create(user=user,
                                                                username=username,
                                                                workout1=chestform.cleaned_data.get('workout1'),
                                                                workout2=chestform.cleaned_data.get('workout2'),
                                                                workout3=chestform.cleaned_data.get('workout3'),
                                                                workout4=chestform.cleaned_data.get('workout4'))
                   
                else:

                    return HttpResponse('error at targetchest')
                
                context['fromtrgtworkout'] = 'Your Target ChestWorkout is Saved and Updated to Exercises Logger' 

                context['workouts'] = chesttrgt_inst

                return render(request,'Exercisesroutine/trgtworkouts.html',context)

            if bodypart_number == 1:    

                backform = Targetbackworkoutform(request.POST)

                if backform.is_valid():
                    backtrgt_inst =Targetbackworkout.objects.create(user=user,
                                                                username=username,
                                                                workout1=backform.cleaned_data['workout1'],
                                                                workout2=backform.cleaned_data['workout2'],
                                                                workout3=backform.cleaned_data['workout3'],
                                                                workout4=backform.cleaned_data['workout4'] )
                else:

                    return HttpResponse('error at targetback')
                
                context['fromtrgtworkout'] = 'Your Target BackWorkout is Saved and Updated to Exercises Logger' 

                context['workouts'] = backtrgt_inst
                
                return render(request,'Exercisesroutine/trgtworkouts.html',context)

            if bodypart_number == 2:        

                legform = Targetlegworkoutform(request.POST)

                if legform.is_valid():
                    legtrgt_inst = Targetlegworkout.objects.create(user=user,
                                                                username=username,
                                                                workout1=legform.cleaned_data['workout1'],
                                                                workout2=legform.cleaned_data['workout2'],
                                                                workout3=legform.cleaned_data['workout3'],
                                                                workout4=legform.cleaned_data['workout4'] )
                    
                else:

                    return HttpResponse('error at targetleg')
                
                
                context['fromtrgtworkout'] = 'Your Target LegWorkout is Saved and Updated to Exercises Logger' 

                context['workouts'] = legtrgt_inst
                
                return render(request,'Exercisesroutine/trgtworkouts.html',context)
                
            if bodypart_number == 3:

                coreform = Targetcoreworkoutform(request.POST)

                if coreform.is_valid():
                    coretrgt_inst = Targetcoreworkout.objects.create(user=user,
                                                                username=username,
                                                                workout1=coreform.cleaned_data['workout1'],
                                                                workout2=coreform.cleaned_data['workout2'],
                                                                workout3=coreform.cleaned_data['workout3'],
                                                                workout4=coreform.cleaned_data['workout4'] )
                    
                else:

                    return HttpResponse('error at targetcore')
                
                context['fromtrgtworkout'] = 'Your Target CoreWorkout is Saved and Updated to Exercises Logger' 

                context['workouts'] = coretrgt_inst
                
                return render(request,'Exercisesroutine/trgtworkouts.html',context)
                
            if bodypart_number == 4:    

                shoulderform = Targetshoulderworkoutform(request.POST)

                if shoulderform.is_valid():
                    shouldertrgt_inst = Targetshoulderworkout.objects.create(user=user,
                                                                username=username,
                                                                workout1=shoulderform.cleaned_data['workout1'],
                                                                workout2=shoulderform.cleaned_data['workout2'],
                                                                workout3=shoulderform.cleaned_data['workout3'],
                                                                workout4=shoulderform.cleaned_data['workout4'] )
                    
                else:

                    return HttpResponse('error at targetshoulder')
                
                context['fromtrgtworkout'] = 'Your Target ShouldertWorkout is Saved and Updated to Exercises Logger' 

                context['workouts'] = shouldertrgt_inst
                
                return render(request,'Exercisesroutine/trgtworkouts.html',context)
            
            return HttpResponse('done')
        
        else:

            return HttpResponse('not done')
    else:

        context['Targetchestworkoutform']    =  Targetchestworkoutform()
        context['Targetbackworkoutform']     =  Targetbackworkoutform()
        context['Targetlegworkoutform']      =  Targetlegworkoutform()
        context['Targetcoreworkoutform']     =  Targetcoreworkoutform()
        context['Targetshoulderworkoutform'] =  Targetshoulderworkoutform()


    return render(request,'Exercisesroutine/trgtexercisesroutine.html',context)





@loginrequied
def Logexercises(request):

    context = {}

    user = request.user

    chesttrgtworkouts = Targetchestworkout.objects.filter(user=user)

    if not chesttrgtworkouts:
         context['chestworkout'] = ''
    else:    
        for i in chesttrgtworkouts:
            chestworkouts = i
        context['chestworkout'] = chestworkouts


    backtrgtworkouts = Targetbackworkout.objects.filter(user=user)

    if not backtrgtworkouts:
       context['backworkout'] = ''
    else:
        for i in backtrgtworkouts:
            backworkouts = i
        context['backworkout'] = backworkouts


    legtrgtworkouts = Targetlegworkout.objects.filter(user=user)

    if not legtrgtworkouts:
       context['legworkout'] = ''
    else:
        for i in legtrgtworkouts:
            legworkouts = i
        context['legworkout'] = legworkouts


    coretrgtworkouts = Targetcoreworkout.objects.filter(user=user)

    if not coretrgtworkouts:
        context['coreworkout'] = ''
    else:
        for i in coretrgtworkouts:
            coreworkouts = i
        context['coreworkout'] =  coreworkouts


    shouldertrgtworkouts = Targetshoulderworkout.objects.filter(user=user)

    if not shouldertrgtworkouts:
        context['shoulderworkout'] = ''

    else:
        for i in shouldertrgtworkouts:

            shoulderworkouts = i

        context['shoulderworkout'] = shoulderworkouts


    if request.method == 'POST':
        bodypart = str(request.GET.get('bodypart'))

        if bodypart == 'chest':

            selected_exercises = request.POST['exercises'] + str(0)
            return redirect('workoutlogger',selected_exercises)
        
        elif bodypart == 'back':

            selected_exercises = request.POST['exercises'] + str(1)
            return redirect('workoutlogger',selected_exercises)
        
        elif bodypart == 'leg':

            selected_exercises = request.POST['exercises'] + str(2)
            return redirect('workoutlogger',selected_exercises)
        
        elif bodypart == 'core':

            selected_exercises = request.POST['exercises'] + str(3)
            return redirect('workoutlogger',selected_exercises)
        
        elif bodypart == 'shoulder':

            selected_exercises = request.POST['exercises'] + str(4)
            return redirect('workoutlogger',selected_exercises)
        
        else:

            return HttpResponse('error at bodypart string')
       
    else:

        return render(request,'Exercisesroutine/exerciseslog.html',context)
    



@loginrequied
def Workoutlogger(request,selected_exercises):
    context = {}

    if request.method == 'GET':

        exercises = selected_exercises[:-1]

        bodypart = int(selected_exercises[-1])

        if bodypart == 0:
            context['bodypart'] = 'chest'

        elif bodypart == 1:
            context['bodypart'] = 'back'

        elif bodypart == 2:
            context['bodypart'] = 'leg'

        elif bodypart == 3:
            context['bodypart'] = 'core'

        elif bodypart == 4:
            context['bodypart'] = 'shoulder'

        else:
            return HttpResponse('error at bodypart number')
        
        context['exercises'] = exercises

    else:
            form = Workoutlogform(request.POST)

            if form.is_valid():

                user = request.user

                username = user.username

                exercises = request.POST['exercises']

                bodypart = request.POST['bodypart']

                workout_inst =  Workoutlog.objects.create(user=user,bodypart=bodypart,
                                          username=username,exercises=exercises,
                                          set1_weight_inkg=form.cleaned_data.get('set1_weight_inkg'),
                                          set1=form.cleaned_data.get('set1_reps'),
                                          set2_weight_inkg=form.cleaned_data.get('set2_weight_inkg'),
                                          set2=form.cleaned_data.get('set2_reps'),
                                          set3_weight_inkg=form.cleaned_data.get('set3_weight_inkg'),
                                          set3=form.cleaned_data.get('set3_reps'),
                                          set4_weight_inkg=form.cleaned_data.get('set4_weight_inkg'),
                                          set4=form.cleaned_data.get('set4_reps'))
        
            context['message'] = 'Your Exercises ' +str(exercises) + ' is Saved'

            context['workout_inst'] = workout_inst

            return render(request,'Exercisesroutine/workoutsave.html',context)
        
    context['Workoutlog'] = Workoutlogform()

    return render(request,'Exercisesroutine/workoutlog.html',context)






@loginrequied
def Gethistory(request):
    
    if request.method == 'POST':
        user = request.user

        context = {}

        if 'get_trgt_workout_routine_by_bodypart' in request.POST:

            count = 0
            
            user = request.user
            
            required_part = request.POST['trgthistory']

            if required_part == 'Chest': 
                
                part_inst = reversed(Targetchestworkout.objects.filter(user=user))
            
            elif required_part == 'Back':

                part_inst = reversed(Targetbackworkout.objects.filter(user=user))
            
            elif required_part == 'Leg':

                part_inst = reversed(Targetlegworkout.objects.filter(user=user))

            elif required_part == 'Core':

                part_inst = reversed(Targetcoreworkout.objects.filter(user=user))

            elif required_part == 'Shoulder':

                part_inst = reversed(Targetshoulderworkout.objects.filter(user=user))

            else:

                return HttpResponse('error at Gethistory-- trgthistory')
            
            for i in part_inst:

                required_data = {}
                
                count +=1
                
                required_data['part_inst'] = i

                context[count] = required_data

            received = 'trgthistory'

        elif 'loghistory' in request.POST:

            count = 0

            part_inst = reversed(Workoutlog.objects.filter(user=user))

            for i in part_inst:

                required_data = {}
                
                count +=1

                required_data['part_inst'] = i

                context[count] = required_data

            received = 'loghistory'

        elif 'loghistorybydatebutton' in request.POST:
            count=0

            start = request.POST['from']
            
            end = request.POST['to']

            if start == '' or end == '':

                return HttpResponse('Please fill both from and to dates')

            required_part = request.POST['loghistorybydate']
            
            part_inst = reversed(Workoutlog.objects.filter(Q(user=user) & Q(date__gte=start) & Q(date__lte=end) & Q(bodypart=required_part)))

            for i in part_inst:

                user_data = {}

                count +=1

                user_data['part_inst'] = i

                context[count] = user_data

            received = 'loghistorybydatebutton'
        
        else:
            return HttpResponse('notok')

        return render(request,'Exercisesroutine/gethistoryEX.html',{'context':context,'user':user,
                                                                        'received':received})

    return render(request,'Exercisesroutine/Gethistory.html')