from django.conf import settings
from django.conf.urls import url
from userprofile import views

urlpatterns = [
	url(r'^settings/$',views.settings, name= 'profilesettings'),
	url(r'^password-change/$',views.password, name= 'password'),
	 url(r'^settings/picture/$', views.picture, name='picture'),
    url(r'^settings/upload_picture/$', views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^like/$', views.profileLike, name='like'),
    url(r'^list/$', views.network, name='network'),
    
]