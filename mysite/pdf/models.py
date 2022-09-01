from django.db import models

class Profil(models.Model):  #tworzymy model w bazie danyc zawierajacy dane do CV

    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    nr_telefonu=models.CharField(max_length=200)
    informacje_ogolne=models.TextField(2000)
    wyksztalcenie= models.CharField(max_length=200)
    szkola= models.CharField(max_length=200)
    uniwersytet= models.CharField(max_length=200)
    doswiadczenie = models.TextField(max_length=1000)
    umiejetnosci=models.TextField(max_length=1000)

