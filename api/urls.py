from django.urls import path, include
from .views import *

urlpatterns = [

    path('weapons/', Weapons.as_view(), name='weapons_list'),
    path('weapons/<str:name>',Weapons.as_view(), name='weapon')
    
]