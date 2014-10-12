# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class RatingItem(Item):
    user = Field()
    movie = Field()
    rating = Field()

class DoubanItem(Item):
    # define the fields for your item here like:
    # name = Field()
    groupName = Field()
    groupURL = Field()
    totalNumber = Field()
    RelativeGroups = Field()
    ActiveUesrs = Field()

