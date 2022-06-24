from django.shortcuts import render, redirect
from apartmentapp.forms import ApartmentForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import generic
from django.http import HttpResponse
from .models import Apartment, ApartmentImage
from PIL import Image

from easy_thumbnails.files import get_thumbnailer
from activities.models import Activity
from apartment.decorators import ajax_required


#for apartment detail page
class ApartmentDetailView(DetailView):
	model=Apartment
	template_name='apartment/apartment_detail.html'

	# def get(self, request, *args, **kwargs):
 #            name = request.GET.get('location')
 #            print name 
 #            return self.render_to_response(name)

	def get_context_data(self, **kwargs):
		context=super(ApartmentDetailView,self).get_context_data(**kwargs)
		# pk = self.kwargs.get(self.pk_url_kwarg)
		# obj = Apartment.objects.get(pk=pk)
		
		# context['recommemded'] = Apartment.objects.filter(location__contains=obj)
  #       # context['recommemded'] = Apartment.objects.filter(string__contains='pattern')
		# print context['recommemded']
		return context



@login_required
@ajax_required
def apartmentLike(request):
    apartment_id = request.POST['apartment']
    apartment = Apartment.objects.get(pk=apartment_id)

    user = request.user
    activity = Activity.objects.filter(activity_type=Activity.FAVORITE,
                                       user=user, apartment=apartment_id)
    if activity:
        activity.delete()
        user.profile.unotify_favorited(apartment)
    else:
        activity = Activity(activity_type=Activity.FAVORITE, user=user,
                            apartment=apartment_id)
        activity.save()
        user.profile.notify_favorited(apartment)

    return HttpResponse(apartment.calculate_favorites())


def testing(request):
    name = request.GET.get('location')
    print name
    return render(request, 'apartment/apartment_detail.html')
