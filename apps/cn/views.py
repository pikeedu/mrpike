from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cn/index.html')

def aboutus(request):
    return render(request, 'cn/aboutus.html')
