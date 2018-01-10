from django.conf.urls import url
from . import views

#urls for USERS app

urlpatterns = [
	url(r'^$', views.index)
]