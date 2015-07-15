# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

os.chdir("e://DLdata")

class IpcrawlerPipeline(object):
    def process_item(self, item, spider):
        f = open("proxy_ips.txt", "a")
        writeIn = item['content']
        f.write(writeIn)
        f.close()
