from django.conf.urls import url 
from .views import apartfilter,profilefilter

urlpatterns = [
	url(r'^apfilter/$', apartfilter, name='apfilter'),
	url(r'^prfilter/$', profilefilter, name='prfilter'),
	]