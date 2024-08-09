from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .models import *

from apartments.quick_stats import *


def create_apartment_view(request):
    context = {}

    apartment_category = request.POST.get('apartment_category')
    apartment_type = request.POST.get('apartment_type')
    phase = request.POST.get('phase')
    street = request.POST.get('street')
    compound = request.POST.get('compound')
    flat_number = request.POST.get('flat_number')
    if request.method == 'POST':
        print('OK')
        obj = Apartment.objects.create(apartment_category=apartment_category,
                                       phase=phase, apartment_type_id=apartment_type, street_id=street,
                                       compound=compound, flat_number=flat_number,
                                       created_by_id=request.user.id)
        obj.save()
        messages.success(request, 'Apartment created sucessfully!')
        return redirect('apartment_list')
    return render(request, 'apartments/create_apartment.html', context)


def apartment_list_view(request):
    apartments = Apartment.objects.all()
    residential_apartments = Apartment.objects.filter(
        apartment_category='residential')
    business_apartments = Apartment.objects.filter(
        apartment_category='business')
    available = Apartment.objects.filter(status='free')
    taken = Apartment.objects.filter(status='taken')
    types = ApartmentType.objects.all()
    streets = Street.objects.all()

    context = {'apartments': apartments, "residential_apartments": residential_apartments,
               "business_apartments": business_apartments, "available": available, "taken": taken,
               "types": types, "streets": streets}
    return render(request, 'apartments/apartment_list.html', context)


def assign_apartment_view(request, id):
    apartment = Apartment.objects.get(id=id)
    user = None
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            obj = Occupant.objects.create(occupant_id=user.id, apartment_id=id)
            obj.save()
            Apartment.objects.filter(id=id).update(status='taken')
            messages.success(
                request, f"Apartment successfully assigned to {email}")
            return redirect('apartment_list')
        except ObjectDoesNotExist:
            messages.error(
                request, f'"{email}" is not assigned to a user. You cannot assign an apartment to a non existing user')
            return redirect("apartment_list")
    print(user)
    context = {"apartment": apartment}
    return render(request, 'apartments/assign_apartment.html', context)


def apartment_detail_view(request, id):
    apartment = Apartment.objects.get(id=id)
    context = {'apartment': apartment}
    return render(request, 'apartments/apartment_detail.html', context)
