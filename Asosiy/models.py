from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    tanvol = [

        ("bajarilmoqda","bajarilmoqda"),

        ("bajarilmadi","bajarilmadi"),

        ("boshlanmadi", "boshlanmadi")
    ]
    sarlavha = models.CharField(max_length=100)
    batafsil = models.TextField()
    holat = models.CharField(max_length=100, choices=tanvol)
    vaqt = models.DateField()
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.sarlavha


class Muallif(models.Model):
    tanlov = [
        ("Erkak", "Erkak"),

        ("Ayol", "Ayol")
    ]
    ism = models.CharField(max_length=30)
    kitob_soni = models.PositiveIntegerField()
    jins = models.CharField(max_length=30, choices=tanlov)
    Tirik = models.BooleanField()
    tugulgan_yil = models.DateField()
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.ism
# Create your models here.
