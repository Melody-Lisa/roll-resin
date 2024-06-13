from django.http import Http404
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from products.models import Product
from util.util import setup_pagination
from .models import Favourites


@login_required
def view_product_favourites(request):
    """
    A view that displays users wishlist
    """
    wishlist_items_count = 0
    try:
        all_wishlist = Wishlist.objects.filter(username=request.user.id)[0]
    except IndexError:
        wishlist_items = None
    else:
        wishlist_items = all_wishlist.products.all()
        wishlist_items_count = all_wishlist.products.all().count()
        wishlist_items = setup_pagination(wishlist_items, request, 4)

    if not wishlist_items:
        messages.info(request, 'Your wishlist is empty!')

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
        'wishlist_items_count': wishlist_items_count
    }
    return render(request, template, context)


@login_required
def add_product_to_wishlist(request, item_id):
    """
    Add a product item to wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
    except Http404:
        wishlist = wishlist.objects.create(username=request.user)
    if product in Wishlist.products.all():
        messages.info(request, 'The product is '
                               'already in your wishlist!')
    else:
        wishlist.products.add(product)
        messages.info(request, 'Added the product to your wishlist')
    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_product_from_wishlist(request, item_id, redirect_from):
    """
    Remove a product item from wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    wishlist = get_object_or_404(Wishlist, username=request.user.id)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.info(request, 'Removed the product '
                               'from your wishlist.')
    else:
        messages.error(request, 'That product is '
                                'not in your wishlist!')
    if redirect_from == 'wishlist':
        redirect_url = reverse('view_product_wishlist')
    else:
        redirect_url = reverse('product_detail', args=[item_id])
    return redirect(redirect_url)