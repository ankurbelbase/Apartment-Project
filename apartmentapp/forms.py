from django import forms 

from django.utils.encoding import force_text

from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)

from .models import City

from .models import Apartment

class ApartmentForm(forms.ModelForm):

	class Meta:
		model = Apartment
		fields ='__all__'



class TitleSearchFieldMixin(object):
    search_fields = [
        'name__icontains',
        'pk__startswith'
    ]


class TitleModelSelect2Widget(TitleSearchFieldMixin, ModelSelect2Widget):
    queryset=City.objects.all()

class TitleModelSelect2MultipleWidget(TitleSearchFieldMixin, ModelSelect2MultipleWidget):
    pass



class CityForm(forms.ModelForm):
	class Meta:
		model = City

		fields = ('name',)

		widgets = {
		'name':TitleModelSelect2Widget,
		'attrs':{'name':'q',
		'type':'text',
		'class':'form-control input-lg'}
		}