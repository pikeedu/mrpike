from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cn/index/indexcn.html')

def aboutus(request):
    return render(request, 'cn/aboutus/aboutuscn.html')

def service(request):
    return render(request, 'cn/service/servicecn.html')

def tour(request):
    return render(request, 'cn/tour/tourcn.html')

def bootcamp(request):
    return render(request, 'cn/bootcamp/bootcampcn.html')

def contact(request):
    return render(request, 'cn/contact/contactcn.html')

def error(request):
    return render(request, 'cn/error/errorcn.html')
