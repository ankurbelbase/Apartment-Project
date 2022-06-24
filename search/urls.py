from django.conf.urls import url


from .views import search, city

urlpatterns = [
url(r'^$', search, name='search'),
url(r'^city/$', city, name='city'),
]