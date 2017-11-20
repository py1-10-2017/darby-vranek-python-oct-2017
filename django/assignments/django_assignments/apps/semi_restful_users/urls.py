from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^new/$', views.new_user),
	url(r'^create/$', views.create_user),
	url(r'^update/$', views.update),
	url(r'^([0-9]+)/edit/$', views.edit_user),
	url(r'^([0-9]+)/$', views.show_user),
	url(r'^([0-9]+)/destroy/$', views.destroy_user)
]
