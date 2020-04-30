# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
import datetime


class DebugJsonPipeline:
    def open_spider(self, spider):
        path = 'cache'
        if not os.path.exists(path):
            os.mkdir(path)
        filename = spider.name + '-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.fetch.log'
        self.fp = open(path + '/' + filename, 'a+', encoding='utf-8')

    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        self.fp.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item
