from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Profile model to extend the built-in User model with additional attributes.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the Django User model.
        is_buyer (BooleanField): A flag indicating whether the user is a buyer. Defaults to True.
        is_admin (BooleanField): A flag indicating whether the user is an admin. Defaults to False.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_buyer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a Profile instance whenever a new User instance is created.
        sender (Model class): The model class that sent the signal (User in this case).
        instance (User): The actual instance of the model being saved.
        created (bool): A boolean indicating if a new record was created.
        **kwargs: Additional keyword arguments.
    Side Effects:
        Creates a corresponding Profile instance for every new User instance.
    """
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()