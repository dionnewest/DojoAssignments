from django.conf.urls import url
from . import views

#urls for BLOG app

urlpatterns = [
	url(r'^$', views.index)
]