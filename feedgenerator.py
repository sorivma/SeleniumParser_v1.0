from rfeed import *
from datetime import date, datetime


def create_items(data_part):
    item = Item(
        title=data_part[0],
        link=data_part[3],
        description=data_part[1],
    )
    return item


def create_feed(items):
    feed = Feed(
        title='Сводка новостей университетов транспортной отрасли',
        link='test',
        language='ru',
        lastBuildDate=datetime.now(),
        description='',
        items=items
    )
    return feed


def create_xml(data, name):
    items = [create_items(data_part) for data_part in data]
    feed = create_feed(items)
    with open(f'{name}_{date.today()}' + '.rss', 'w', encoding='UTF-8') as xml:
        xml.write(feed.rss())
