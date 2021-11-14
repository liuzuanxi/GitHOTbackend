#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Githot 
@File ：spider.py
@Author ：抱着欣欣看月亮
@Date ：2021/11/11 18:29 
'''
import urllib
from urllib.request import urlopen, Request
import requests
from scrapy.selector import Selector
import re

# TODO 4.实现爬虫类
class Spider():

    def __init__(self):
        '''爬虫静态配置'''

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    def _parse(self, url):

        '''
            实现获取网页（项目链接）内容并解析。
        :param url: 链接
        :return data: 爬取内容
        '''

        response = requests.get(url, headers=self.headers)
        # html = response.text
        s = Selector(text = html)
        title = s.xpath('//span[@itemprop="name"]/a/text()').extract_first()








        '''your demo'''
        data = {"title": str, "url": url, "introduction": str,'stars':int,"keyWords":list(str)}

        '''end'''
        return data

    def _getAllproject(self, num=10000):
        '''
            获得所有项目中一定量的项目
        :param num:获取项目数量
        :return project_urls: 返回链接列表
        '''
        '''your demo'''
        project_urls = list(str)

        '''end'''
        return project_urls
