from django.conf.urls import url
from . import views

#urls for SURVEYS app

urlpatterns = [
	url(r'^', views.index)
]