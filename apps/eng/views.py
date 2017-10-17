from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'eng/index.html')

def aboutus(request):
    return render(request, 'eng/aboutus.html')

def service(request):
    return render(request, 'eng/service/service.html')

def tour(request):
    return render(request, 'eng/tour/tour.html')
