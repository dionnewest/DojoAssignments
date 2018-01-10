from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	# url(r'^/destination/(?P<trip_id>\d+)$', views.destination),
	# url(r'^/add$', views.add_page),
	# url(r'^/add_trip$', views.add),
	# url(r'^/join/(?P<trip_id>\d+)$', views.join),
	# url(r'^/remove/(?P<trip_id>\d+)$', views.remove)
]