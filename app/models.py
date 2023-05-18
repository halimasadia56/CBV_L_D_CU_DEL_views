from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100)
    principle=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()

    def __str__(self): 
        return self.sname