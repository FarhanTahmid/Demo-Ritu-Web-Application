from distutils.archive_util import make_zipfile
import email
from ftplib import MAXLINE
from hashlib import blake2b
from shutil import _ntuple_diskusage
from types import TracebackType
from django.db import models

# Players table
class Players(models.Model):
    username=models.CharField(primary_key=True,null=False,blank=False,max_length=20)
    fullname=models.CharField(null=False,blank=False,max_length=50)
    mobileNumber=models.CharField(null=False,blank=False,max_length=15)
    email=models.EmailField(null=False,blank=False,max_length=30)
    address=models.CharField(null=False,blank=False,max_length=100)
    picture=models.ImageField(null=True,blank=True)

    def __str__(self) :
        return self.username

#Proof of task 1 submission : multimedia 
class Task1Proof(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    #taskid= here comes the taskid field which will be generated from the tasktable
    proof=models.ImageField(null=True,blank=True)
    
    def __str(self):
        return self.player

#Proof of task 2 submission : multimedia 
class Task2Proof(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    #taskid= here comes the taskid field which will be generated from the tasktable
    proof=models.ImageField(null=True,blank=True)
    
    def __str(self):
        return self.player

#Proof of task 3 submission : multimedia 
class Task3Proof(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    #taskid= here comes the taskid field which will be generated from the tasktable
    proof=models.ImageField(null=True,blank=True)
    
    def __str(self):
        return self.player

#Proof of task 1 submission : URL of facebook post/drive link
class Task1Text(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE,db_constraint=False)
    text=models.URLField(max_length=200,null=False,blank=False,verbose_name="text")
    #time_added = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    earnedPoints=models.CharField(null=True,blank=True,max_length=30,verbose_name='Points')
    def __str__(self):
        return f"{self.text[:50]}..."

#Proof of task 2 submission : URL of facebook post/drive link
class Task2Text(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE,db_constraint=False)
    text=models.URLField(max_length=200,null=False,blank=False,verbose_name="text")
    # time_added = models.DateTimeField(auto_now_add=True)
    earnedPoints=models.CharField(null=True,blank=True,max_length=30,verbose_name='Points')

    def __str__(self):
        return f"{self.text[:50]}..."

#Proof of task 3 submission : URL of facebook post/drive link
class Task3Text(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE,db_constraint=False)
    text=models.URLField(max_length=200,null=False,blank=False,verbose_name="text")
    # time_added = models.DateTimeField(auto_now_add=True)
    earnedPoints=models.CharField(null=True,blank=True,max_length=30,verbose_name='Points')

    def __str__(self):
        return f"{self.text[:50]}..."



#Points table for leaderboard
class Leaderboard(models.Model):
    player=models.ForeignKey(Players,null=False,blank=False,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True,verbose_name="Name")
    earnedPoints=models.CharField(null=True,blank=True,max_length=30,verbose_name='Points')

    def __str__(self):
        return self.player.username



#The items to be sold in marketplace for various tasks
class Marketplace(models.Model):
    product_name=models.CharField(null=False,blank=False,max_length=100,verbose_name="Name")
    product_desc=models.CharField(null=False,blank=False,max_length=150,verbose_name="Description")
    product_price=models.CharField(max_length=20,null=False,blank=False,verbose_name="Price")
    product_img=models.ImageField(null=True,blank=True,verbose_name="Image")

    def __str__(self):
        return self.product_name

