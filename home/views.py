from django.shortcuts import render
from news.models import News

def home(request):
    news_items_published = News.objects.filter(status=1).order_by('-create_date')[:5]
    return render(request, 'home/index.html/', {'news_items_published': news_items_published})
