# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Pokemon Card(models.Model):

    #__Pokemon Card_FIELDS__
    price = models.IntegerField(null=True, blank=True)
    market_value = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    set = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    date_purchased = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Pokemon Card_FIELDS__END

    class Meta:
        verbose_name        = _("Pokemon Card")
        verbose_name_plural = _("Pokemon Card")



#__MODELS__END
