from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Client, Order
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = 'proxifir/index.html'
    context_object_name = 'orderList'
    paginate_by = 30
    
    #def get_queryset(self):
    #    return Order.objects.order_by('-id')

    def get_queryset(self):
        filterclient_val = self.request.GET.get('filterclient', '')
        filtersubject_val = self.request.GET.get('filtersubject', '')
        filterstatus_val = self.request.GET.get('filterstatus', '')
        new_context = Order.objects.filter(
            client__name__contains=filterclient_val,subject__contains = filtersubject_val, status__contains = filterstatus_val)
        return new_context
#
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['filterclient'] = self.request.GET.get('filterclient', '')
        context['filtersubject'] = self.request.GET.get('filtersubject', '')
        context['filterstatus'] = self.request.GET.get('filterstatus', '')
        return context



class ClientsView(generic.ListView):
    template_name = 'proxifir/clients.html'
    context_object_name = 'clientsList'
    paginate_by = 30
    
    def get_queryset(self):
        return Client.objects.order_by('-coopDate')#[:2]

class OrderView(generic.DetailView):
    model = Order
    template_name = 'proxifir/order.html'

class ClientView(generic.DetailView):
    model = Client
    template_name = 'proxifir/client.html'

class OrderCreate(CreateView):
    model = Order
    fields = ['client','price','startDate','returnDate','subject','description','status','comment']
    def get_success_url(self):
        return reverse('proxifir:index')

class OrderUpdate(UpdateView):
    model = Order
    fields = ['client','price','startDate','returnDate','subject','description','status','comment']
    def get_success_url(self):
        return reverse('proxifir:index')


class OrderDelete(DeleteView):
    model = Order
    def get_success_url(self):
        return reverse('proxifir:index')
