from django.db import models
from django.utils import timezone

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class Client(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=15,blank = True)
    lastName = models.CharField(max_length=15,blank = True)
    nip = models.CharField(max_length=10,blank = True)
    balance = models.DecimalField(max_digits=15,decimal_places = 2,blank = True, null = True)
    coopDate = models.DateField(blank = True, null=True, default=timezone.now)
    phoneNumber = models.CharField(max_length=12,blank=True)


class Order(models.Model):
    def __str__(self):
        return self.subject
    client = models.ForeignKey('Client',on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=13,decimal_places = 2)
    startDate = models.DateField(default = timezone.now, blank = True)
    returnDate = models.DateField(blank=True, null = True)
    subject = models.CharField(max_length = 100, default = "")
    description = models.TextField(max_length = 400, blank = True)
    #class Statuses(models.TextChoices):
    #    IN_PROGRESS = 1 ,'Przyjete'
    #    OUTSOURCED = 2 , 'outsourcowane'
    #    COMPLICATIONS = 3, 'komplikacje'
    #    DONE = 4 ,'wykonane'
    #    RETURNED = 5,'oddane'
    class Statuses(models.TextChoices):
        IN_PROGRESS = 'Przyjete'
        OUTSOURCED = 'outsourcowane'
        COMPLICATIONS = 'komplikacje'
        DONE = 'wykonane'
        RETURNED = 'oddane'

    status = models.CharField(choices = Statuses.choices,max_length = 15, default = Statuses.IN_PROGRESS)
    comment = models.TextField(max_length = 400, blank=True)


