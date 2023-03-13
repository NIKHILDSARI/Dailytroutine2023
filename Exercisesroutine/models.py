from django.db import models
from django.contrib.auth.models import User 
# Create your models here.




class Targetchestworkout(models.Model):
    
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    username = models.CharField(max_length=200,null=True,blank=True)

    workout1 = models.CharField(max_length=200,null=True,blank=True)
    workout2 = models.CharField(max_length=200,null=True,blank=True)
    workout3 = models.CharField(max_length=200,null=True,blank=True)
    workout4 = models.CharField(max_length=200,null=True,blank=True)

    date = models.DateField(auto_now_add=True)

    time = models.TimeField(auto_now_add=True)
    
    def __str__(self) -> str:
         
         return 'Trgchst-'+ str(self.username) + '-' + str(self.date) + '-' + str(self.time)
    




class Targetbackworkout(models.Model):
   
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    username = models.CharField(max_length=200,null=True,blank=True)

    workout1 = models.CharField(max_length=200,null=True,blank=True)
    workout2 = models.CharField(max_length=200,null=True,blank=True)
    workout3 = models.CharField(max_length=200,null=True,blank=True)
    workout4 = models.CharField(max_length=200,null=True,blank=True)

    date = models.DateField(auto_now_add=True)

    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
         
         return 'Trgback-'+ str(self.username) + '-' + str(self.date) + '-' + str(self.time)






class Targetlegworkout(models.Model):
    
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    username = models.CharField(max_length=200,null=True,blank=True)

    workout1 = models.CharField(max_length=200,null=True,blank=True)
    workout2 = models.CharField(max_length=200,null=True,blank=True)
    workout3 = models.CharField(max_length=200,null=True,blank=True)
    workout4 = models.CharField(max_length=200,null=True,blank=True)

    date = models.DateField(auto_now_add=True)

    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
         
         return 'Trgleg-'+ str(self.username) + '-' + str(self.date) + '-' + str(self.time)
    





class Targetcoreworkout(models.Model):
   
    
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    username = models.CharField(max_length=200,null=True,blank=True)

    workout1 = models.CharField(max_length=200,null=True,blank=True)
    workout2 = models.CharField(max_length=200,null=True,blank=True)
    workout3 = models.CharField(max_length=200,null=True,blank=True)
    workout4 = models.CharField(max_length=200,null=True,blank=True)

    date = models.DateField(auto_now_add=True)

    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
         
         return 'Trgcore-'+ str(self.username) + '-' + str(self.date) + '-' + str(self.time)
    



class Targetshoulderworkout(models.Model):
   
    
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    username = models.CharField(max_length=200,null=True,blank=True)

    workout1 = models.CharField(max_length=200,null=True,blank=True)
    workout2 = models.CharField(max_length=200,null=True,blank=True)
    workout3 = models.CharField(max_length=200,null=True,blank=True)
    workout4 = models.CharField(max_length=200,null=True,blank=True)

    date = models.DateField(auto_now_add=True)

    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
         
         return 'Trgshlder-'+ str(self.username) + '-' + str(self.date) + '-' + str(self.time)
    




class Workoutlog(models.Model):
   
    
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    bodypart = models.CharField(max_length=200,null=True,)

    username = models.CharField(max_length=200,null=True,blank=True)

    exercises = models.CharField(max_length=200,null=True,)

    set1_weight_inkg = models.IntegerField(null=True,blank=True)
    set1 = models.IntegerField(null=True,blank=True)

    set2_weight_inkg = models.IntegerField(null=True,blank=True)
    set2 = models.IntegerField(null=True,blank=True)

    set3_weight_inkg = models.IntegerField(null=True,blank=True)
    set3 = models.IntegerField(null=True,blank=True)

    set4_weight_inkg = models.IntegerField(null=True,blank=True)
    set4 = models.IntegerField(null=True,blank=True)

    date = models.DateField(auto_now_add=True)

    time = models.TimeField(auto_now_add=True)


    def __str__(self) -> str:
         
         return str(self.username) + '-' +str(self.bodypary) + '-' + str(self.exercises) + '-' + str(self.date) + '-' + str(self.time)  
    

