from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a Profile instance whenever a new User instance is created.

    Args:
        sender (Model class): The model class that sent the signal (User in this case).
        instance (User): The actual instance of the model being saved.
        created (bool): A boolean indicating if a new record was created.
        **kwargs: Additional keyword arguments.

    Side Effects:
        Creates a corresponding Profile instance for every new User instance.
    """
    if created and not hasattr(instance, 'profile'):
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to save the Profile instance whenever the User instance is saved.

    Args:
        sender (Model class): The model class that sent the signal (User in this case).
        instance (User): The actual instance of the model being saved.
        **kwargs: Additional keyword arguments.

    Side Effects:
        Saves the corresponding Profile instance whenever the User instance is saved.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()