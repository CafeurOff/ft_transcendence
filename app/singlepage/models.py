from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile-picture', default='default_profile_picture.png', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    win = models.IntegerField(default=0, blank=True)
    lose = models.IntegerField(default=0, blank=True)   

    def __str__(self):
        return self.usernames

@receiver(post_save, sender='singlepage.User')
def assign_default_image(sender, instance, created, **kwargs):
    if created and not instance.profile_image:
        instance.profile_image = 'default_profile_picture.png'
        instance.save()

class Game(models.Model):
    local = models.BooleanField(default=False)
    tournament = models.BooleanField(default=False)
    ended = models.BooleanField(default=False)
    winner_uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Friend(models.Model):
    user1_uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2_uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    created_at = models.DateTimeField(auto_now_add=True)
