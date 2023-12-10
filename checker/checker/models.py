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
    email= models.EmailField(unique=True)
    firstname= models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    state= models.CharField(max_length=200)

    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email

class Subjects(models.Model):
    subject_name= models.CharField(max_length=200)
    subject_score= models.IntegerField(blank=True,null=True)
    student= models.ForeignKey(Student, on_delete=models.CASCADE)

    def save(self,*args):
        score = generate_random_score()
        self.subject_score = score
        return super().save()