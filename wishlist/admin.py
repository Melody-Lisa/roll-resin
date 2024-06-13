from django.contrib import admin

from .models import Favourites


class WishlistAdmin(admin.ModelAdmin):
    """
    Admin class for the wishlist model.
    """
    list_display = (
        'username',
    )
    search_fields = (
        'username',
    )
    list_filter = (
        'username',
    )
    list_per_page = 20


admin.site.register(Wishlist, WishlistAdmin)
