# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapethissiteSandboxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class teamStats(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    wins = scrapy.Field()
    losses = scrapy.Field()
    ot_losses = scrapy.Field()
    win_percent = scrapy.Field()
    goals_for = scrapy.Field()
    goals_against = scrapy.Field()
    goal_diff = scrapy.Field()