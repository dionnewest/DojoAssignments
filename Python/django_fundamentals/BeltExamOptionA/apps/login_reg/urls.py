#OPTION A

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^main$', views.index),
	url(r'^logout$', views.logout),
	url(r'^$', views.index2),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^success$', views.success),
	url(r'^add_friend/(?P<friend_id>\d+)/(?P<user_id>\d+)$', views.add_friend),
	url(r'^remove_friend/(?P<friend_id>\d+)/(?P<user_id>\d+)$', views.remove_friend)
]
	# url(r'^users', views.users)
