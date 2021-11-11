
'''
https://zhuanlan.zhihu.com/p/78571509
'''
import sqlite3
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import json
import csv
import time



class StocksSpider():
    # tbCreated用来记录是否建立了数据库的表格，0表示未创建
    tbCreated = 0
    # isLast用来判断是否翻页到最后
    isLast = False
    # 创建或来连接到数据库
    def openDB(self):
        self.con = sqlite3.connect("stocks.db")
        self.cursor = self.con.cursor()
        print('Connect to stocks.db successfully!')
    # 创建关系表
    def createTB(self):

        try:
            self.cursor.execute(
                "create table stocks "
                "(num varchar(32),"
                "st_code varchar(32),"
                "st_name varchar(32),"
                "st_price varchar(32),"
                "st_varition_rate varcahr(32),"
                "st_varition_value varchar(32),"
                "st_turnover varcahr(32),"
                "st_trading_volumn varchar(32),"
                "st_wave varchar(32),"
                "st_max varcahr(32),"
                "st_min varchar(32),"
                "st_td carcahr(32),"
                "st_yest varchar(32)"
                ")")
        except:
            # self.cursor.execute("delete from stocks")
            print('Table exists')
    # 提交数据库
    def commitDB(self):
        self.con.commit()
    # 关闭数据库
    def closeDB(self):

        self.con.commit()
        self.con.close()
    # 执行插入操作，输入的是各列表
    def insertDB(self, nums,
                 st_code,
                 st_name,
                 st_price,
                 st_varition_rate,
                 st_varition_value,
                 st_turnover,
                 st_trading_volumn,
                 st_wave,
                 st_max,
                 st_min,
                 st_td,
                 st_yest):
        try:
            for i in range(len(st_name)):
                self.cursor.execute \
                    ("insert into stocks (num,st_code,st_name,st_price,st_varition_rate,st_varition_value,st_turnover,st_trading_volumn,st_wave,st_max,st_min,st_td,st_yest) values (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                     (nums[i],
                      st_code[i],
                      st_name[i],
                      st_price[i],
                      st_varition_rate[i],
                      st_varition_value[i],
                      st_turnover[i],
                      st_trading_volumn[i],
                      st_wave[i],
                      st_max[i],
                      st_min[i],
                      st_td[i],
                      st_yest[i]
                      )
                     )


        except Exception as err:
            print(err)

