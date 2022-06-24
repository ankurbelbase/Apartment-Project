from django.shortcuts import render
from apartmentapp.models import Apartment 
from userprofile.models import Profile 

from .filters import ApartmentFilter,ProfileFilter 


# Create your views here.
def apartfilter(request):
	apartment_list = Apartment.objects.all()
	apartment_filter = ApartmentFilter(request.GET, queryset=apartment_list)
	return render(request, 'apartmentapp_filter.html',{'filter':apartment_filter})

def profilefilter(request):
	profile_list = Profile.objects.all()
	profile_filter = ProfileFilter(request.GET,queryset=profile_list)
	return render(request,'profile_filter.html',{'filter':profile_filter})
