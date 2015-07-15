#!usr/bin/env python
#coding: utf-8

"""
从专利局官网上爬取各公司的专利信息
"""
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy import log
import sys
from ipcrawler.items import *


reload(sys)
sys.setdefaultencoding("utf-8")


class patenttest(Spider):
    # download_delay=20
    name = 'kuaidaili'
    start_urls = ['http://www.kuaidaili.com/proxylist/']

    def parse(self, response):
        """
        doc
        """
        for i in range(1,11):
            url = self.start_urls[0] + str(i)
            yield Request(url, callback=self.ip_extract,dont_filter=True)

    def ip_extract(self, response):
        item = IpcrawlerItem()
        item["content"] = self.xpath(response)
        yield item

    def xpath(self, response):
        sel = response.selector
        ips = sel.xpath(u"//tbody/tr/td[1]/text()").extract()
        ports = sel.xpath(u"//tbody/tr/td[2]/text()").extract()

        if len(ips) == len(ports):
            ip_port_tu = zip(ips, ports)
            ip_port = ['http://'+":".join(item)+'\n' for item in ip_port_tu]
            ips_ports = "".join(ip_port)
            return ips_ports
        else:
            log.msg("error in xpath",level=log.ERROR)


