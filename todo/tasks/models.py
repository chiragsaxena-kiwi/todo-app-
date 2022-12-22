from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return self.title



class Signup(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)

def __str__(self):
        return self.username


class Book(models.Model):
    title=models.CharField(max_length=100,blank=True)
    author=models.CharField(max_length=100,blank=True)
    isbn=models.CharField(max_length=100,blank=True)
    publisher=models.CharField(max_length=100,blank=True)

def __str__(self):
        return self.title
      