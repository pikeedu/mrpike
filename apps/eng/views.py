from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'eng/index/index.html')

# def cn(request):
#     return render (request, './../cn/templates/cn/index.html')

def aboutus(request):
    return render(request, 'eng/aboutus/aboutus.html')

def service(request):
    return render(request, 'eng/service/service.html')

def tour(request):
    return render(request, 'eng/tour/tour.html')

def bootcamp(request):
    return render(request, 'eng/bootcamp/bootcamp.html')


def contact(request):
    return render(request, 'eng/contact/contact.html')

# def error(request):
#     return render(request, 'eng/error/error.html')
