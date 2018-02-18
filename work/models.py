from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

year_choices = [
        (None, 'Year'),
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
    ]
sex_choices = [
    (None,'Sex'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    number=models.CharField(max_length=10)
    message=models.TextField()

    def __unicode__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    sex = models.CharField(max_length=10, choices=sex_choices, null=True, blank=True)
    year = models.PositiveSmallIntegerField(choices=year_choices, null=True, blank=True)
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile()
        profile.user = instance
        profile.save()
post_save.connect(update_user_profile, sender=User)
# Create your models here.
