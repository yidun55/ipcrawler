# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class IpcrawlerPipeline(object):
    def process_item(self, item, spider):
        f = open("/home/dyh/data/ipcrawler/proxy_ips.txt", "a")
        writeIn = item['content']
        f.write(writeIn)
        f.close()
