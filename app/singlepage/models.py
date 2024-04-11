from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile-picture', default='default_profile_picture.png', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    total_matches = models.IntegerField(default=0, blank=True)
    win = models.IntegerField(default=0, blank=True)
    lose = models.IntegerField(default=0, blank=True)   


    def __str__(self):
        return self.usernames

@receiver(post_save, sender='singlepage.User')
def assign_default_image(sender, instance, created, **kwargs):
    if created and not instance.profile_image:
        instance.profile_image = 'default_profile_picture.png'
        instance.save()
        
@receiver(pre_save, sender=User)
def delete_old_profile_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = User.objects.get(pk=instance.pk)
            if old_instance.profile_image != instance.profile_image:
                if old_instance.profile_image:
                    old_image_path = old_instance.profile_image.path
                    default_image_path = default_storage.path(instance.profile_image.field.default)
                    if default_storage.exists(old_image_path) and old_image_path != default_image_path:
                        default_storage.delete(old_image_path)
        except User.DoesNotExist:
            pass

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
