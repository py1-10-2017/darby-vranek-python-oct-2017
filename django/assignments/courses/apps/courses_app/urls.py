from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_course/$', views.add_course, name='add_course'),
	url(r'^destroy/(?P<id>\d+)/$', views.destroy, name='destroy'),
	url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove')
]
