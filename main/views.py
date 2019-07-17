from datetime import date, timedelta

from django.template.response import TemplateResponse
from django.http import HttpResponse


from feedparser import parse

from feeds.settings import FEEDS
from models import NewsItem


def homepage(request):
    items = NewsItem.objects.all()
    if 'provider' in request.GET.keys():
        items = items.filter(source=request.GET['provider'])

    context = {
        'items': items[:50],
        'IS_ADMIN': True
    }

    return TemplateResponse(request, 'main/home.html', context=context)


def show_post(request, year, month, day, slug):
    post_date = date(int(year), int(month), int(day))
    next_day = post_date + timedelta(days=1)
    news_item = NewsItem.objects.get(slug=slug, date__gte=post_date, date__lt=next_day)
    context = {
        'item': news_item
    }

    return TemplateResponse(request, 'main/post.html', context=context)


def kill_story(request):
    story_url = request.POST['storyUrl']
    NewsItem.objects.get(url=story_url).delete()

    return HttpResponse('')


# DEPRECATED
def live_feed(request):
    items = []

    for feed in FEEDS:
        feed_data = parse(feed)
        items.extend(feed_data['entries'])

    context = {
        'items': items
    }

    return TemplateResponse(request, 'main/home.html', context=context)