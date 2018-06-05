from django.db import models

class User(models.Model):
    SEX = (
        ('M','男'),
        ('F','女'),
        ('U','保密'),
    )
    nlck = models.CharField(max_length=32,unique=True)
    pssword = models.CharField(max_length=200)
    icon = models.ImageField()
    sex = models.CharField(max_length=32,choices=SEX)
    age = models.IntegerField()
