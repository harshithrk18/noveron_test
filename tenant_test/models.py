from django.db import models
from django.urls import reverse

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile_1 = models.CharField(max_length=15)
    mobile_2 = models.CharField(max_length=15)
    mobile_3 = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    location = models.TextField()

    # def get_absolute_url(self):
    #     return reverse()

    def __str__(self):
        return self.name



