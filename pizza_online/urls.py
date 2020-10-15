from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from store_managers import views as store_manage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', store_manage_views.register, name='manager-register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='manager-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='manager-logout'),
    path('store/', include('store.urls')),
]
