from django.template.response import TemplateResponse

from feedparser import parse

from feeds.settings import FEEDS


def homepage(request):
    items = []

    # import pdb
    # pdb.set_trace()

    for feed in FEEDS:
        feed_data = parse(feed)
        items.extend(feed_data['entries'])

    context = {
        'items': items
    }

    return TemplateResponse(request, 'main/home.html', context=context)