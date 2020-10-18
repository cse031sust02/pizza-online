from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='store-dashboard'),
    path('setup/', views.setup, name='store-setup'),
    path('items/', views.items, name='store-items'),
    path('orders/', views.orders, name='store-orders'),
]
