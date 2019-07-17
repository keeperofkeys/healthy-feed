from datetime import datetime
from dateutil.parser import parse as parse_date

from feedparser import parse

from settings import FEEDS
from main.models import NewsItem


def __handle_feed_key__(entry, key):
    try:
        return entry[key]
    except KeyError:
        return 'unknown'

def import_feeds():
    count = 0

    for feed in FEEDS:
        source = feed[0]
        source_url = feed[1]
        feed_data = parse(source_url)

        for entry in feed_data['entries']:
            article_url = entry['link']

            news_item, new_entry = NewsItem.objects.get_or_create(url=article_url)

            if new_entry:
                news_item.title = entry['title']
                news_item.date = parse_date(entry['published'], ignoretz=True)
                news_item.author = __handle_feed_key__(entry, 'author')
                news_item.source = source
                news_item.summary = __handle_feed_key__(entry, 'description')
                news_item.save()

                count += 1

    print ('imported {count} new articles'.format(count=count))

