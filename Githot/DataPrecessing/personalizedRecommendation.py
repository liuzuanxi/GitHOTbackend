#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Githot 
@File ：personalizedRecommendation.py
@Author ：抱着欣欣看月亮
@Date ：2021/11/11 19:01 
'''

# TODO 个性化推荐模块


class PersonalizedRecommendation():
    def __init__(self,wx_id):
        ''':param wx_id:微信id'''
        self.wx_id = wx_id
        pass

    def getUserReadHistory(self,maxNum = 100):
        '''
            获取用户的阅读记录
        :param maxNum:获取的最大数量
        :return ReadHistory:list  []
        '''
        '''your demo'''
        ReadHistory = list(str)

        '''end'''