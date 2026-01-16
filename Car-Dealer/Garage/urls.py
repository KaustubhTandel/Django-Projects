
from django.urls import path
from . import views

urlpatterns = [
    # path('Personals_Informations',views.index,name='F1'),
    # path('Car_Collections',views.index,name='F2'),
    # path('Payment',views.index,name='F3'),
    # path('Thank You',views.index,name='TY'),
    path('',views.index,name='index'),

]
