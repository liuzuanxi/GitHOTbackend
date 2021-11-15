

import urllib
from urllib.request import urlopen, Request
import requests
from scrapy.selector import Selector
import re


def getHtml(url):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    # #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}# resp = requests.get(url, headers=header)
    # resp = urllib.request.urlopen(url,headers=headers)
    # html = resp.read().decode()


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    response = requests.get(url,headers=headers)
    html = response.text

    return html

url = 'http://fx.cmbchina.com/Hq/'
html = getHtml(url)
'//*[@id="realRateInfo"]/table/tbody/tr[3]/td[4]/text()'
s = Selector(text=html)

currency_list = s.xpath('//div[@id="realRateInfo"]//tr[position()>1]/td[1]/text()').extract()
tsp_list = s.xpath('//div[@id="realRateInfo"]//tr/td[@class="numberright"][1]/text()').extract()
csp_list = s.xpath('//div[@id="realRateInfo"]//tr/td[@class="numberright"][2]/text()').extract()
tbp_list = s.xpath('//div[@id="realRateInfo"]//tr/td[@class="numberright"][3]/text()').extract()
cbp_list = s.xpath('//div[@id="realRateInfo"]//tr/td[@class="numberright"][4]/text()').extract()
time_list = s.xpath('//div[@id="realRateInfo"]//tr/td[@align="center"][3]/text()').extract()
for i in range(len(cbp_list)):
    print(currency_list[i].strip())
    print(tsp_list[i].strip())
    print(csp_list[i].strip())
    print(tbp_list[i].strip())
    print(cbp_list[i].strip())
    print(time_list[i].strip())
    print()
'/html/body/div[5]/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[8]/text()'









# film = selector.xpath('//li')
#
# src = selector.xpath('//img/@src').extract()
# # name of film
# # alt = film.xpath('//div[@class="hd"]/a/span[1]/text()').extract()
# alt = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@alt').extract()
# # direct of film
# directors_actors = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]').extract()
# # alt = selector.xpath('//img/@alt').extract()
# abstruct = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()').extract()
# bg='''
#                             '''
# print(director_and_acts[0].replace(bg,'').replace('\n',''))
# for i in range(len(directors_actors)):
#     t = directors_actors[i]#.replace('bg','')
#     t = "".join(t.split())
#     t= t.replace(u'\xa0', '')
#     d_a = t.split(':')
#     # print(t.split(':'))
#     director = d_a[1][0:len(d_a[1])-2]
#     actor = d_a[-1]
#     print('Director : ',director)
#     print('Actor : ',actor)



    # director = re.search(r'演:(.*?)主',t)
    # act = re.search(r'主演:(.*?)',t)

    # if director:
    #     # print(director.group(1),end='  ')
    #     if act:
    #         print(act.group(1))
    #     else:
    #         print('null')

# name_list = selector.xpath()
# star_list = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()').extract()
# print(len(src))
# for i in range(25):
#     print(alt[i])
# //*[@id="content"]/div/div[1]/ol/li[25]/div/div[2]/div[2]/div/span[2]
# //*[@id="content"]/div/div[1]/ol/li[22]/div/div[1]/a/img
