from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Targetfoodroutine(models.Model):

    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    username = models.CharField(max_length=200,null=True,blank=True)

    breakfast = models.TextField(null=True,blank=True)

    breakfastcalories = models.IntegerField(null=True,unique=False,blank=True)

    lunch = models.TextField(null=True,blank=True)

    lunchcalories = models.IntegerField(null=True,unique=False,blank=True)

    dinner = models.TextField(null=True,blank=True)

    dinnercalories = models.IntegerField(null=True,unique=False,blank=True)

    snacks = models.TextField(null=True,blank=True)

    snackscalories = models.IntegerField(null=True,unique=False,blank=True)

    date = models.DateField(auto_now_add=True,blank=True)

    time = models.TimeField(auto_now_add=True,blank=True)

    def __str__(self) -> str:

        return 'Trgfodrutin-' + str(self.username) + '-' + str(self.date) + '-' + str(self.time)





class Meallog(models.Model):

    user =  user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    username = models.CharField(max_length=200,null=True,blank=True)

    meal_name = models.CharField(max_length=200,null=True,blank=True)

    meal_recipe = models.TextField(null=True,blank=True)

    calories = models.IntegerField(null=True,unique=False,blank=True)

    date = models.DateField(auto_now_add=True)
    
    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        
        return 'Meallog-' + str(self.username) + '-' + str(self.meal_name) + '-' + str(self.date) + '-' + str(self.time)



