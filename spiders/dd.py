# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request
import random
import re
from dangdang.items import DangdangItem

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%D4%FA%C8%BE']
    '''
    ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
          'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.3397.16 Safari/537.36',
          'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0']
    keywd = '扎染'
    url = 'http://search.dangdang.com/?key=' + str(keywd)
    req = urllib.request.Request(url).add_header('User-Agent', random.choice(ua))
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    pat_name = '<a title="(.*?)"'
    name = re.compile(pat_name).findall(data)
    '''
    def parse(self, response):
        item = DangdangItem()
        item["name"]= response.xpath('//a[@class="pic"]/@title').extract()
        item["price"] = response.xpath('//span[@class="search_now_price"]/text()').extract()
        item["comment"] = response.xpath('//a[@class ="search_comment_num"]/text()').extract()
        #print(item["name"])
        #print(item["price"])
        #print(item["comment"])
        yield item
        for i in range(1,3):
            url = 'http://search.dangdang.com/?key=%D4%FA%C8%BE&page_index='+str(i)
            yield Request(url,callback=self.parse)
            i+=1
