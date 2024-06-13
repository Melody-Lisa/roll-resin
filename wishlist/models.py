from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Wishlist(models.Model):
    """
    A model for a users wishlist
    """
    class Meta:
        verbose_name_plural = 'Wishlist'

    products = models.ManyToManyField(
        Product,
        blank=True
    )
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Return object string
        """
        return f"{self.username}'s Wishlist"
