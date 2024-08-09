from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about_us/', about_us_view, name='about_us'),
    path('contact_us/', contact_us_view, name='contact_us'),
]
