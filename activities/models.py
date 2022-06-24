from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape


@python_2_unicode_compatible
class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        )

    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.IntegerField(null=True, blank=True)
    apartment = models.IntegerField(null=True, blank=True)
   

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.activity_type


@python_2_unicode_compatible
class Notification(models.Model):
    LIKED = 'L'
    FAVORITED = 'F'
    
    
    
    
    NOTIFICATION_TYPES = (
        (LIKED, 'Liked'),
        
        (FAVORITED, 'Favorited'),
        
        )

    _LIKED_TEMPLATE = '<a href="/{0}/">{1}</a> liked your profile:'  # noqa: E501
    
    _FAVORITED_TEMPLATE = '<a href="/{0}/">{1}</a> favorited this <a href="/apartment/apartment-detail/{2}">apartment.</a>' 
    

    from_user = models.ForeignKey(User, related_name='+')
    to_user = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField(auto_now_add=True)
    profile = models.OneToOneField('userprofile.Profile', null=True, blank=True)
    apartment = models.ForeignKey('apartmentapp.Apartment', null=True, blank=True)
    notification_type = models.CharField(max_length=1,
                                         choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __str__(self):
        if self.notification_type == self.LIKED:
            return self._LIKED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                
                )
        
        elif self.notification_type == self.FAVORITED:
            return self._FAVORITED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.apartment.pk,
                )
        
        else:
            return 'Ooops! Something went wrong.'