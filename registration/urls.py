"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('procesar_seleccion/', views.procesar_seleccion, name='procesar_seleccion'),
    path('actividad1/', views.actividad1, name='actividad1'),
    path('actividad2/', views.actividad2, name='actividad2'),
    path('actividad3/', views.actividad3, name='actividad3'),
    path('actividad4/', views.actividad4, name='actividad4'),
    path('actividad5/', views.actividad5, name='actividad5'),
    path('actividad6/', views.actividad6, name='actividad6'),
    path('actividad7/', views.actividad7, name='actividad7'),
    path('actividad8/', views.actividad8, name='actividad8'),
    path('actividad9/', views.actividad9, name='actividad9'),
    path('vistaactividad1/', views.vistaactividad1, name='vistaactividad1'),
    path('vistaactividad3/', views.vistaactividad3, name='vistaactividad3'),
    path('vistaactividad6/', views.vistaactividad6, name='vistaactividad6'),
    path('vistaactividad7/', views.vistaactividad7, name='vistaactividad7'),
    path('admin/', admin.site.urls),
]
