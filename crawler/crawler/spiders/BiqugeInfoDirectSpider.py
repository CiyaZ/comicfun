# -*- coding: utf-8 -*-
import scrapy
from crawler.items.BiqugeInfoItems import *


class BiqugeInfoDirectSpider(scrapy.Spider):
    name = 'BiqugeInfoDirectSpider'
    allowed_domains = ['biquge.info']
    custom_settings = {
        'CONCURRENT_REQUESTS': 32,
        'DOWNLOAD_DELAY': 0,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 32
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chapter_order = 0

    def start_requests(self):
        try:
            nid = self.nid
            if nid is None or nid == '':
                raise Exception('缺少抓取目标参数ID')
        except AttributeError:
            raise Exception('缺少抓取目标参数ID')

        urls = ['http://biquge.info/' + nid]
        for url in urls:
            yield scrapy.Request(url=url, meta={'nid': nid}, callback=self.parse)

    def parse(self, response):
        """列表页采集"""
        novel_item = NovelItem(item_name='NovelItem')

        # Novel 标题描述封面图
        title = response.css('#info h1::text').extract_first()
        desc = ''
        for desc_str in response.css('#intro p::text').extract():
            desc += desc_str
        cover_img_url = response.css('#fmimg img::attr(src)').extract_first()

        novel_item['nid'] = response.meta['nid']
        novel_item['title'] = title
        novel_item['desc'] = desc
        novel_item['cover_img_url'] = cover_img_url

        # 章采集
        for chapter in response.css('#list dl dd a'):
            chapter_href = chapter.css('::attr(href)').extract_first()
            chapter_title = chapter.css('::attr(title)').extract_first()

            yield response.follow(
                chapter_href,
                meta={
                    'nid': response.meta['nid'],
                    'chapter_title': chapter_title,
                    'chapter_order': self.chapter_order
                },
                callback=self.parse_novel_page)
            self.chapter_order += 1
        yield novel_item

    def parse_novel_page(self, response):
        """内容页采集"""
        chapter_title = response.meta['chapter_title']
        chapter_order = response.meta['chapter_order']
        nid = response.meta['nid']
        novel_chapter_item = NovelChapterItem(item_name='NovelChapterItem', nid=nid, title=chapter_title, order=chapter_order)
        content = ''
        for content_str in response.css('#content::text').extract():
            content += content_str
        novel_chapter_item['content'] = content
        yield novel_chapter_item
