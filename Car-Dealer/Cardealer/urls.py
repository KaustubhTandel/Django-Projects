"""
URL configuration for Cardealer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Garage import views
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Personals_Informations',views.p_d,name="F1"),
    path('Car_Collections',views.c_c,name="F2"),
    path('Payment',views.p_t,name="F3"),
    path('Thank You',views.t_y,name="TY"),
    path('',include('Garage.urls'))

]
