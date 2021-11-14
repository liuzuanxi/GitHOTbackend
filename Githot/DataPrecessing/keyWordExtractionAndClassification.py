#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Githot 
@File ：keyWordExtractionAndClassification.py
@Author ：抱着欣欣看月亮
@Date ：2021/11/11 18:49 
'''


# TODO 关键词提取及分类模块设计

class KeyWordExtractionAndClassification():
    def __init__(self, data = {"title": str, "url": str, "introduction": str,'stars':int,"keyWords":list(str)}):
        self.data = data
        pass

    def extractKeyWords(self):
        '''
            提取self.data中introduction的关键词
        :return keyWords
        '''
        '''your demo'''
        keyWords = list(str)

        '''end'''
        return keyWords

    def classificate(self):
        '''
            对项目进行分类
        :return projectClass
        '''
        '''your demo'''
        projectClass = int

        '''end'''
        return projectClass
