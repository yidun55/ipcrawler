# -*- coding: utf-8 -*-

# Scrapy settings for ipcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ipcrawler'

SPIDER_MODULES = ['ipcrawler.spiders']
NEWSPIDER_MODULE = 'ipcrawler.spiders'

DEFAULT_ITEM_CLASS = 'ipcrawler.items.PatenttestItem'
ITEM_PIPELINES=['ipcrawler.pipelines.IpcrawlerPipeline']

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 200,
        'ipcrawler.rotate_useragent.RotateUserAgentMiddleware' :400,
        # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
        # 'patenttest.middlewares.ProxyMiddleware': 100
    }
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ipcrawler (+http://www.yourdomain.com)'
