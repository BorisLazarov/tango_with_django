from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    account_number = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    balance = models.FloatField()

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Message(models.Model):
    author = models.ForeignKey(UserProfile)
    text = models.CharField(max_length=144)




