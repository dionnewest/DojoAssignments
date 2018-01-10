from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.details),
    url(r'^add$', views.addBook),
    url(r'^create$', views.createBook),
    # url(r'^(?P<id>\d+)$', views.show),
]
