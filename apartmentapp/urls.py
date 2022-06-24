from django.conf.urls import url
from .views import ApartmentDetailView, apartmentLike
from django.contrib.auth import views as auth_views
from .forms import CityForm



urlpatterns = [	
	
	url(r'^apartment-detail/(?P<pk>\d+)$', ApartmentDetailView.as_view(), name='apartment_detail'),
	url(r'^apartment-detail/like/$', apartmentLike, name='like'),
]
