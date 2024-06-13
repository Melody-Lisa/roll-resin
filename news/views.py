from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import NewsForm
from .models import News


def news_items(request):
    """
    A view to show all news items
    """
    news_items_published = \
        News.objects.filter(status=1).order_by('-create_date')
    news_items_drafts = \
        News.objects.filter(status=0).order_by('-create_date')

    news_items_count = News.objects.filter(status=1).count()

    context = {
        'news_items_published': news_items_published,
        'news_items_drafts': news_items_drafts,
        'news_items_count': news_items_count
    }

    return render(request, 'news/news.html', context)


@login_required
def add_news_item(request):
    """
    A view to add a news item
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES)
        if news_form.is_valid():
            form_data = news_form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.success(request, 'Your news item was posted successfully!')
            return redirect('news_items')
        else:
            messages.error(
                request, 'Your news item failed to add, Please try again')
            return redirect('add_news_item')
    else:
        news_form = NewsForm()

    template = 'news/add_news_item.html'
    context = {
        'post_form': news_form,
    }
    return render(request, template, context)


@login_required
def edit_news_item(request, news_item_id):
    """ Edit a news item """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    news_item_to_edit = get_object_or_404(News, pk=news_item_id)
    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES, instance=news_item_to_edit)
        if news_form.is_valid():
            news_form.save()
            messages.success(request, 'Successfully updated news item!')
            return redirect(reverse('news_item', args=[news_item_to_edit.id]))
        else:
            messages.error(request, 'Failed to update news item. Please ensure the form is valid.')
    else:
        news_form = NewsForm(instance=news_item_to_edit)
        messages.info(request, f'You are editing {news_item_to_edit}')

    template = 'news/edit_news_item.html'
    context = {
        'news_form': news_form,
        'news_item': news_item_to_edit,
    }

    return render(request, template, context)


@login_required
def delete_news_item(request, news_item_id):
    """
    A view to delete news items
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    news_item = get_object_or_404(News, pk=news_item_id)
    news_item.delete()
    messages.success(request, f'{news_item.title} Successfully Deleted')
    return redirect(reverse('manage_news_items'))


def news_item(request, news_item_id):
    """
    A view to show an individual news item
    """
    news_item = get_object_or_404(News, pk=news_item_id)

    context = {
        'news_item': news_item,
    }

    return render(request, 'news/news_item.html', context)
