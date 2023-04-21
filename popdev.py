# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains  #处理鼠标悬停事件
from selenium.webdriver import  TouchActions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By   #By类：定位元素
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import sys
import os
import time,datetime
import random
from root_scripts.common import Common
from root_scripts.common import output_print
#Python3字符串默认编码unicode
libpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not libpath in sys.path:
    sys.path.append(libpath)

class web_test(Common):
    output_print=output_print()
    def __init__(self, logname):
        Common.__init__(self, logname)
        self.account='aosom'
        self.password='9b973e8e-f77a-413a-b247-e920ff2f23af'

    def set_up(self, web='https://admindev.aosom.com/', device_type='html'):
        '''常见的操作元素方法如下：
        clear 清除元素的内容
        send_keys 模拟按键输入
        click 点击元素
        submit 提交表单'''
        device_type=device_type.upper()
        if device_type=='H5':
            mobile_emulation = {'deviceName': 'iPhone X'}
            options = webdriver.ChromeOptions()
            options.add_experimental_option('mobileEmulation', mobile_emulation)
        else:
            options = webdriver.ChromeOptions()
        self.browser=webdriver.Chrome("C:/Users/aosom/AppData/Local/Google/Chrome/Application/chromedriver.exe", chrome_options=options)#firefox_profile=profile,
        try:
            self.browser.implicitly_wait(10)  # 隐式等待10秒，如果在10秒内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
            self.browser.get(web)   #在当前窗口加载 url
            self.logger.info("Start web:%s" %web)
            self.browser.maximize_window()
            print("Set window to max size.")
        except TimeoutException:
            print("Can not open the web!")

    def close(self):
        self.browser.close()  #关闭当前窗口, 如果当前窗口是最后一个窗口, 浏览器将关闭
        self.browser.quit()  #关闭所有窗口并停止 ChromeDriver 的执行
        print("Close the browser.")

    def login(self,account='',password=''):
        '''登陆控制台'''
        self.browser.find_element_by_id('username').send_keys(account)
        print("Input account:%s"%account)
        self.browser.find_element_by_id('password').send_keys(password)
        print("Input password:%s" % password)
        time.sleep(1)
        self.browser.find_element_by_class_name('login-button').click()
        print("Click login")
        self.browser.set_page_load_timeout(10)
        # self.browser.implicitly_wait(20)

    def switch_language(self):
        '''切换显示的语言'''
        while not self.browser.find_element_by_class_name('main-menu').is_displayed():
            time.sleep(2)
        time.sleep(5)  #等待登陆成功提醒消失
        self.browser.find_element_by_class_name('ant-select-selection__rendered').click()
        time.sleep(1)
        # self.browser.find_element_by_link_text('简体中文').click()
        self.browser.find_element_by_xpath("//ul[@class='ant-select-dropdown-menu']/li[1]").click()
        print("switch language to Chinese.")

    def total_test(self):
        self.set_up()
        self.login('aosom', '9b973e8e-f77a-413a-b247-e920ff2f23af')
        self.switch_language()



if __name__ == '__main__':
    test=web_test('popdev')
    test.total_test()