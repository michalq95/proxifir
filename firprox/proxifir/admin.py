from django.contrib import admin
from .models import Client, Order

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nazwa',{'fields':['name']}),
        ('Imie',{'fields':['firstName']}),
        ('Nazwisko',{'fields':['lastName']}),
        ('NIP',{'fields':['nip']}),
        ('rachunek',{'fields':['balance']}),
        ('Poczatek Wspolpracy',{'fields':['coopDate']}),
    ]
    list_display = ('name', 'firstName', 'lastName','nip','balance','coopDate')
    list_filter = ['coopDate']
    search_fields = ['name', 'firstName', 'lastName','nip']


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('client',{'fields':['client']}),
        ('price',{'fields':['price']}),
        ('subject',{'fields':['subject']}),
        ('description',{'fields':['description']}),
        ('startDate',{'fields':['startDate']}),
        ('returnDate',{'fields':['returnDate']}),
        ('comment',{'fields':['comment']}),
        ('status',{'fields':['status']}),

    ]
    list_display = ('client', 'price', 'subject','description','startDate','returnDate','comment','status')
    list_filter = ['startDate','returnDate']
    search_fields = ['client', 'price', 'subject','description','status']


admin.site.register(Client,ClientAdmin)
    
admin.site.register(Order,OrderAdmin)
