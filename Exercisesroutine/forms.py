from django.forms import ModelForm
from django import forms
from .models import *

EXERCISE_CHEST = (
    ('Flatpress', 'Flat Press'),
    ('Inclintpress', 'Incline Press'),
    ('Declientpress', 'Decline Press'),
    ('cableflys', 'Cable Flys'),)

class Targetchestworkoutform(forms.Form):

    workout1 = forms.ChoiceField(choices=EXERCISE_CHEST, required=False)
    workout2 = forms.ChoiceField(choices=EXERCISE_CHEST, required=False)
    workout3 = forms.ChoiceField(choices=EXERCISE_CHEST, required=False)
    workout4 = forms.ChoiceField(choices=EXERCISE_CHEST, required=False)





EXERCISE_BACK = (('Pullups','Pullups'),
               ('Bendoverrows','Bendoverrows'),
               ('Shugs','Shugs'),
               ('Dublerows','Dublerows'))

class Targetbackworkoutform(forms.Form):
    
    workout1 = forms.ChoiceField(choices=EXERCISE_BACK , required=False)
    workout2 = forms.ChoiceField(choices=EXERCISE_BACK , required=False)
    workout3 = forms.ChoiceField(choices=EXERCISE_BACK , required=False)
    workout4 = forms.ChoiceField(choices=EXERCISE_BACK , required=False)







EXERCISE_LEG = (('Squats','Squats'),
               ('Lunge','Lunge'),
               ('RDL','RDL'),
               ('Legpress','Legpress'))
        
class Targetlegworkoutform(forms.Form):
   
    workout1 = forms.ChoiceField(choices=EXERCISE_LEG, required=False)
    workout2 = forms.ChoiceField(choices=EXERCISE_LEG, required=False)
    workout3 = forms.ChoiceField(choices=EXERCISE_LEG, required=False)
    workout4 = forms.ChoiceField(choices=EXERCISE_LEG, required=False)








EXERCISE_CORE =  (('cablecrunch','cablecrunch'),
               ('Babyshark','Babyshark'),
               ('hanginglegraise','hanginglegraise'),
               ('plank','plank'))
        
class Targetcoreworkoutform(forms.Form):
   
    workout1 = forms.ChoiceField(choices=EXERCISE_CORE, required=False)
    workout2 = forms.ChoiceField(choices=EXERCISE_CORE, required=False)
    workout3 = forms.ChoiceField(choices=EXERCISE_CORE, required=False)
    workout4 = forms.ChoiceField(choices=EXERCISE_CORE, required=False)







EXERCISE_SHOULDER =  (('Frontrisese','Frontrisese'),
               ('Siderises','Siderises'),
               ('Facepull','Facepull'),
               ('Shugs','Shugs'))
   
class Targetshoulderworkoutform(forms.Form):
    
    workout1 = forms.ChoiceField(choices=EXERCISE_SHOULDER, required=False)
    workout2 = forms.ChoiceField(choices=EXERCISE_SHOULDER, required=False)
    workout3 = forms.ChoiceField(choices=EXERCISE_SHOULDER, required=False)
    workout4 = forms.ChoiceField(choices=EXERCISE_SHOULDER, required=False)



'''************************************WORKOUT LOG'S*****************************************************'''




class Workoutlogform(forms.Form):
    
    set1_weight_inkg = forms.IntegerField(required=False) 
    set1_reps = forms.IntegerField(required=False)

    set2_weight_inkg = forms.IntegerField(required=False)
    set2_reps = forms.IntegerField(required=False)

    set3_weight_inkg = forms.IntegerField(required=False)
    set3_reps = forms.IntegerField(required=False)

    set4_weight_inkg = forms.IntegerField(required=False)
    set4_reps = forms.IntegerField(required=False)







