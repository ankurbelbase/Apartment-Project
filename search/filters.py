from apartmentapp.models import Apartment 
from userprofile.models import Profile 

import django_filters


class ApartmentFilter(django_filters.FilterSet):
	rent = django_filters.NumberFilter(name='rent',lookup_expr='lt')

	class Meta:
		model = Apartment 
		fields = ['apartment_type','location','internet','area','mininun_stay','max_occupency',]


class ProfileFilter(django_filters.FilterSet):

	class Meta:
		model = Profile 
		fields = ['location','age','job_title',]
