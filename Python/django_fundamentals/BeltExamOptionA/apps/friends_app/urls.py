#OPTION A

from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.index),
	url(r'^/(?P<user_id>\d+)$', views.user)
]

