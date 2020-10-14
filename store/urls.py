from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='store-dashboard'),
    path('orders/', views.orders, name='store-orders'),
]
