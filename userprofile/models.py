from __future__ import unicode_literals

import hashlib
import os.path
import urllib

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from activities.models import Activity, Notification

GENDER = (
        ('Male', 'Male'),
        ('Female','Female'),
    )


python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10,choices= GENDER, null=True, blank= True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    likes = models.IntegerField(default = 0)


    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
    	return "user:{}".format(self.user)

    def get_picture(self):
        picture=User.objects.all()
        no_picture = 'http://trybootcamp.vitorfs.com/static/img/user.png'
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' +\
                self.user.username + '.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' +\
                self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                gravatar_url = 'http://www.gravatar.com/avatar/{0}?{1}'.format(
                    hashlib.md5(self.user.email.lower()).hexdigest(),
                    urllib.urlencode({'d': no_picture, 's': '256'})
                    )
                return gravatar_url

        except Exception:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username

    def notify_liked(self, profile):
        if self.user != profile.user:
            Notification(notification_type=Notification.LIKED,
                         from_user=self.user, to_user=profile.user,
                         ).save()

    def unotify_liked(self, profile):
        if self.user != profile.user:
            Notification.objects.filter(
                notification_type=Notification.LIKED,
                from_user=self.user,
                to_user=profile.user,
                ).delete()

    def calculate_likes(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                            profile=self.pk).count()
        self.likes = likes
        self.save()
        return self.likes

    def get_likers(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                            profile=self.pk)
        likers = []
        for like in likes:
            likers.append(like.user)
        return likers

    def notify_favorited(self, apartment):
        if self.user != apartment.user:
            Notification(notification_type=Notification.FAVORITED,
                         from_user=self.user, to_user=apartment.user,
                         apartment=apartment).save()

    def unotify_favorited(self, apartment):
        if self.user != apartment.user:
            Notification.objects.filter(notification_type=Notification.FAVORITED,
                                        from_user=self.user, to_user=apartment.user,
                                        apartment=apartment).delete()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
