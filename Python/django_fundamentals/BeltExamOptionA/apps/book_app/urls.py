from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^add$', views.add),
	url(r'^book_profile$', views.book_profile)
]