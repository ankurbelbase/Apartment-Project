from apartmentapp.models import Apartment 
from userprofile.models import Profile 

import django_filters


class ApartmentFilter(django_filters.FilterSet):
	# rent__lt = django_filters.NumberFilter(name='rent', lookup_expr='lt')

	location = django_filters.CharFilter(lookup_expr='icontains')


	# rent = django_filters.RangeFilter(widget='rent',required=False)

	rent = django_filters.NumberFilter(name='rent',lookup_expr='lte')


	class Meta:
		model = Apartment 
		fields = ['apartment_type',]


class ProfileFilter(django_filters.FilterSet):

	class Meta:
		model = Profile 
		fields = ['user','location','age','job_title',]



