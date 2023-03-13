from django.shortcuts import redirect
from django.contrib.auth import authenticate

def loginrequied(view_func):

    def wrapper_func(request,*args,**kwargs):


        if request.user.is_authenticated:
            
            return view_func(request,*args,**kwargs)
        
        else:

            return redirect('auth')

    return wrapper_func
