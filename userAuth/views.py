from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import *

# Create your views here.

def Auth(request):

    context = {}

    if request.method == 'POST':

        if 'send_message' in request.POST:
            
            form = Message_to_nikhil_form(request.POST)

            if form.is_valid:

                form.save()

                return HttpResponse('Your Message is sent')

        if 'login' in request.POST:

            username = request.POST['username']
            password = request.POST['password']



            if username == 'testuser1' and password == 'testpass1':

                Website_footfall_and_actionstatus({'viewed':'used_samples'})

            if username != 'testuser1' or password != 'testpass1':

                Website_footfall_and_actionstatus({'viewed':'random_clicks'})




            user = authenticate(request,username=username,password=password)

            if user is not None:
                
                login(request,user)
                
                return redirect('homepage')
            
            else:

                return redirect('createuser')
            
    context['message'] = Message_to_nikhil_form()

    Website_footfall_and_actionstatus({'viewed':'viewed'})

    return render(request,'userAuth/Auth.html',context)






def Createuser(request):
    context = {}

    if request.method == 'POST':

        form = usercreationform(request.POST)

        if form.is_valid():

            form_inst = form.save()
            
            context['received'] = 'createsuccess'

            context['username'] = form_inst.username

            return render(request,'userAuth/creationsuccess.html',context)
        
        else:
            
            return render(request,'userAuth/creationformvalidatiom.html')
    
    context['form'] = usercreationform()

    Website_footfall_and_actionstatus({'viewed':'random_clicks_usercreate'})

    return render(request,'userAuth/Createuser.html',context)






def Userlogout(request) -> redirect:

    logout(request)

    return redirect('auth')


def Website_footfall_and_actionstatus(viewed):

    Visite.objects.create(viewed =viewed['viewed'])



def Mainpage(request):
     
    Website_footfall_and_actionstatus({'viewed':'reached_mainpage'})

    return render(request,'userAuth/mainpage.html')

