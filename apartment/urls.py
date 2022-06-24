"""apartment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from activities import views as activities_views
from userprofile import views as userprofile_views


urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^apartment/', include('apartmentapp.urls', namespace='apartmentapp')),    
    url(r'^userprofile/', include('userprofile.urls', namespace='userprofile')),    
    url(r'^filter/', include('filter.urls', namespace = 'filter')), 
    url(r'^account/', include('authentication.urls', namespace='authentication')),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^messages/', include('messenger.urls')),
    

    # urls for notification
    url(r'^notifications/$', activities_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications,
        name='check_notifications'),
    url(r'^(?P<username>[^/]+)/$', userprofile_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)