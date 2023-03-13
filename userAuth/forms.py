from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class usercreationform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class Message_to_nikhil_form(ModelForm):
    
    class Meta:
        
        model = Message_to_you

        fields = '__all__'