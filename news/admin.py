from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    """
    Admin class for the News model.
    """
    list_display = (
        'title',
        'user',
        'news_item_text',
        'image',
        'update_date',
        'create_date',
        'status',
    )
    list_filter = (
        'title',
        'user',
        'create_date',
    )
    search_fields = (
        'title',
        'user',
        'news_item_text',
        'image',
        'update_date',
        'create_date',
        'status',
    )
    list_per_page = 20


admin.site.register(News, NewsAdmin)
