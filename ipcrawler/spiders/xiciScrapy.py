#!usr/bin/env python
#coding: utf-8

"""
从专利局官网上爬取各公司的专利信息
"""
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy import log
from scrapy import Selector
import sys
from ipcrawler.items import *


reload(sys)
sys.setdefaultencoding("utf-8")

class patenttest(Spider):
    # download_delay=20
    name = 'xici'
    start_urls = ['http://www.xici.net.co/nn']

    def parse(self, response):
        """
        获取总页数
        """
        urls = ["http://www.xici.net.co/nn/"+str(i) for\
         i in xrange(1, 204)]
        for url in urls:
            yield Request(url, callback=self.detail,\
                dont_filter=True)

    def detail(self, response):
        sel = Selector(text=response.body)
        ips = sel.xpath("//table[@id='ip_list']/tr[position()>1]\
                /td[3]/text()").extract()
        ports = sel.xpath("//table[@id='ip_list']/tr[position()>1]\
                /td[4]/text()").extract()

