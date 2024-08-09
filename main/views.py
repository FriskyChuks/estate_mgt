from django.shortcuts import render


def home(request):

    return render(request, 'main/index.html', {})


def about_us_view(request):

    return render(request, 'main/about_us.html', {})


def contact_us_view(request):

    return render(request, 'main/contact_us.html', {})
