import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest
from apartment.decorators import ajax_required
from apartmentapp.models import Apartment, City
from .filters import ApartmentFilter

def search(request):
    temp = request.GET.get('name')
    similar = Apartment.objects.filter(city__name__icontains=temp)
    print similar
    
    if 'name' in request.GET:
        querystring = request.GET.get('name').strip()
        
        if querystring == None:
            return redirect('/home/')

        try:
            search_type = request.GET.get('type')
            if search_type not in ['city', 'users']:
                search_type = 'city'

        except Exception:
            search_type = 'city'
        results = {}
        
        
        results['city'] = Apartment.objects.filter(
             Q(city__name__iexact=querystring))
        return render(request, 'search/listing.html', {
            'hide_search': True,
            'querystring': querystring,
            'active': search_type,
            'results': results[search_type],
            
        })
    else:

        return render(request, 'search/listing.html', {'hide_search': True, 'filter':apartment_filter})

        return render(request, 'index.html', {'hide_search': True})


@ajax_required
def city(request):
    city = City.objects.all()
    dump = []
    template = '{0}'
    for city in city:
        if city is not None:
            dump.append(template.format(city.name))
        else:
            dump.append(city.name)
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')
