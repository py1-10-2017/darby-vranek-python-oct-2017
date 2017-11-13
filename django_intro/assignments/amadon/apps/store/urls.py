from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^buy/([0-9]+)/$', views.buy),
	url(r'^checkout/$', views.checkout)
]
