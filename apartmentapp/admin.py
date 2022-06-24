from django.contrib import admin
from .models import Apartment, ApartmentImage, City

# Register your models here.
class ApartmentImageInline(admin.StackedInline):
    model = ApartmentImage
    extra = 2

class ApartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Apartment',{'fields': ['user', 'city', 'apartment_type',]}),
        ('Basic information', {'fields': ['location','description',], 'classes': ['collapse']}),
        ('Services', {'fields':['internet','bedroom','bathroom','water_supply','furnished',
        	'parking','kitchen',], 'classes': ['collapse']}),
        ('Extra Information', {'fields':['area','rent', 'mininun_stay', 'max_occupency', 'utilities_cost', 
        	'apartment_avaibility' ,'favorites'], 'classes': ['collapse']})
    ]
    inlines = [ ApartmentImageInline ]

admin.site.register(Apartment,ApartmentAdmin),


admin.site.register(City)