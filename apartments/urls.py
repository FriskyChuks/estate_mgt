from django.urls import path
from .views import *


urlpatterns = [
    path('create_apartment/', create_apartment_view, name='create_apartment'),
    path('apartment_list/', apartment_list_view, name='apartment_list'),
    path('assign_apartment/<int:id>/',
         assign_apartment_view, name='assign_apartment'),
    path('apartment_detail/<int:id>/',
         apartment_detail_view, name='apartment_detail'),
]
