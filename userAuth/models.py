from django.db import models
from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField
# Create your models here.


class Message_to_you(models.Model):

    Message = RichTextField(blank=False,null=True) 

    date = models.DateField(auto_now_add=True,blank=True)

    time = models.TimeField(auto_now_add=True,blank=True)

    def __str__(self) -> str:

        return str(self.Message)

class Visite(models.Model):

    viewed = models.CharField(max_length=200,blank=False,null=False)

    date = models.DateField(auto_now_add=True,blank=True)

    time = models.TimeField(auto_now_add=True,blank=True)

    def __str__(self) -> str:

        return str(self.viewed)

