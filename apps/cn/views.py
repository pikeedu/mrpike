from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cn/index/indexcn.html')

def aboutus(request):
    return render(request, 'cn/aboutus/aboutuscn.html')

def service(request):
    return render(request, 'cn/service/servicecn.html')

def service_i20(request):
    return render(request, 'cn/service/i20.html')

def tour(request):
    return render(request, 'cn/tour/tourcn.html')

def bootcamp(request):
    return render(request, 'cn/bootcamp/bootcampcn.html')

def bootcamp_art(request):
    return render(request, 'cn/bootcamp/art.html')

def bootcamp_game(request):
    return render(request, 'cn/bootcamp/game.html')

def bootcamp_film(request):
    return render (request, 'cn/bootcamp/film.html')

def bootcamp_makeup(request):
    return render (request, 'cn/bootcamp/makeup.html')

def bootcamp_animation(request):
    return render (request, 'cn/bootcamp/animation.html')

def bootcamp_usc(request):
    return render (request, 'cn/bootcamp/usc.html')

def bootcamp_ucberkeley(request):
    return render (request, 'cn/bootcamp/ucberkeley.html')

def bootcamp_pepperdine(request):
    return render (request, 'cn/bootcamp/pepperdine.html')

def contact(request):
    return render(request, 'cn/contact/contactcn.html')

def error(request):
    return render(request, 'cn/error/errorcn.html')

def esltour(request):
    return render(request, 'cn/tour/eslla.html')

def us(request):
    return render(request, 'eng/index/index.html')
