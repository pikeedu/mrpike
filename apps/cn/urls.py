from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$', views.aboutus),
    url(r'^service$', views.service),
    url(r'^service/i20$', views.service_i20),
    url(r'^tour$', views.tour),
    url(r'^tour/esl$', views.esl),
    url(r'^tour/eslla$', views.esltour),
    url(r'^tour/esltwoweeks$', views.esltwoweeks),
    url(r'^tour/golfandwine$', views.golfandwine),
    url(r'^bootcamp$', views.bootcamp),
    url(r'^bootcamp/film1$', views.bootcamp_film1),
    url(r'^bootcamp/film2$', views.bootcamp_film2),
    url(r'^bootcamp/film$', views.bootcamp_film),
    url(r'^bootcamp/makeup$', views.bootcamp_makeup),
    url(r'^bootcamp/cinemamakeup$', views.bootcamp_cinemamakeup),
    url(r'^bootcamp/usc$', views.bootcamp_usc),
    url(r'^bootcamp/ucberkeley$', views.bootcamp_ucberkeley),
    url(r'^bootcamp/pepperdine$', views.bootcamp_pepperdine),
    url(r'^contact$', views.contact),
    url(r'^us$', views.us),
    url(r'^[a-zA-Z0-9_.-]*$',views.error),

]
