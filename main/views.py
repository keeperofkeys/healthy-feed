from django.template.response import TemplateResponse
from django.http import HttpResponse


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
        'items': NewsItem.objects.all()[:50],
        'IS_ADMIN': True
    }

    return TemplateResponse(request, 'main/home.html', context=context)


def kill_story(request):
    story_url = request.POST['storyUrl']
    NewsItem.objects.get(url=story_url).delete()

    return HttpResponse('')
