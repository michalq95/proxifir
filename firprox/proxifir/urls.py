from django.urls import path
from . import views
app_name = 'proxifir'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('index',views.IndexView.as_view(),name='index'),
    path('clients',views.ClientsView.as_view(),name='clients'),
    path('clients/<int:pk>',views.ClientView.as_view(),name='client'),
    path('order<int:pk>',views.OrderView.as_view(),name='order'),
    path('order/create',views.OrderCreate.as_view(),name='ordercreate'),
    path('order<int:pk>/update',views.OrderUpdate.as_view(), name='orderupdate'),
    path('order<int:pk>/delete',views.OrderDelete.as_view(),name='orderdelete')

]