from datetime import datetime

from feedparser import parse

from settings import FEEDS
from main.models import NewsItem


def import_feeds():
    import pdb
    pdb.set_trace()

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
                news_item.date = datetime.strptime(entry['published'], '%a, %d %b %Y %H:%M:%S %Z')
                news_item.author = entry['author']
                news_item.source = source
                news_item.save()

                count += 1

    print ('imported {count} new articles'.format(count=count))

