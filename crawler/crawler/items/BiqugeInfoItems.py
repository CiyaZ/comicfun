import scrapy


class NovelItem(scrapy.Item):
    item_name = scrapy.Field()
    nid = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    cover_img_url = scrapy.Field()


class NovelChapterItem(scrapy.Item):
    item_name = scrapy.Field()
    nid = scrapy.Field()
    order = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
