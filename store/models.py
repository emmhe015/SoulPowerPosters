from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
 

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
    def __str__(self):
        return f'{self.user.username} Profile'
    

