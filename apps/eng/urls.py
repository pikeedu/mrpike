from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^cn$', views.cn),
    url(r'^aboutus$', views.aboutus),
    url(r'^service$', views.service),
    url(r'^tour$',views.tour),
    url(r'^bootcamp$',views.bootcamp),
    url(r'^contact$',views.contact),
    # url(r'^[a-zA-Z0-9_.-]*$',views.error)
]
