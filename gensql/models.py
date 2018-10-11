from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey("gensql.Owner", on_delete=True)


class Owner(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
