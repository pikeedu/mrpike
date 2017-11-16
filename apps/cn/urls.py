from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$', views.aboutus),
    url(r'^service$', views.service),
    url(r'^service/i20$', views.service_i20),
    url(r'^tour$', views.tour),
    url(r'^tour/eslla$', views.esltour),
    url(r'^bootcamp$', views.bootcamp),
    url(r'^bootcamp/art$', views.bootcamp_art),
    url(r'^bootcamp/game$', views.bootcamp_game),
    url(r'^bootcamp/film$', views.bootcamp_film),
    url(r'^bootcamp/makeup$', views.bootcamp_makeup),
    url(r'^bootcamp/animation$', views.bootcamp_animation),
    url(r'^bootcamp/usc$', views.bootcamp_usc),
    url(r'^bootcamp/ucberkeley$', views.bootcamp_ucberkeley),
    url(r'^bootcamp/pepperdine$', views.bootcamp_pepperdine),
    url(r'^contact$', views.contact),
    url(r'^us$', views.us),
    url(r'^[a-zA-Z0-9_.-]*$',views.error),

]
