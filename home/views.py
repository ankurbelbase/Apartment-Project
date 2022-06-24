from django.shortcuts import render
from django.views.generic.list import ListView
from apartmentapp.models import Apartment

from django.http import HttpResponse
from django.views import generic

class TemplateFormView(generic.FormView):
	template_name = 'index.html'

class ApartmentListView(ListView):
	model=Apartment
	template_name='apartment_browse.html'
	def get_context_data(self, **kwargs): 
		context = super(ApartmentListView, self).get_context_data(**kwargs)
		return context
       