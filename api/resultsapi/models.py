from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import random

def generate_random_score():
    return random.randint(0, 100)

class BaseModel(models.Model):
    # This is an abstract base model for other models
    # it provides common fields that most models need
    # Every class must inherit from this base model 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        # mark as abstract model so that it cannot be used to create table in the database
        abstract = True

class Student(BaseModel,AbstractBaseUser):

    password = None
    
    email= models.EmailField(unique=True,verbose_name="email address")
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    state= models.CharField(max_length=200)
    subject_1 = models.CharField(max_length=200,null=True,blank=True)
    subject_2 = models.CharField(max_length=200,null=True,blank=True)
    subject_3 = models.CharField(max_length=200,null=True,blank=True)
    subject_4 = models.CharField(max_length=200,null=True,blank=True)
    subject_5 = models.CharField(max_length=200,null=True,blank=True)

    subject_1_score = models.IntegerField(null=True,blank=True)
    subject_2_score = models.IntegerField(null=True,blank=True)
    subject_3_score = models.IntegerField(null=True,blank=True)
    subject_4_score = models.IntegerField(null=True,blank=True)
    subject_5_score = models.IntegerField(null=True,blank=True)




    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email



