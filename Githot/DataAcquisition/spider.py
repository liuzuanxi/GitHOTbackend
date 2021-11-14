#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Githot 
@File ：spider.py
@Author ：抱着欣欣看月亮
@Date ：2021/11/11 18:29 
'''


# TODO 4.实现爬虫类
class Spider():
    def __init__(self):
        '''爬虫静态配置'''
        pass

    def _parse(self, url):
        '''
            实现获取网页（项目链接）内容并解析。
        :param url: 链接
        :return data: 爬取内容
        '''
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

    def _search(self,keyWord,num):
        '''
            通过关键词搜索项目仓库链接
            :param keyWord:关键词
                   num:返回链接数量
            :return links:链接
        '''
        '''your demo'''
        links = list(str)

        '''end'''
        return links