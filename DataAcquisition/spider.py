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
import time
# TODO 4.实现爬虫类
class Spider():

    def __init__(self):
        '''爬虫静态配置'''


    def _parse(self, url):

        '''
            实现获取网页（项目链接）内容并解析。
        :param url: 链接
        :return data: 爬取内容
        '''
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        #
        # response = requests.get(url, headers=headers)
        # html = response.text
        html = self.getHtml(url)
        s = Selector(text = html)
        title = s.xpath('//strong[@itemprop="name"]/a/text()').extract_first()
        print(title)
        introductions = s.xpath('//div[@class="BorderGrid-cell"]/p[1]/text()').extract()
        introduction = ''
        for item in introductions:
            introduction += item.strip()
        print(introduction.strip())
        keywords = s.xpath('//div[@class="f6"]/a/text()').extract()
        # for keyword in keywords:
        #     print(keyword.strip())

        '''your demo'''
        # data = {"title": str, "url": url, "introduction": str,'stars':int,"keyWords":list(str)}

        '''end'''
        # return data

    def getHtml(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

        response = requests.get(url, headers=headers)
        html = response.text
        return html

    def _getAllproject(self, num):
        '''
            获得所有项目中一定量的项目
        :param num:获取项目数量
        :return project_urls: 返回链接列表
        '''
        '''your demo'''
        project_urls = []
        count = 0
        url = 'https://hub.fastgit.org/search?p={}&q=stars%3A%3E100&type=Repositories'
        for page in range(1,100):
            current_url = url.format(page)
            print('current url:  ',current_url)
            html = self.getHtml(current_url)
            s = Selector(text=html)
            urls = s.xpath('//li/div[2]/div[1]/div/a/@href').extract()
            # '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li[10]/div[2]/div[1]/div/a'
            pre_url = 'https://hub.fastgit.org'
            for item in urls:
                project_url = pre_url+item
                if len(project_urls) > num:
                    break
                project_urls.append(project_url)
            print(len(project_urls))
            if len(project_urls) > num:
                break
            time.sleep(5)
            print('end')
            # print()
        for i in project_urls:
            print(i)


        '''end'''
        return project_urls