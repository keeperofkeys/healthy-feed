from django.template.response import TemplateResponse

from feedparser import parse

from feeds.settings import FEEDS
from models import NewsItem


def live_feed(request):
    items = []

    for feed in FEEDS:
        feed_data = parse(feed)
        items.extend(feed_data['entries'])

    context = {
        'items': items
    }

    return TemplateResponse(request, 'main/home.html', context=context)


def homepage(request):

    context = {
        'items': NewsItem.objects.all()
    }

    return TemplateResponse(request, 'main/home.html', context=context)