# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
import re

class BookscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def extract_stock(value):
    match = re.search(r'\((\d+)', value)
    return match.group(1) if match else value

class BookItem(Item):
    url = Field()
    title = Field()
    product_type = Field()
    price_excel_tax = Field()
    price_incl_tax = Field()
    Availability = Field(extract_stock=extract_stock)
    ratting = Field()
    description = Field()
    price = Field()
