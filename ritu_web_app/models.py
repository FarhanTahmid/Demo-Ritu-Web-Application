from distutils.archive_util import make_zipfile
import email
from hashlib import blake2b
from shutil import _ntuple_diskusage
from django.db import models

# Create your models here.

class Players(models.Model):
    username=models.CharField(primary_key=True,null=False,blank=False,max_length=20)
    fullname=models.CharField(null=False,blank=False,max_length=50)
    mobileNumber=models.CharField(null=False,blank=False,max_length=15)
    email=models.EmailField(null=False,blank=False,max_length=30)
    address=models.CharField(null=False,blank=False,max_length=100)

    def __str__(self) :
        return self.username
class Task1Proof(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    #taskid= here comes the taskid field which will be generated from the tasktable
    proof=models.ImageField(null=True,blank=True)
    
    def __str(self):
        return self.player
class Task2Proof(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    #taskid= here comes the taskid field which will be generated from the tasktable
    proof=models.ImageField(null=True,blank=True)
    
    def __str(self):
        return self.player
class Task3Proof(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    #taskid= here comes the taskid field which will be generated from the tasktable
    proof=models.ImageField(null=True,blank=True)
    
    def __str(self):
        return self.player

class Task1Text(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    text=models.URLField(max_length=200,null=False,blank=False,verbose_name="text")
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."

class Task2Text(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    text=models.URLField(max_length=200,null=False,blank=False,verbose_name="text")
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."

class Task3Text(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    text=models.URLField(max_length=200,null=False,blank=False,verbose_name="text")
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."


