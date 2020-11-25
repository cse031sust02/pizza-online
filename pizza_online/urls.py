from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from web import views as web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', web_views.register, name='web-register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='web-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='web-logout'),
    path('', include('web.urls')),
]
