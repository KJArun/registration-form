from django.db import models

class Responses(models.Model):
    Name=models.CharField(max_length=30,default="")
    Email=models.CharField(max_length=30,default="")
    Phone=models.CharField(max_length=30,default="")
    Department=models.CharField(max_length=30,default="")
    Year=models.CharField(max_length=30,default="")
    Title=models.CharField(max_length=30,default="")
    Link=models.CharField(max_length=300,default="")
    def __str__(self):
        return self.Email
    

