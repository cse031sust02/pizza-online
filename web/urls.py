from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('dashboard/', views.dashboard, name='web-dashboard'),
    path('setup/', views.setup, name='web-setup'),
    path('items/', views.items, name='web-items'),
    path('orders/', views.orders, name='web-orders'),
]