# 打开浏览器
    def open_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.wait = WebDriverWait(self.browser,10)


    # 将表格内容一行一行打印出来
    def show(self,
             nums, codes, names, latest_prices, change_pencent,
             change_amount, turnover_hand, turnover_amount,
             wave, maximum, minimum, today, yesterday
             ):



        fmt = "{0:<16}\t{1:<16}\t{2:<16}\t{3:<16}\t{4:<16}" \
              "{5:<16}\t{6:<16}\t{7:<16}\t{8:<16}\t{9:<16}" \
              "{10:<16}\t{11:<16}\t{12:<16}"
        print(fmt.format('序号', '股票代码', '股票名称', '最新报价', '涨跌幅', '张跌额', '成交量', '成交额', '振幅', '最高', '最低', '今开', '昨收',
                         chr(12288)))
        # fmt = "{0:<16}\t{1:<16}\t{2:<16}\t{3:<16}\t{4:<16}" \
        #       "{5:<16}\t{6:<16}\t{7:<16}\t{8:<16}\t{9:<16}" \
        #       "{10:<16}\t{11:<16}\t{12:<16}"
        data = zip(nums, codes, names, latest_prices, change_pencent, change_amount, turnover_hand, turnover_amount,
                   wave, maximum, minimum, today, yesterday)
        for item in data:
            # print(i)
            print(
                fmt.format(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9],
                           item[10], item[11], item[12]))

    # 将网页中指定的信息爬取下来，再插入数据库
    def parse_page(self):
        try:
            #以下为各目标数据项
            nums = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[1]')))
            nums = [item.text for item in nums]

            codes = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[2]/a')))
            codes = [item.text for item in codes]
            names = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td[@class="mywidth"]/a')))
            names = [item.text for item in names]

            latest_prices = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[@class="mywidth2"][1]/span')))
            latest_prices = [item.text for item in latest_prices]

            change_pencent = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[@class="mywidth2"][2]/span')))
            change_pencent = [item.text for item in change_pencent]

            change_amount = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[7]/span')))
            change_amount = [item.text for item in change_amount]

            turnover_hand = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[8]')))
            turnover_hand = [item.text for item in turnover_hand]

            turnover_amount = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[9]')))#'//*[@id="table_wrapper-table"]/tbody/tr[1]/td[9]'
            turnover_amount = [item.text for item in turnover_amount]

            wave = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[10]')))#'//*[@id="table_wrapper-table"]/tbody/tr[1]/td[9]'
            wave = [item.text for item in wave]

            maximum = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[11]/span')))#'//*[@id="table_wrapper-table"]/tbody/tr[1]/td[9]'
            maximum = [item.text for item in maximum]

            minimum = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[12]/span')))#'//*[@id="table_wrapper-table"]/tbody/tr[1]/td[9]'
            minimum = [item.text for item in minimum]

            today = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[13]/span')))#'//*[@id="table_wrapper-table"]/tbody/tr[1]/td[9]'
            today = [item.text for item in today]


            yesterday = today = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//tbody/tr/td[14]')))#'//*[@id="table_wrapper-table"]/tbody/tr[1]/td[9]'
            yesterday = [item.text for item in yesterday]
            today = [item.text for item in today]
            # 以上为个目标数据项

            # 将数据项插入关系表中
            self.insertDB(nums, codes, names, latest_prices, change_pencent, change_amount, turnover_hand, turnover_amount, wave, maximum, minimum, today, yesterday)
            # 插入之后立刻提交
            self.commitDB()
            # 打印出插入的数据
            self.show(nums, codes, names, latest_prices, change_pencent,
                      change_amount, turnover_hand, turnover_amount,
                       wave, maximum, minimum, today, yesterday)

        except selenium.common.exceptions.TimeoutException:
            print('parse_page: TimeoutException')
            self.parse_page()
        except selenium.common.exceptions.StaleElementReferenceException:
            print('parse_page: StaleElementReferenceException')
            self.browser.refresh()

    # 翻页功能，模拟点击‘下一页’按钮来实现翻页操作
    def turn_page(self):
        try:
            # 点击按钮：下一页
            self.wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="next paginate_button"]'))).click()
            time.sleep(1)
            # 滑屏获取全部元素
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
        except selenium.common.exceptions.NoSuchElementException:
            self.isLast = True
        except selenium.common.exceptions.TimeoutException:
            print('turn_page: TimeoutException')
            self.turn_page()
        except selenium.common.exceptions.StaleElementReferenceException:
            print('turn_page: StaleElementReferenceException')
            self.browser.refresh()



    def close_browser(self):
        self.browser.quit()
    # 爬取指定url开头的网页
    def crawl(self,url):
        # self.open_file()
        self.open_browser()
        # self.init_variable()
        print('开始爬取: ',url)

        self.browser.get(url)
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        # count 用来实现对页数的控制
        count = 1
        # 打开数据库
        self.openDB()
        if self.tbCreated == 0:
            self.createTB()
            self.tbCreated = 1
        # 爬取两页，故count最大可以取到2
        while count <= 2:

            print('正在爬取第 ' + str(count) + ' 页......')
            count += 1
            # 爬取网页内容
            self.parse_page()
            # 实现翻页
            self.turn_page()
        print('结束爬取')

if __name__ == '__main__':
    spider = StocksSpider()
    urlfmt = 'http://quote.eastmoney.com/center/gridlist.html#{}_a_board'
    # url_list存的是沪深，深证，上证的网页链接
    url_list = [urlfmt.format('hs'),urlfmt.format('sz'),urlfmt.format('sh')]

    for url in url_list:
        spider.crawl(url)
    spider.closeDB()