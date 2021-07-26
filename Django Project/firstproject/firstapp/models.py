from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    age = models.IntegerField(default=20)
    mobilenumber = models.CharField(max_length=10,null=True)
    uimg = models.ImageField(upload_to='Profilepics/', default = 'logo.png')
    t = [(1,'Guest'),(2,'Manager'),(3,'User')]
    role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
    f = [(2,'Manager'),(3,'User')]
    rltype = models.IntegerField(choices=f)
    is_checked = models.BooleanField(default=False)
    Uname = models.CharField(max_length=50)
    ud = models.OneToOneField(User,on_delete=models.CASCADE)


class Userorder(models.Model):
    items=[('shirts','shirts'),('pants', 'pants'),('whites', 'whites'),('saree','saree'),('Select a Starter item', 'Select a Starter item')] 
    t1 = models.CharField(choices=items,default="Select",max_length=50)
    t1q = models.IntegerField(default=0)
    t2 = models.CharField(choices=items,default="Select",max_length=50)
    t2q = models.IntegerField(default=0)
    t3 = models.CharField(choices=items,default="Select",max_length=50)
    t3q = models.IntegerField(default=0)
    t4 = models.CharField(choices=items,default="Select",max_length=50)
    t4q = models.IntegerField(default=0)
    person = models.CharField(max_length=50,default="Type your name")
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=5000)
