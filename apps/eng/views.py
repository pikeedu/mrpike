from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    # response = "hello, mr.pike"
    # return HttpResponse(response)
    return render(request, 'eng/index.html')

def aboutus(request):
    return render(request, 'eng/aboutus.html')
