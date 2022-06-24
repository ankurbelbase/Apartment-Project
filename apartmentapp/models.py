from __future__ import unicode_literals
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from django.db import models
from activities.models import Activity


class City(models.Model):
    name = models.CharField(max_length = 80)

    def __str__(self):
        return self.name



class Apartment(models.Model):
    TYPE = (
        ('House', 'House'),
        ('Apartment','Apartment'),
    )
    BATHROOM =(
        ('Shared','Shared'),
        ('Private','Private'),

    )
    WATER_SUPPLY=(
        ('Limited','Limited'),
        ('24hrs Supply','24hrs Supply')
    )
    FURNISHED=(
        ('Well-Furnished','Well-Furnished'),
        ('Semi-Furnished','Semi-Furnished'),
        ('None','None'),
    )
    MINIMUM_STAY=(
        ('3 Months','3 Months'),
        ('6 Months','6 Months'),
        ('12 Months','12 Months'),
        ('More','More'),
    )
    UTILITIES_COST=(
        ('Included','Included'),
        ('Excluded','Excluded'),
    )
    MAX_OCCUPENCY=(
        ('Two','2'),
        ('Three','3'),
        ('Four','4'),
        ('Five','5'),
    )
    KITCHEN=(
        ('Private','Private'),
        ('Shared','Shared'),
    )
    user = models.ForeignKey(User, blank = True, null = True)
    city = models.ForeignKey(City, blank = True, null = True)
    apartment_type = models.CharField(max_length=100, choices = TYPE)
    location=models.CharField(max_length=100)
    description=models.TextField()
    internet=models.BooleanField(default=False)
    area=models.CharField(max_length=100)
    bedroom=models.PositiveIntegerField()
    bathroom=models.CharField(max_length=100, choices = BATHROOM) 
    water_supply=models.CharField(max_length=100, choices = WATER_SUPPLY)
    furnished=models.CharField(max_length=100, choices = FURNISHED)
    mininun_stay=models.CharField(max_length=100, choices = MINIMUM_STAY)
    utilities_cost=models.CharField(max_length=100, choices = UTILITIES_COST)
    parking=models.BooleanField(default=False)
    rent=models.PositiveIntegerField()
    max_occupency=models.CharField(max_length=100, choices = MAX_OCCUPENCY)
    apartment_avaibility=models.BooleanField(default=False)
    kitchen=models.CharField(max_length=100, choices = KITCHEN)
    favorites = models.PositiveIntegerField(default=0, null=True, blank= True)

    def __str__(self):
        return 'Apartment Type: {}, Apartment Location : {}'.format(self.apartment_type,self.location)

    def calculate_favorites(self):
        favorites = Activity.objects.filter(activity_type=Activity.FAVORITE, apartment=self.pk).count()
        self.favorites = favorites
        self.save()
        return self.favorites

    def get_favoriters(self):
        favorites = Activity.objects.filter(activity_type=Activity.FAVORITE,
                                            apartment=self.pk)
        favoriters = []
        for favorite in favorites:
            favoriters.append(favorite.user)
        return favoriters



class ApartmentImage(models.Model):
    
    apartment = models.ForeignKey(Apartment)
    apartment_image=ResizedImageField(size= [500, 300], crop = ['top', 'left'], upload_to='media/apartment_image', null=True)
    