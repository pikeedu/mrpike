from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$', views.aboutus),
    url(r'^service$', views.service),
    url(r'^service/i20$', views.servicei20),
    url(r'^tour$', views.tour),
    url(r'^tour/eslla$', views.esltour),
    url(r'^bootcamp$', views.bootcamp),
    url(r'^contact$', views.contact),
    url(r'^us$', views.us),
    url(r'^[a-zA-Z0-9_.-]*$',views.error),

]
