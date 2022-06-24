
from django.conf.urls import url
from .views import TemplateFormView
from apartmentapp.forms import CityForm
from .views import ApartmentListView

urlpatterns = [
	url(r'^$',
        TemplateFormView.as_view(form_class=CityForm),
        name='home'),
	 url(r'^apartment-browse/$', ApartmentListView.as_view(), name='apartment-browse')
]