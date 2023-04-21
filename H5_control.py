# -*- coding: utf-8 -*-
"""
版本更新记录
V1.0 2022/1/29
1.完成基础case的迁移

V1.1 2022/3/10
1.短信提醒增加完整站点执行后结果统计
2.匹配IT站地址输入的逻辑

V1.2 2022/3/12
1.将执行log同步输出到每日的txt log文件中

V1.3 2022/3/17
1.调整了print和logger的打印逻辑
2.主流程新增了添加心愿单
3.主流程新增了切换父子贴
4.主流程新增了打开评论集合页
5.优化了下单流程新增地址后保存超时的问题
6.优化了网站打不开的逻辑问题

V1.4 2022/4/6
1.优化父子贴切换的逻辑，大于4个一组的时候
2.优化单站点执行完后的异常站点统计逻辑
3.缩略图显示失败报错信息细化
4.关闭广告弹窗增加条件判定
5.搜索适配热搜词功能上线

V1.5 2022/4/21
1.优化登陆加载判断，添加无法登陆的报错
2.优化点击搜索框时弹出广告的逻辑判断
3.优化支付列表切换到某个支付方式长时间卡住的逻辑判断

V1.6  2022/5/18
1.更新适配意大利站地址输入去掉了邮编匹配的功能
2.更新适配类目页对商品筛选的判断
3.点击类目筛选第一层级进一步做数量限制

V1.7 2022/5/20
1.增加类目页适配landingpage的板式
2.增加IT站商详页scalapay判定

V1.8 2022/5/31
1.修复点击到新品页后选择商品报错的问题
2.优化类目页层级点击的逻辑
3.ES站登陆改造做适配

V1.9 2022/6/1
1.增加判定类目页为空的情况
2.适配新的支付流程
3.适配商详点击加购购物车新弹窗样式

V1.10 2022/6/6
1.增加点击类目菜单广告弹窗后异常判断
2.修复点击打开购物车可能出现概率性死循环的逻辑问题

V1.11 2022/6/17
1.修复搜索词页面新的样式适配
2.增加首页banner划动切换和点击打开
3.增加商详页商品FAQ提问

V1.11.2 2022/6/23
1.修复切换站点弹窗无法被关闭的问题
2.增加对父子贴商品的异常判断，优化异常截图

V1.12 2022/6/25
1.新增商详页所有详情图片的检查

V1.13 2022/7/5
1.增加浏览器版本升级导致无法执行脚本的报错提醒
2.新增脚本完成短信播报内容：天气播报

V1.14 2022/7/6
1.优化天气播报SSLEOFError的情况
2.修复商详页滑动产品图片的报错问题
3.优化打开类目页的地址判定，不是类目页的重新打开
4.替换全新短信播报模板，兼容更多的内容输出

V1.15 2022/7/8
1.修复加心愿单会有广告弹窗的判定
2.修复RO注册页面默认未勾选政策导致无法注册的问题

V1.16 2022/7/19
1.新增站点执行时间统计
2.修复商详页加购弹广告窗口的情况
3.修复商详页打开评论集合页时出现广告窗口的情况
4.兼容购物车页优惠券选择新样式

V1.17 2022/7/25
1.修复商详页切换父子贴商品的逻辑
2.修复商详页切换商品图片失败的问题
3.修复下单流程地址的判断偶尔异常的问题

V1.18 2022/8/3
1.兼容RO填写地址电话号码只有10位的限制

V1.19 2022/8/18
1.修复打开商品详情获取不到商品名称的问题
2.增加商详页没有找到商品加购按钮的详情

V1.20 2022/9/5
1.修复了新版类目页打开商品的广告弹窗报错
2.修改页面的加载策略，提高执行速率

V1.21 2022/9/15
1.适配新支付流程，增加对页面的判定/payment/onepage/
2.针对商品报错，取其sku替换商品名字
3.添加评论集合页的排序功能
4.增加当前站点是否点击过cookie弹窗的参数判定

V1.22 2022/9/22
1.增加支付流程total价格的判断
2.优化下单流程是否需要新增地址的判定
3.优化截图,增加了一部分截图高度
4.修复了滑动切换商详页图片move target out of bounds的问题

V1.23 2022/9/24
1.增加商详页评论数量上下的匹配确认
2.优化商详页滑动图片方向值偶尔为正值的异常处理
3.增加评论翻译功能
4.修复检查商详评论数量时弹出广告弹窗导致判定异常的问题
5.修复打开评论集合页正好弹广告弹窗的问题

V2.0 DEMO 2022/9/28
1.改造商详页图片检查check_image_in_detail_page函数，增加执行效率，缩短执行时间
2.优化划动图片检查的逻辑，只取一次划动值
3.更多的引入WebDriverWait显性等待，替换sleep强制等待，增加执行效率
4.增加ES支付勾选政策的动作
5.优化信用卡账号输入的组建判定，适配新老的3DS2支付组建

V2.0 2022/10/7
1.支持信用卡支付、paypal支付、amazon支付点击和结果检测
2.FR 增加配送方式切换：自提点功能异常导致点击支付异常 16FPMSLU92801
3.修复新增地址界面选择州元素无法点击的问题
4.兼容新老支付流程关于是否需要新建地址的判定

V2.1 2022/10/10
1.修复点击亚马逊支付跳转后，跳转回来页面没加载完的问题
2.修复点击折扣券有时候没有弹出来导致报错的问题
3.修复点击亚马逊支付后，页面回退，页面元素重新加载导致无法找到的问题
4.增加wait控件出现，等待时间的统计

V2.2 2022/10/21
1.快捷支付流程的兼容
2.增加商详和购物车页面打开404的判定
3.解决打开购物车时候，出现异常时的死锁问题
4.修改adyen支付报错验证逻辑

V2.3 2022/11/1
1.优化点击购物车的逻辑

V2.4 2022/11/24
1.兼容英国站page页cates图标点不到的问题

V2.5 2023/1/3
1.兼容最新版本的类目页结构，打开类目树随机选择类目

V2.6 2023/1/28
1.兼容新的支付错误模板
2.同步兼容US站信用卡支付报错
3.优化评论展示异常的数据反馈

V2.7 2023/3/14
1.US站信用卡支付报错详情内容展示
2.修复打开类目页最后一层脚本长时间卡住的问题
3.关闭不了广告弹窗，无限刷新页面
4.修复重复点击打开类目的问题 class="cates ga-event" data-ga-val="Category Menu"
5.兼容地址填充功能
6.修复添加心愿单 递归错误:无法从堆栈溢出中恢复Fatal Python error: Cannot recover from stack overflow.
Python runtime state: initialized
7.修复DE切换某个类目无法点击的情况
8.适配部分国家地址填写addr2必填和部分国家不存在该字段的问题

V2.8
1.修复游客购物功能，导致新增地址判定异常的问题
1.FR信用卡支付后弹的错误提醒遮挡 r_switch_payment_Amazon pay_failed

V2.N  待添加
1.改造get_status函数
引入协程 import asyncio
async def hanshu():
    XXX
    await asyncio.sleep(1)
asyncio.run(task)
4.增加下单流程的金额判定
3.个人中心操作
5.删除心愿单
6.将异常的截图上传，把图片链接分享到通知里面
7.评论集合页的操作
8.修改昵称
9.商详页ES clearpay图标，klarna分期
10.对所有的banner都点开一下
11.适配全新的登陆注册弹窗，增加一个是否登陆状态的全局变量
12.类目页操作筛选项 判定attribute-select-list->attribute-item项
13.加购弹窗的推荐商品点击跳转
14.购物车页勾选商品排序检查
15.检查评论统计页面各星级占比总和
16.商详推荐版位翻页后打开商品
17.快捷支付流程的兼容
18.游客购物兼容

"""
from selenium import webdriver
from selenium.webdriver import ActionChains  # 处理鼠标悬停事件
# from selenium.webdriver import TouchActions
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException, StaleElementReferenceException, SessionNotCreatedException
from selenium.webdriver.common.by import By   # By类：定位元素
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from requests_html import HTMLSession
import sys
import os
import time
import random
from rootscripts.common import Common
from message.sendmessage import Message
import contextlib  # 用于处理上下文管理器和with语句
import lxml.html as LH
import lxml.html.clean as clean
import asyncio

# Python3字符串默认编码unicode
libpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if libpath not in sys.path:
    sys.path.append(libpath)


class H5_test(Common, Message):
    # output_print = output_print()
    def __init__(self, log_name):
        Common.__init__(self, log_name)
        self.current_site = 'us'
        self.have_close_current_site_cookie = False  # 是否已经关闭当前站点的cookie弹窗
        # self.logger = self.createlogger(log_name)

    def set_up(self, web='https://www.aosom.ie/', device_type='html'):
        """常见的操作元素方法如下：
        clear 清除元素的内容
        send_keys 模拟按键输入
        click 点击元素
        submit 提交表单"""
        device_type = device_type.upper()
        if device_type == 'H5':
            # mobile_emulation = {'deviceName': 'iPhone X'}
            mobile_emulation = {
            "deviceMetrics": {"width": 320, "height": 1000, "pixelRatio": 3.0},  # 指定设备宽度、高度、分辨率以及ua标识
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.page_load_strategy = 'eager'  # 只等待结构加载的加载策略
            # options.add_argument('ignore-certificate-errors')
            options.add_experimental_option('mobileEmulation', mobile_emulation)  # 设置为手机模式
            # options.add_argument('--headless')  # 无头模式用以截全页面,实现不弹出浏览器，后台运行
            # options.add_argument('--disable-gpu')  # 关闭GPU计算
            # options.add_argument('--no-sandbox')  # 解决浏览器卡住不动的问题
        else:
            options = webdriver.ChromeOptions()
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('browser.download.dir', "download/") #设置默认下载路径
        # profile.set_preference('browser.download.folderList', 2)  #browser.download.folderList 设置Firefox的默认 下载 文件夹。0是桌面；1是“我的下载”；2是自定义
        # profile.set_preference('browser.download.manager.showWhenStarting', False)
        # profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')  #设置默认免提示文件类型
        # req_url="https://popdev.aosom.ie/"
        try:
            if os.path.exists("D:/python/chromedriver.exe"):
                self.browser = webdriver.Chrome("D:/python/chromedriver.exe", options=options)
            elif os.path.exists("C:/Users/aosom/AppData/Local/Google/Chrome/Application/chromedriver.exe"):
                self.browser = webdriver.Chrome(
                    "C:/Users/aosom/AppData/Local/Google/Chrome/Application/chromedriver.exe",
                    options=options)
            else:
                self.browser = webdriver.Chrome(
                    "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe",
                    options=options)
        except SessionNotCreatedException:  # 浏览器没有打开
            self.send_warning_message('ALL', '启动模拟浏览器', 'Chrome浏览器版本更新无法启动，请更新驱动')
            return False
        try:
            self.browser.implicitly_wait(
                10)  # 隐式等待10秒，如果在10秒内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步,设置全局的查找页面元素的等待时间，在这个时间内没找到指定元素则抛出异常，只需设置一次
            self.browser.get(web)  # 在当前窗口加载 url
            self.logger.info("Start web:%s" % web)
            if device_type != 'H5':
                self.browser.maximize_window()
                self.logger.info("Set window to max size.")
            else:
                self.browser.set_window_size(320, 1050)  # 浏览器带了个头部，所以设置的要比上面配置的分辨率高度多一点
                self.logger.info("Set window size to 320*1050.")
        except TimeoutException:
            print("Can not open the web!")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8"}  # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        self.sessions = HTMLSession()
        self.sessions.headers = headers
        return True

    def get_page(self, web='https://www.aosom.ie/'):
        try:
            self.browser.get(web)
            self.logger.info("Switch and open web:%s" % web)
            self.browser.implicitly_wait(6)
            return True
        except:
            self.logger.error("打开站点%s失败!" % self.current_site)
            self.send_warning_message(self.current_site, '站点打开', '打开站点失败')
            self.screenshot(self.browser, "%s_website_open_fail" % self.current_site)
            return False

    def close_ad(self):
        """关闭广告弹窗,如果关不掉就刷新页面"""
        close_time = 0
        while True:
            if self.iselementexist_by_classname(self.browser,
                                                'icon-modal-close') and self.browser.find_element_by_class_name(
                'icon-modal-close').is_displayed():
                print("class named icon-modal-close")
                try:
                    self.browser.find_element_by_class_name('icon-modal-close').click()
                    self.logger.info("Click close the AD or site switch remind.")
                    time.sleep(2)
                    close_time += 1
                    return True
                except ElementNotInteractableException:
                    self.browser.refresh()
                    self.logger.warning("ElementNotInteractable,Can not close the modal AD, refresh the page.")
                    self.delay(5)
                    return False
                except ElementClickInterceptedException:
                    self.browser.refresh()
                    self.logger.warning("ElementClickIntercepted,Can not close the modal AD, refresh the page.")
                    self.delay(5)
                    return False
            elif self.iselementexist_by_classname(self.browser,
                                                  'cloudiqClose') and self.browser.find_element_by_class_name(
                'cloudiqClose').is_displayed():
                print("class named cloudiqClose")
                try:
                    self.browser.find_element_by_class_name('cloudiqClose').click()
                    self.logger.info("Click close the cloudiq AD.")
                    time.sleep(2)
                    close_time += 1
                    return True
                except ElementNotInteractableException:
                    self.browser.refresh()
                    self.logger.warning("ElementNotInteractable,Can not close the cloudiq AD, refresh the page.")
                    self.delay(5)
                    return False
            elif self.iselementexist_by_classname(self.browser,
                                                  'smc-closer') and self.browser.find_element_by_class_name(
                'smc-closer').is_displayed():
                print("class named smc-closer")
                try:
                    self.browser.find_element_by_class_name('smc-closer').click()
                    self.logger.info("Click close the Smc AD.")
                    time.sleep(2)
                    close_time += 1
                    return True
                except ElementNotInteractableException:
                    self.browser.refresh()
                    self.logger.warning("ElementNotInteractable,Can not close the Smc AD, refresh the page.")
                    self.delay(5)
                    return False
                except StaleElementReferenceException:  # 在点击的时候，页面元素出现了刷新，当时定位到的元素出现了替换
                    self.browser.refresh()
                    self.delay(5)
                    return False
            elif close_time == 0:
                if not self.have_close_current_site_cookie:
                    if self.close_cookie():
                        return True
                    return False
                self.logger.info('Can not close the ad, Refresh the page')
                self.browser.refresh()
                self.delay(5)
                return False
            return False

    def close_cookie(self):
        """关闭cookie窗口"""
        if self.iselementexist_by_classname(self.browser, 'cookie-handle-button'):
            try:
                self.browser.find_element_by_class_name('cookie-handle-button').click()
                self.logger.info("Click confirm the cookie.")
                self.delay(1)
                self.have_close_current_site_cookie = True
                return True
            except ElementNotInteractableException:
                self.logger.info("确认cookie的图标无法交互,pass.")
                return False
            except ElementClickInterceptedException:
                self.close_ad()
                self.close_cookie()
                return True
        return False

    def close(self):
        self.browser.close()  # 关闭当前窗口, 如果当前窗口是最后一个窗口, 浏览器将关闭
        self.browser.quit()  # 关闭所有窗口并停止 ChromeDriver 的执行
        print("Close the browser.")

    def get_status(self, add=''):
        """获取页面状态码,并返回状态码，将符合类目格式的地址存入数组"""
        try:
            page_result = self.sessions.get(add, allow_redirects=False)
            status = page_result.status_code
            print("URL:%s status is:%s" % (add, status))
            status = str(status)
            return status
        except Exception as e:
            print(e)
            return False

    async def get_status_result(self, add='', sku='', photo_num=1):
        """获取页面状态码,并返回状态码，将符合类目格式的地址存入数组"""
        try:
            page_result = self.sessions.get(add, allow_redirects=False)
            status = page_result.status_code
            print("URL:%s status is:%s" % (add, status))
            status = str(status)
            if status == '404' or status == '403':
                status = ''
            if not status:
                # text_info = img.get_attribute('alt')
                self.logger.error("商详页图片加载失败")
                self.screenshot(self.browser, "%s_photo_display_failed" % self.current_site)
                self.send_warning_message(self.current_site, '商品详情页',
                                          '商品sku:%s,缩略图显示失败,图片为第%s张' % (sku, photo_num))
            # await asyncio.sleep(1)
        except Exception as e:
            print(e)
            return False

    def random_info(self, type='shopping'):
        """随机生成某一种资料，包含手机号，姓名，购物搜索词，信用卡号"""
        type = type.lower()
        if type == 'shopping' or type == 'shop':
            shop_list = ["pawhut", "chAir", "bed", "cat", "dog", "car", "outsunny", "HOMCOM", "vinsETto", "outdOOr"]
            return random.choice(shop_list)
        elif type == 'visa' or type == 'credit card' or type == 'card' or type == 'card number':
            card_list = ['4111 1111 4555 1142', '4988 4388 4388 4305', '4166 6766 6766 6746', '4646 4646 4646 4644',
                         '4003 5500 0000 0003', '4151 5000 0000 0008']
            return random.choice(card_list)
        elif type == 'phone' or type == 'phone number' or type == 'mobile number':
            return random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
                random.choice("0123456789") for i in range(8))
        elif type == 'email' or type == 'account':
            return 'test' + "".join(random.choice("0123456789") for i in range(8)) + '@aosom.com'

    def close_alart(self, alart='alart'):
        """对话框一般来说有三种：alert 只有确认键，confirm 确认+取消键，prompt 需要输入后确认
        浏览器自带的组件，比较丑一般不用"""
        al = self.browser.switch_to.alert
        # 使用accept方法点击“确定”
        alart = alart.lower()
        if alart == 'alart':
            al.accept()
        # 使用dismiss方法点击“取消”
        elif alart == 'confirm':
            al.dismiss()
        # 输入内容
        elif alart == 'prompt':
            al.send_keys('')

    def swipe_banner(self, swipe_time=6):
        """往左滑动banner"""
        if self.iselementexist_by_id(self.browser, 'bannerSlider'):
            try:
                banner = self.browser.find_element_by_id('bannerSlider')
                loc = banner.location  # {'x': 15, 'y': 193}
                # print(loc)
                width, height = self.get_current_page_width_and_height(self.browser)
                width = width / 2
                print("width middle is %s" % width)
                movex = -abs(width - loc['x'])  # 能往左移动的极限边界
                for i in range(swipe_time):
                    ActionChains(self.browser).drag_and_drop_by_offset(banner, movex, 0).perform()
                    time.sleep(1)
                    print('swipe left to switch the banner.')
                return True
            except ElementClickInterceptedException:
                self.close_ad()
                return self.swipe_banner(swipe_time)
            except Exception as e:
                print(e)
                self.logger.warning("Can not swipe the banner.")
                return False
        self.logger.warning("%s站无法找到banner版块" % self.current_site)
        self.screenshot(self.browser, "%s_not_find_banner" % self.current_site)
        return False

    def open_banner(self):
        """打开当前banner的页面"""
        if self.iselementexist_by_id(self.browser, 'bannerSlider'):
            try:
                self.browser.find_element_by_id('bannerSlider').click()
                self.logger.debug("Click open the current banner")
                time.sleep(3)
                self.browser.implicitly_wait(10)
                current_url = self.browser.current_url
                if '/page' not in current_url and '/activity' not in current_url:
                    self.logger.warning("Open banner failed, current url is:%s" % current_url)
                    return False
                self.logger.info("Open url:%s" % current_url)
                return True
            except ElementNotInteractableException:
                self.close_ad()
                return self.open_banner()
            except ElementClickInterceptedException:
                self.close_ad()
                return self.open_banner()
        self.logger.warning("%s站无法找到banner版块" % self.current_site)
        self.screenshot(self.browser, "%s_not_find_banner" % self.current_site)
        return False

    def search_pop(self, item_name=''):
        """有热搜词就点热搜词，没有就按字符串查找商品"""
        try:
            if self.iselementexist_by_classname(self.browser, 'search-wrap'):
                self.browser.find_element_by_class_name('search-wrap').click()
                print("Click search bar.")
                self.delay(2)
                if not self.browser.find_element_by_class_name('search-screen').is_displayed():  # 搜索页面展示
                    self.logger.warning("Open search bar failed, try again.")
                    self.search_pop(item_name)
                    return False
                if self.iselementexist_by_classname(self.browser, 'top-search-list'):  # 存在推荐的热搜词
                    search_word_list = self.browser.find_elements_by_xpath(
                        '//div[@class="top-search-list mt-3"]/div/ul/li/div')
                    word_length = len(search_word_list)
                    print("Get %s top search keywords." % word_length)
                    if word_length > 0:
                        i = random.randrange(1, word_length) - 1
                        word = search_word_list[i].text
                        self.logger.debug("Click top word:%s" % word)
                        search_word_list[i].click()
                        self.delay(2)
                        return True
                self.browser.find_element_by_class_name('search-input').send_keys(item_name)
                print("Input search item name:%s" % item_name)
                self.browser.find_element_by_class_name('search-icon').click()
                print("Click search.")
                time.sleep(2)
                return True
            self.logger.warning("Can not find search input bar.")
            self.screenshot(self.browser, "not_find_search_bar")
            return False
        except ElementClickInterceptedException:
            self.close_ad()
            self.search_pop(item_name)
            return True
        except ElementNotInteractableException:
            self.close_ad()
            self.search_pop(item_name)
            return True

    def add_cart_pop(self):
        """随机选择搜索列表的第X件商品添加购物车"""
        # soft_menu=self.browser.find_element_by_xpath('/html/body/div[5]/div[4]/div[2]/div[1]/div[2]/a[1]/div')
        total_count = self.check_commodity_count_pop()
        if total_count > 1:
            i = random.randint(1, total_count)
        else:
            self.logger.warning('Have no commodity list found!')
            self.screenshot(self.browser, "not_find_commodity_list")
            i = 1
        # print("Random choose num:%s commodity." % i)
        soft_menu = self.browser.find_element_by_xpath("//div[@class='grid']/a[%s]/div" % i)
        ActionChains(self.browser).move_to_element(soft_menu).perform()
        # add_to_cart_button=self.browser.find_element_by_link_text('Add to cart')
        time.sleep(2)
        text_img = self.browser.find_element_by_xpath("//div[@class='grid']/a[%s]/div/div" % i)
        text_info = text_img.get_attribute('name')
        print("Random choose commodity:%s." % text_info)
        if self.iselementexist_by_xpath(self.browser,
                                        "//div[@class='grid'/a[%s]/div/div/div[1]/div[1] and contains(text(),'Out of Stock')]" % i):
            print("The commodity is out of stock!")
            return False
        # self.browser.find_element_by_xpath("//div[contains(text(),'Add to basket')]").click()  #用这个值只会点击第一件商品的那个add，导致fail
        if self.iselementexist_by_xpath(self.browser,
                                        "//div[@class='grid']/a[%s]/div/div/div[5]/div[contains(text(),'Add to basket')]" % i):
            self.browser.find_element_by_xpath(
                "//div[@class='grid']/a[%s]/div/div/div[5]/div[contains(text(),'Add to basket')]" % i).click()  # 对应没有打分的商品
        elif self.iselementexist_by_xpath(self.browser,
                                          "//div[@class='grid']/a[%s]/div/div/div[7]/div[contains(text(),'Add to basket')]" % i):
            try:
                self.browser.find_element_by_xpath(
                    "//div[@class='grid']/a[%s]/div/div/div[7]/div[contains(text(),'Add to basket')]" % i).click()  # 对应有打分的商品
            except NoSuchElementException:
                self.logger.warning("Can not find Add to basket button.")
                self.screenshot(self.browser, "not_find_Add_to_basket_button")
                return False
        print("Click add to basket/cart.")
        time.sleep(4)

    def check_commodity_count_pop(self):
        """统计当前页面显示的商品个数"""
        elements = self.browser.find_elements_by_class_name("display-good-item")
        total_count = len(elements)
        print("Current page have %s commodities." % total_count)
        return total_count

    def into_detail_page_pop(self):
        """随机选一个界面上的商品点击，进入其商品详情界面"""
        try:
            total_count = self.check_commodity_count_pop()
            if total_count > 1:
                i = random.randint(1, total_count)
            else:
                print('Have no commodity list found!')
                i = 1
            # print("Random choose num:%s commodity." % i)
            soft_menu = ''
            if self.iselementexist_by_xpath(self.browser, "//div[@class='single-column']/a[1]/div"):
                # soft_menu = self.browser.find_element_by_xpath("//div[@class='single-column']/a[%s]/div" % i)
                soft_menu = self.browser.find_element_by_xpath("//div[@class='single-column']/a[%s]" % i)
            elif self.iselementexist_by_xpath(self.browser, "//div[@class='grid']/a[1]/div"):
                soft_menu = self.browser.find_element_by_xpath("//div[@class='grid']/a[%s]/div" % i)
            elif self.iselementexist_by_classname(self.browser, 'popular-box'):  # 新版的landingpage热销商品
                text_info = self.browser.find_element_by_class_name('popular-title').text
                self.browser.find_element_by_class_name('popular-box').click()
                print("In new category page,Choose commodity:%s to into detail page." % text_info)
                if self.wait_until_exist_by_classname(self.browser, 'content-title-name'):
                    return True
                # if self.iselementexist_by_classname(self.browser, 'not-main'):  # 404的页面
                #     self.screenshot(self.browser, 'open_commodity_detail_page_404')
                #     self.send_warning_message(self.current_site, '商详', '打开商详页404,sku:%s' % sku)
                #     return False
            if soft_menu != '':
                text_info = soft_menu.get_attribute('name')
                sku = soft_menu.get_attribute('sellersku')
                if not text_info:
                    text_info = self.browser.find_element_by_xpath(
                        "//div[@class='single-column']/a[%s]/div/div[1]/img" % i).get_attribute(
                        'alt')  # 当没有name获取到，就从alt标签里面拿
                ActionChains(self.browser).move_to_element(soft_menu).perform()
                # self.scroll_to_element_by_class()
                self.logger.debug("Scroll to commodity:%s, SKU:%s" % (text_info, sku))
                photo_add = self.browser.find_element_by_xpath(
                    "//div[@class='single-column']/a[%s]/div/div[1]/img" % i).get_attribute('src')
                time.sleep(1)
                result = self.get_status(photo_add)
                if result == '404' or result == '403':
                    result = ''
                if not result:
                    self.logger.error("图片加载失败")
                    self.screenshot(self.browser, "%s_photo_display_failed" % self.current_site)
                    self.send_warning_message(self.current_site, '商品列表页',
                                              '列表页商品sku:%s缩略图显示失败,地址:%s' % (sku, photo_add))
                # text_img=self.browser.find_element_by_xpath("//div[@class='single-column']/a[%s]/div/div" %i)
                print("Random choose commodity:%s to into detail page." % text_info)
                soft_menu.click()
                if self.wait_until_exist_by_classname(self.browser, 'content-title-name'):
                    return True
                if self.iselementexist_by_classname(self.browser, 'not-main'):  # 404的页面
                    self.screenshot(self.browser, 'open_commodity_detail_page_404')
                    self.send_warning_message(self.current_site, '商详', '打开商详页404,sku:%s' %sku)
                    return False
            self.logger.info("Current category has no commodity!")
            return False
        except ElementClickInterceptedException:
            self.close_ad()
            # time.sleep(4)
            self.into_detail_page_pop()
            return False
        except ElementNotInteractableException:
            self.close_ad()
            self.into_detail_page_pop()
            return False
        except NoSuchElementException:
            self.logger.debug("Can not find any commodity.")
            return False

    def check_image_in_detail_page(self):
        """检查商详页的所有商品banner图是否正常,因为懒加载的机制需要滑动才能加载出实际图片"""
        if self.iselementexist_by_classname(self.browser, 'content-top-img'):
            try:
                # img_list = self.browser.find_elements_by_class_name('content-top-img')
                # img_list = self.browser.find_elements_by_xpath('//picture[@class="picture"]')
                img_list = self.browser.find_elements_by_xpath('//div[contains(@class,"content-top-img")]/picture')
                # img_url_list=[]
                img_count = len(img_list)
                self.logger.info("The commodity has %s images." % img_count)
                # current_url = self.browser.current_url
                sku = self.browser.find_element_by_class_name('content-title').get_attribute('sellersku')
                # for img in img_list:
                width, height = self.get_current_page_width_and_height(self.browser)
                width = width/2
                print("width middle is %s" % width)
                loc = img_list[0].find_element_by_tag_name('img').location  # {'x': 15, 'y': 193}
                # print(loc)
                movex = 0
                if loc['x'] >= 10:  # 获取第一张图片的左划极限，后面的图片都按这个标准划动
                    movex = -abs(width - loc['x'])  # 能往左移动的极限边界
                for i in range(img_count):
                    # banner = img.find_element_by_tag_name('img')
                    banner = img_list[i].find_element_by_tag_name('img')
                    # 存在标签下是video tag的情况
                    if banner:
                        url = banner.get_attribute('src')
                        if url != '':
                            # img_url_list.append(url)
                            # result = self.get_status(url)
                            # task=[]
                            # task.append(asyncio.create_task(self.get_status_result(url)))
                            # await asyncio.wait(task)
                            asyncio.run(self.get_status_result(url, sku, i+1))
                            # if result == '404' or result == '403':
                            #     result = ''
                            # if not result:
                            #     # text_info = img.get_attribute('alt')
                            #     self.logger.error("商详页图片加载失败")
                            #     self.screenshot(self.browser, "%s_photo_display_failed" % self.current_site)
                                # self.send_warning_message(self.current_site, '商品详情页',
                                #                           '商品sku:%s,缩略图显示失败,图片为第%s张' % (sku, i + 1))
                        # loc = banner.location  # {'x': 15, 'y': 193}
                        # # print(loc)
                        # movex = 0
                        # if loc['x'] >= 10:
                        #     movex = -abs(width - loc['x'])  # 能往左移动的极限边界
                        if movex:
                            print('swipe left %s to switch the detail photo.' % movex)
                            ActionChains(self.browser).drag_and_drop_by_offset(banner, movex, 0).perform()
                            # time.sleep(1.5)
                        # url= img.find_element_by_tag_name('img').get_attribute('src')
                return True
            except Exception as e:
                self.screenshot(self.browser, "%s_get_commodity_photo_failed" % self.current_site)
                print(e)
                return False

    def check_scalapay(self):
        """判定商详页的scalapay的标签是否存在"""
        if self.iselementexist_by_id(self.browser, 'scalapay-widget-outter'):
            self.logger.info("Check scalapay displayed.")
            return True
        self.logger.warning("Can not find scalapay in item detail page.")
        self.send_warning_message(self.current_site, '商详', '商详页没有显示Scalapay组件')
        return False

    def check_reviews_count_in_detail_page(self):
        """检查商品评论数量上下是否匹配"""
        if self.iselementexist_by_classname(self.browser, 'content-reviews-text'):
            top_count = self.browser.find_element_by_class_name('content-reviews-text').find_element_by_tag_name('span').text
            # print(top_count)
            top_count = top_count.strip()
            # print(top_count)
            try:
                self.scroll_to_element_by_class(self.browser, 'content8-reviews')  # 评论统计版块
                below_count = self.browser.find_element_by_class_name('global-ratings').find_element_by_tag_name('span').text
                below_count = below_count.strip()
                # print(below_count)
                if below_count and below_count != top_count:
                    sku = self.browser.find_element_by_class_name('content-title').get_attribute('sellersku')
                    self.logger.warning("%s站商品sku:%s,上:%s下:%s展示的评论总数量不一致" % (self.current_site, sku, top_count, below_count))
                    self.send_warning_message(self.current_site, "商详", "商品sku:%s,展示的评论上:%s下:%s总数量不一致" % (sku, top_count, below_count))
                    self.screenshot(self.browser, "%s_comment_not_match_%s" % (self.current_site, sku))
                    return False
                elif not below_count:
                    sku = self.browser.find_element_by_class_name('content-title').get_attribute('sellersku')
                    self.logger.warning("没有获取到global-ratings对应的字段，没有得到评论条数")
                    self.screenshot(self.browser, "%s_not_find_global_ratings_%s" % (self.current_site, sku))
                    self.send_warning_message(self.current_site, "商详",
                                              "商品sku:%s,没有正常加载出评论数,页面异常" % sku)
                    return False
                self.logger.info("商品评论总数量%s,验证OK." % top_count)
                return True
            except ElementNotInteractableException:
                self.close_ad()
                return self.check_reviews_count_in_detail_page()

        self.logger.debug("商品没有评论内容.")
        return False

    def translate_review_in_detail_page(self):
        """在商详页点击翻译评论"""
        if self.iselementexist_by_classname(self.browser, 'translate-item'):
            self.scroll_to_element_by_class(self.browser, 'translate-item')
            # 获取翻译按钮兄弟节点的文字内容
            if self.iselementexist_by_xpath(self.browser, "//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span[@class='seclist-less']"):
                contant_old = self.browser.find_element_by_xpath("//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span[@class='seclist-less']").text
            else:
                # contant_old = self.browser.find_element_by_xpath(
                #     "//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span[@class='commentLess']/span[@class='seclist-less']").text
                contant_old = self.browser.find_element_by_xpath(
                    "//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span/span[@class='seclist-more']").text

            print("contant before translate:%s" % contant_old)
            self.browser.find_element_by_class_name('translate-item').click()
            self.logger.debug("Click translate button.")
            time.sleep(3)
            if self.iselementexist_by_xpath(self.browser, "//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span[@class='seclist-less']"):
                contant_new = self.browser.find_element_by_xpath("//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span[@class='seclist-less']").text
            else:
                contant_new = self.browser.find_element_by_xpath(
                    "//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span/span[@class='seclist-more']").text
            # contant_new = self.browser.find_element_by_xpath("//div[contains(@class, 'translate-item')]/preceding-sibling::div[contains(@class, 'content8-item-describe')]/span[@class='seclist-less']").text
            print("contant after translate:%s" % contant_new)
            if contant_new == contant_old:
                self.logger.warning("translate not working,before and after are the same:%s" % contant_old)
                self.screenshot(self.browser, "%s_translate_review_failed" % self.current_site)
                return False
            self.logger.info("translate succeed.")
            return True
        return False

    def into_reviews_page(self):
        """进入评论集合页"""
        try:
            if self.iselementexist_by_classname(self.browser, 'content8-reviews'):
                # review=self.browser.find_element_by_class_name('content8-reviews')
                # ActionChains(self.browser).move_to_element(review).perform()
                self.scroll_to_element_by_class(self.browser, 'content8-reviews')
                self.delay(1)
            if self.iselementexist_by_classname(self.browser, 'to-reviews'):
                self.browser.find_element_by_class_name('to-reviews').click()
                self.logger.info("Click into reviews page.")
                self.delay(4)
                return True
            self.logger.debug("The commodity has no reviews page.")
            return False
        except ElementNotInteractableException:
            self.close_ad()
            return self.into_reviews_page()
        except ElementClickInterceptedException:
            self.close_ad()
            return self.into_reviews_page()

    def sort_in_reviews_page(self):
        """在评论集合页排序"""
        try:
            if "/reviews/" in self.browser.current_url:
                if self.iselementexist_by_classname(self.browser, 'content8-sortby-select'):
                    self.browser.find_element_by_class_name('content8-sortby-select').click()
                    chooses = self.browser.find_elements_by_class_name('dropdown-item')
                    choose_count = len(chooses)
                    i = random.randrange(0, choose_count - 1)
                    info = chooses[i].text
                    chooses[i].click()
                    self.logger.info("Click to sort by:%s" % info)
                    time.sleep(1)
        except ElementNotInteractableException:
            self.close_ad()
            self.sort_in_reviews_page()

    def switch_product_pop(self):
        """在商详页面，如果存在父子产品，随机切换一个"""
        try:
            if self.iselementexist_by_classname(self.browser, 'content2-image'):  # 组合贴的商品图片合辑栏
                self.scroll_to_element_by_class(self.browser, 'content2-image')
                # products=self.browser.find_elements_by_class_name('content2-image-imgDiv')  #未选中的分类叫content2-image-imgDiv或者是content2-image-img，那个被选中的叫content2-image-IsimgDiv
                if self.iselementexist_by_classname(self.browser, 'content2-image-imgDiv'):
                    products = self.browser.find_elements_by_xpath('//div[@class="content2-image-imgDiv"]/img')
                elif self.iselementexist_by_classname(self.browser, 'content2-image-img'):  # 超出4个组合的情况
                    self.browser.find_element_by_class_name('content2-image-img').click()
                    time.sleep(1)
                    # products = self.browser.find_elements_by_xpath('//div[@class="content2-image-img"]/img')
                    products = self.browser.find_elements_by_xpath('//div[@class="slide-right-content-item"]/div/img')
                    # 筛选一遍不可见的
                    prd_list = []
                    for prd in products:
                        if prd.is_displayed():
                            prd_list.append(prd)
                    products = prd_list
                elif self.browser.find_element_by_class_name('content2-image').test == "":
                    self.logger.info("没有父子贴的商品列表存在")
                    return False
                else:
                    self.logger.warning("没有匹配到父子贴的图片/内容展示")
                    self.screenshot(self.browser, "not_find_other_product_img")
                    return False
                count = len(products)
                if count == 0:
                    return False
                if count < 4:
                    count += 1
                print("The product have %s kinds contains current product." % count)
                i = random.randint(1, count - 1) - 1  # 只有1个的时候就取第0个
                # print("select the num %s product."%i)
                pruduct_name = products[i].get_attribute('alt')
                products[i].click()
                print("Click switch to:%s." % pruduct_name)
                time.sleep(5)
                return True
                # if self.iselementexist_by_xpath(self.browser, "//div[@class='product-right-product-bottom']/div[%s]"%i):
                #     pruduct_name=self.browser.find_element_by_xpath("//div[@class='product-right-product-bottom']/div[%s]/img" % i).get_attribute('alt')
                #     self.browser.find_element_by_xpath("//div[@class='product-right-product-bottom']/div[%s]" % i).click()
                #     print("Click switch to:%s."%pruduct_name)
                #     time.sleep(1)
                #     return True
            print("The product have no other configural product.")
            return False
        except ElementClickInterceptedException:
            self.logger.info('Switch product element intercepted.')
            return False

    def FAQ(self, name='test account', questions='Aosom FAQ function test.'):
        """在商详页打开FAQ，输入内容并提交"""
        if self.iselementexist_by_classname(self.browser, 'ask-btn'):
            try:
                self.scroll_to_element_by_class(self.browser, 'ask-btn')
                time.sleep(1)
                self.browser.find_element_by_class_name('ask-btn').click()
                print("Click ask a question button.")
                time.sleep(2)
                FAQPOPUPs = self.browser.find_elements_by_class_name('FAQ-popup')
                for faqpopup in FAQPOPUPs:
                    if faqpopup.is_displayed():
                        faq_operation = faqpopup
                        break
                faq_operation.find_element_by_class_name('FAQ-input').send_keys(name)
                faq_operation.find_element_by_class_name('FAQ-textarea').send_keys(questions)
                time.sleep(1)
                faq_operation.find_element_by_class_name('submit-btn').click()
                self.logger.info("Input name:%s and questions:%s,click submit." % (name, questions))
                time.sleep(1)
                if self.iselementexist_by_classname(self.browser, 'faq-success-btn'):  # 新toast优化，faq提交确认弹窗
                    self.browser.find_element_by_class_name('faq-success-btn').click()
                    print('Click FAQ success submit button.')
                if faq_operation.is_displayed():
                    faq_operation.find_element_by_id('back-faq-arrow').click()
                    print("Click back arrow to quit FAQ.")
                    time.sleep(1)
                return True
            except Exception as e:
                print(e)
                self.logger.warning("FAQ operation failed.")
                return False

    def buy_in_detail_page_pop(self):
        """在商品详情界面直接点击购买"""
        if self.iselementexist_by_classname(self.browser, 'content4-buy'):
            self.browser.find_element_by_class_name('content4-buy').click()
            print("Click to buy now.")
            return True
        elif self.iselementexist_by_classname(self.browser, 'content4-notice'):
            print("The commodity is sold out! select Notify me when available")
            self.browser.find_element_by_class_name('content4-notice').click()
            return True
        self.screenshot(self.browser, "not_find_buy_button")
        return False

    def add_cart_in_detail_page_pop(self, notify=False):
        """在商品详情界面点击添加购物车"""
        try:
            if self.iselementexist_by_classname(self.browser, 'content4-add'):
                self.browser.find_element_by_class_name('content4-add').click()
                print("Click to add to cart.")
                time.sleep(3)
                if self.iselementexist_by_classname(self.browser,
                                                    'cart-close-icon') and self.browser.find_element_by_class_name(
                    'cart-close-icon').is_displayed():
                    self.browser.find_element_by_class_name('cart-close-icon').click()
                    print("Click close the cart popup.")
                    time.sleep(1)
                return True
            elif self.iselementexist_by_classname(self.browser, 'content4-notice-no'):  # 新的到货提醒图标
                if notify:
                    print("The commodity is sold out! select Notify me when available")
                    self.browser.find_element_by_class_name('content4-notice-no').click()
                    return True
                else:
                    print("The commodity is sold out!")
                    return False
            elif self.iselementexist_by_classname(self.browser, 'content4-notice'):  # 老的到货提醒图标
                if notify:
                    print("The commodity is sold out! select Notify me when available")
                    self.browser.find_element_by_class_name('content4-notice').click()
                    return True
                else:
                    print("The commodity is sold out!")
                    return False
            self.logger.warning("没有找到加购或者是到货提醒的button.")
            self.screenshot(self.browser, "%s_not_find_addcart_or_notice_button" % self.current_site)
            return False
        except ElementClickInterceptedException:
            self.close_ad()
            return self.add_cart_in_detail_page_pop(notify)
        except ElementNotInteractableException:
            self.close_ad()
            return self.add_cart_in_detail_page_pop(notify)

    def add_wishlist(self):
        """在商详页点击添加心愿单"""
        if self.iselementexist_by_classname(self.browser, 'content4-collect-collect'):
            if self.browser.find_element_by_class_name('content4-collect-collect').is_displayed():
                try:
                    self.browser.find_element_by_class_name('content4-collect-collect').click()
                    self.logger.info('Click add to wishlist.')
                    self.delay(3)
                    return True
                except ElementClickInterceptedException:
                    self.close_ad()
                    # self.add_wishlist()
                    return False
            self.logger.debug('The commodity is already in wish list.')
            return True
        self.logger.warning("Can not find add wish list button.")
        return False


    def open_signin_page_pop(self):
        """点击sign in主动进入登陆界面"""
        # account_name=self.browser.find_element_by_class_name('account')
        # account_name = self.browser.find_element_by_link_text('Account')
        # ActionChains(self.browser).move_to_element(account_name).perform()
        if self.iselementexist_by_classname(self.browser, 'account'):
            self.scroll_to_element_by_class(self.browser, 'account')
            time.sleep(1)
        else:
            self.screenshot(self.browser, "%s_cannot_find_account_button" % self.current_site)
            self.send_warning_message(self.current_site, '注册/登陆', "页面无法找到用户登陆图标，截图")
            return False
        try:
            # self.browser.find_element_by_xpath("//div[contains(text(),'Sign In')]").click()
            self.browser.find_element_by_class_name('account').click()
            print("Click sign in button.")
            if self.current_site == 'es':  # 只针对es站有登陆端口的选择
                if self.iselementexist_by_id(self.browser, 'login-2C'):
                    self.browser.find_element_by_id('login-2C').click()
                    print('Click 2C login page.')
            try:
                WebDriverWait(self.browser, 8).until(EC.presence_of_element_located(
                    (By.CLASS_NAME, 'login-form')))  # 元素是否出现
                return True
            except TimeoutException:
                self.logger.warning("%s点击登陆在8秒内都没有打开登陆界面" % self.current_site)
                self.screenshot(self.browser, '%s_not_open_login_page' %self.current_site)
                return False
            # self.browser.find_element_by_link_text('Sign In').click()
        except ElementClickInterceptedException:
            self.close_ad()
            return self.open_signin_page_pop()
        except NoSuchElementException:
            self.logger.warning("NoSuchElementException,Can not find the login button!")
            self.screenshot(self.browser, "%s_not_find_login_button" % self.current_site)
            return False

    def set_user_name(self):
        """设置账户名字"""
        if "/customer/account" in self.browser.current_url:
            return True
        self.logger.debug("Current not in user account center.")
        return False

    def login_pop(self, account='', password=''):
        """直接在登陆界面，输入账号密码，可用于注册和登陆"""
        if self.iselementexist_by_classname(self.browser, 'login-form'):
            self.browser.find_element_by_name("username").send_keys(account)
            self.browser.find_element_by_class_name('submit-btn').click()
            print("Input account:%s and continue." % account)
            time.sleep(1)
            if self.current_site == 'ro':
                if self.iselementexist_by_classname(self.browser, 'check'):
                    self.browser.find_elements_by_class_name('check')[1].click()  # 点击第二个check窗口
                    print('Click confirm the register policy.')
            self.browser.find_element_by_name("password").send_keys(password)
            # self.browser.find_element_by_class_name('submit-btn').click()
            self.browser.find_element_by_xpath('//div[@class="login-body"]/form/div[2]/div[1]/div[4]/div[1]').click()
            print("Input password:%s and continue." % password)
            time.sleep(2)
            result = self.wait_until_not_exist_by_classname(self.browser, 'login-body')
            self.logger.debug("等待登陆加载完成,结果为:%s" % result)
            if not result:  # 界面依旧卡在登陆界面
                self.logger.error("注册/登陆失败.")
                self.screenshot(self.browser, "%s_Login_fail" % self.current_site)
                self.send_warning_message(self.current_site, '注册/登陆', "注册/登陆账号:%s失败，保持登陆加载超10s界面未跳转" % account)
                return False
            return True
        self.logger.warning("Can not find login page!")
        self.screenshot(self.browser, "%s_Can_not_find_login_page" % self.current_site)
        return False

    def open_category_in_account_center(self):
        """在个人中心"""

    def delete_account_pop(self, password=''):
        """注销账号"""
        if not self.iselementexist_by_classname(self.browser, 'name'):
            self.screenshot(self.browser, 'Cannot_find_account_menu')
            return False
        account_name = self.browser.find_element_by_class_name('name')
        # account_name = self.browser.find_element_by_link_text('Account')
        ActionChains(self.browser).move_to_element(account_name).perform()
        time.sleep(1)
        try:
            self.browser.find_element_by_class_name("my-account").click()
            print("Click my account button.")
            time.sleep(2)
            # self.browser.find_element_by_link_text('Sign In').click()
        except NoSuchElementException:
            print("Can not find the my account button!")
            return False
        self.browser.find_element_by_xpath("//div[@class='content-top-right']").click()
        print("Click account edit button.")
        time.sleep(2)
        self.browser.execute_script('window.scrollBy(0,200)')
        self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[1]/ul/li[6]/div[1]').click()
        time.sleep(2)
        self.browser.find_element_by_id('deletePassword').send_keys(password)
        time.sleep(1)
        self.browser.find_element_by_class_name('delete-button').click()
        time.sleep(1)
        self.browser.find_element_by_class_name('no-border-button').click()
        print('Click confirm the delete.')
        time.sleep(1)

    def open_cart_pop(self, retry_time=0):
        """打开购物车"""
        # retry_time = 0
        if retry_time >= 10:
            self.logger.warning("Reach max retry click cart button times!")
            self.screenshot(self.browser, "%s_max_time_click_cart_button" % self.current_site)
            return False
        try:
            retry_time += 1
            # self.scroll_to_element_by_class(self.browser, 'cart')
            self.scroll_to_head(self.browser)
            self.browser.find_element_by_class_name('cart').click()
            print('Click the shopping cart button.')
            time.sleep(2)
            if self.iselementexist_by_classname(self.browser, 'empty-cart'):
                self.logger.debug("购物车为空.")
                self.browser.find_element_by_class_name('shopping-btn').click()
                time.sleep(2)
                return False
            elif self.iselementexist_by_classname(self.browser, 'not-main'):  # 404的页面
                self.screenshot(self.browser, 'open_category_404')
                self.send_warning_message(self.current_site, '支付', '打开购物车页面404')
                return False
            return True
        except ElementClickInterceptedException as e:
            print(e)
            if retry_time < 10:
                self.close_ad()
                return self.open_cart_pop(retry_time)
            self.logger.warning("Reach max retry click cart button times!")
            self.screenshot(self.browser, "%s_max_time_click_cart_button" % self.current_site)
            return False
        except Exception as e:
            print(e)
            if retry_time < 10:
                print("Click into cart failed, retry.")
                self.browser.refresh()
                time.sleep(3)
                return self.open_cart_pop(retry_time)
                # return False
            self.logger.warning("Reach max retry click cart button times!")
            self.screenshot(self.browser, "%s_max_time_click_cart_button" % self.current_site)
            return False

    def select_discount_pop(self):
        """在存在折扣码的界面,如果discount列表存在可选项，则选中"""
        try:
            if self.iselementexist_by_classname(self.browser, 'discount-main'):
                # while self.browser.find_element_by_class_name('loading-wrap').is_displayed():
                #     time.sleep(1)  #等待loading界面消失
                # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'discount-input')))
                soft_menu = self.browser.find_element_by_class_name('discount-input')  # 延迟不够主窗体会遮挡输入框，需要等待
                ActionChains(self.browser).move_to_element(soft_menu).perform()
                time.sleep(2)
                # self.browser.find_element_by_class_name('discount-input').click()
                # self.browser.execute_script("arguments[0].click();",self.browser.find_element_by_class_name('discount-input'))
                # print("Click discount input bar.")
                if self.iselementexist_by_xpath(self.browser,
                                                "//div[@class='discount-main']/following-sibling::label[1]") and self.browser.find_element_by_xpath(
                    "//div[@class='discount-main']/following-sibling::label[1]").is_displayed():  # 选择折扣码的按钮,兄弟节点的查询  用/following-sibling::*  方法(定位同级的第二位)，用/preceding-sibling::* (定位同级的第一位)
                    # if self.browser.find_element_by_xpath("//div[@class='discount-main']/following-sibling::label[1]").is_displayed():
                    self.browser.find_element_by_xpath(
                        "//div[@class='discount-main']/following-sibling::label[1]").click()
                    print("Click choose code button.")
                    time.sleep(2)
                    # discount_name = self.browser.find_element_by_xpath(
                    #     "//div[contains(@class,'discount-item')]/label[contains(@class,'item-text')]").text
                    if self.iselementexist_by_xpath(self.browser, "//div[@class='item-title']/label[1]"):
                        discount_name = self.browser.find_element_by_xpath("//div[@class='item-title']/label[1]").text
                        self.browser.find_element_by_class_name('popup-check').click()
                        # self.browser.find_element_by_xpath("//div[contains(@class,'discount-list')]").click()
                        print('Choose:%s.' % discount_name)
                        time.sleep(2)
                        return True
                    self.logger.warning("Discount list not displayed.")
                    self.screenshot(self.browser, 'discount_list_not_display')
                self.browser.find_element_by_xpath('//div[@class="input-box"]/input').click()
                self.logger.info("点击折扣input窗口.")
                if self.iselementexist_by_classname(self.browser, 'discount-item') and self.browser.find_element_by_class_name('discount-item').is_displayed():
                    discount_name = self.browser.find_element_by_class_name('discount-item').text
                    self.browser.find_element_by_class_name('discount-item').click()
                    print('Choose:%s.' % discount_name)
                    time.sleep(2)
                    return True
                print("Current have no discount code to choose.")
                self.browser.find_element_by_xpath('//div[@class="input-box"]/input').send_keys('Apponly')
                print("Input code:Apponly")
                self.browser.find_element_by_class_name('apply-btn').click()
                time.sleep(2)
                return False
            self.logger.warning("Can not find discount code window!")
            self.screenshot(self.browser, "%s_not_find_discount_code_window" % self.current_site)
            return False
        except ElementClickInterceptedException:
            self.close_ad()
            self.select_discount_pop()
            return False

    def select_discount_m2(self):
        """在存在折扣码的界面,如果discount列表存在可选项，则选中"""
        if self.iselementexist_by_classname(self.browser, 'aosom-input-content'):
            # while self.browser.find_element_by_class_name('loading-wrap').is_displayed():
            #     time.sleep(1)  #等待loading界面消失
            # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'discount-input')))
            # soft_menu = self.browser.find_element_by_class_name('discount-input') #延迟不够主窗体会遮挡输入框，需要等待
            # ActionChains(self.browser).move_to_element(soft_menu).perform()
            # time.sleep(2)
            try:
                self.browser.find_element_by_class_name('aosom-input-content').click()
                # self.browser.execute_script("arguments[0].click();",self.browser.find_element_by_class_name('discount-input'))
                print("Click discount input bar.")
            except ElementClickInterceptedException:
                self.logger.debug('折扣码输入框被遮挡.')
                if self.iselementexist_by_id(self.browser, 'cookies-es'):  # 西班牙独有的隐私策略
                    self.browser.find_element_by_xpath('//div[@id="cookies-es"]/div[2]/button[2]').click()
                    self.logger.debug("Click accept the cookies.")
                else:
                    self.scroll_to_element_by_class(self.browser, 'aosom-input-content')
                self.browser.find_element_by_class_name('aosom-input-content').click()
                print("Click discount input bar.")
            if self.browser.find_element_by_xpath("//div[@id='coupon-list']").is_displayed():  # 打折列表可见
                discount_name = self.browser.find_element_by_xpath("//div[@id='coupon-list']/ul[1]/li").text
                self.browser.find_element_by_xpath("//div[@id='coupon-list']/ul[1]/li").click()
                print('Choose:%s.' % discount_name)
                time.sleep(3)
                return True
            print("Current have no discount code to choose.")
            return False
        self.logger.warning("Can not find discount code window!")
        return False

    def add_address_book_pop(self, firstname='Big', lastname='Diao brother', city='Ningbo', zip=' D15 A6WR',
                             street='National Aquatic Centre, Snugborough Rd', mobile='1234567890'):
        """在address界面填写信息"""
        if self.iselementexist_by_classname(self.browser, 'add-form') or self.iselementexist_by_classname(self.browser,
                                                                                                          'edit-form'):
            # if self.iselementexist_by_classname(self.browser, "address-edit") or self.iselementexist_by_classname(
            #         self.browser, 'address-new') or self.iselementexist_by_classname(self.browser, 'add-form'):
            try:
                # if self.browser.find_element_by_xpath("//div[contains(text(),'Add New Address')]"):
                firstnames = self.browser.find_elements_by_name('firstname')
                if firstnames[0].is_displayed():
                    firstnames[0].send_keys(firstname)
                else:
                    firstnames[1].send_keys(firstname)
                print("Input first name:%s" % firstname)
                lastnames = self.browser.find_elements_by_name('lastname')
                if lastnames[0].is_displayed():
                    lastnames[0].send_keys(lastname)
                else:
                    lastnames[1].send_keys(lastname)
                print("Input last name:%s" % lastname)
                # state=self.browser.find_element_by_name('state')
                # self.browser.execute_script("arguments[0].scrollIntoView();", state)
                if self.iselementexist_by_classname(self.browser, 'enter-manual'):  #切换到手动输入地址
                    enter_manuals = self.browser.find_elements_by_class_name('enter-manual')
                    if enter_manuals[0].is_displayed():
                        enter_manuals[0].click()
                    else:
                        enter_manuals[1].click()
                    print("Click choose enter address manually")
                if self.iselementexist_by_name(self.browser, 'state'):
                    states = self.browser.find_elements_by_name('state')
                    if states[0].is_displayed():
                        states[0].click()
                    else:
                        states[1].click()
                    print('Click state.')
                    self.browser.find_element_by_xpath("//div[@class='option-list']/ul/li[1]").click()
                    # if 'payment/address' in self.browser.current_url:  # 老支付流程
                    #     self.browser.find_element_by_xpath("//div[@class='option-list']/ul/li[1]").click()
                    # else:
                    #     self.browser.find_element_by_xpath("//div[@class='option-list' and @style='']/ul/li[1]").click()
                        # 新支付流程因为国家也改成了有多个下拉地址框，做一个匹配display不为none的
                elif self.iselementexist_by_id(self.browser, 'statename'):
                    statenames = self.browser.find_elements_by_id('statename')
                    if statenames[0].is_displayed():
                        statenames[0].send_keys('Zhejiang')
                    else:
                        statenames[1].send_keys('Zhejiang')
                citys = self.browser.find_elements_by_name('city')
                if citys[0].is_displayed():
                    citys[0].send_keys(city)
                else:
                    citys[1].send_keys(city)
                print("Input city:%s" % city)
                # self.browser.execute_script('window.scrollBy(0,300)')
                postcodes = self.browser.find_elements_by_name('postcode')
                if postcodes[0].is_displayed():
                    postcodes[0].send_keys(zip)
                else:
                    postcodes[1].send_keys(zip)
                print("Input postcode:%s" % zip)
                # if self.current_site == 'it':  #这块功能移除了
                #     if self.iselementexist_by_classname(self.browser, 'it-option-list'):
                #         self.logger.info('专门针对意大利站，点击邮编匹配列表结果')
                #         self.browser.find_element_by_class_name('it-option-list').click()
                addr12 = self.browser.find_elements_by_name('addr1')
                if addr12[0].is_displayed():
                    addr12[0].send_keys(street)
                else:
                    addr12[1].send_keys(street)
                print("Input street:%s" % street)
                if self.current_site == 'de':  #de特有需求,必须要填写addr2
                    if self.iselementexist_by_name(self.browser, 'addr2'):
                        addr22 = self.browser.find_elements_by_name('addr2')
                        if addr22[0].is_displayed():
                            addr22[0].send_keys('street2')
                        else:
                            addr22[1].send_keys('street2')
                        print("Input street2:street2")
                mobiles = self.browser.find_elements_by_name('mobile')
                if mobiles[0].is_displayed():
                    mobiles[0].send_keys(mobile)
                else:
                    mobiles[1].send_keys(mobile)
                print("Input mobile number:%s" % mobile)
                # self.scroll_to_element_by_class(self.browser, 'button-save')
                # save_b = self.browser.find_element_by_class_name('button-save')
                # self.browser.execute_script("arguments[0].scrollIntoView();", save_b)
                retry_times = 0
                while self.iselementexist_by_classname(self.browser, 'button-save') and retry_times < 5:
                    button_saves = self.browser.find_elements_by_class_name('button-save')
                    if button_saves[0].is_displayed():
                        button_saves[0].click()
                        print('Click save button.')
                        time.sleep(5)
                    elif len(button_saves) > 1:
                        button_saves[1].click()
                        print('Click save button.')
                        time.sleep(5)
                    else:
                        break
                    # self.scroll_to_element_by_class(self.browser, 'button-save')
                    # self.browser.find_element_by_class_name('button-save').click()
                    retry_times += 1
                if retry_times >= 5:
                    self.logger.warning("Click address save button more then 5 times.")
                    self.screenshot(self.browser, "%s_click_address_save_button_many_times" % self.current_site)
                    return False
                return True
            except ElementNotInteractableException:
                self.screenshot(self.browser, '%s_ElementNotInteractable' % self.current_site)
                self.close_ad()
            except ElementClickInterceptedException:
                self.screenshot(self.browser, '%s_ElementClickIntercepted' % self.current_site)
                self.close_ad()
        print("Current not find add new address page.")
        self.screenshot(self.browser, "%s_not_find_add_new_address" % self.current_site)
        return False


    def add_address_book_m2(self, firstname='test', lastname='test', city='test', zip=' D15 A6WR',
                            street='Ningbo,Zhenhai', mobile='11111111111'):
        """在address界面填写信息"""
        # if self.iselementexist_by_xpath(self.browser, "//div[contains(text(),'Add New Address')]"):
        if self.iselementexist_by_classname(self.browser, 'address-edit'):
            self.browser.find_element_by_name('firstname').send_keys(firstname)
            print("Input first name:%s" % firstname)
            self.browser.find_element_by_name('lastname').send_keys(lastname)
            print("Input last name:%s" % lastname)
            self.delay(1)
            # state=self.browser.find_element_by_name('state')
            # self.browser.execute_script("arguments[0].scrollIntoView();", state)
            while self.browser.find_element_by_class_name('aosom-full-loading').is_displayed():
                self.delay(2)
                print('wait page load for 2 seconds.')
            if self.iselementexist_by_name(self.browser, 'region'):  # 法国不需要填州信息
                if self.browser.find_element_by_name('region').is_enabled():
                    self.browser.find_element_by_name('region').click()
                    print('Click state.')
                    self.delay(1)
                else:
                    self.logger.debug("选择state/region的位置无法点击!")
                    self.screenshot(self.browser, "cannot_click_region")
                if self.iselementexist_by_classname(self.browser, 'van-picker__confirm'):
                    self.browser.find_element_by_class_name('van-picker__confirm').click()
                else:
                    self.browser.find_element_by_name('region').send_keys('Test')
                    self.logger.debug("input region/state Test.")
            self.browser.find_element_by_name('city').send_keys(city)
            print("Input city:%s" % city)
            # self.browser.execute_script('window.scrollBy(0,300)')
            if self.iselementexist_by_name(self.browser, 'newzipcode'):
                self.browser.find_element_by_name('newzipcode').send_keys(zip)
                print("Input postcide:%s" % zip)
                self.delay(1)
                if self.current_site == 'it':
                    self.delay(2)
                    if self.iselementexist_by_classname(self.browser, 'autocomplete-container'):
                        self.browser.find_element_by_class_name('autocomplete-container').click()
                        self.delay(2)
            else:
                self.browser.find_element_by_name('zipcode').send_keys(zip)
                print("Input postcide:%s" % zip)
                self.delay(1)
            self.browser.find_element_by_name('street[0]').send_keys(street)
            print("Input street:%s" % street)
            # self.browser.execute_script('window.scrollBy(0,300)')
            self.browser.find_element_by_name('telephone').send_keys(mobile)
            print("Input mobile number:%s" % mobile)
            self.delay(1)
            # save_b = self.browser.find_element_by_class_name('van-button-save')
            # self.browser.execute_script("arguments[0].scrollIntoView();", save_b)
            self.browser.find_element_by_class_name('van-button-save').click()
            print('Click save button.')
            result = self.wait_until_not_exist_by_classname(self.browser, 'van-button-save')
            if not result:
                self.logger.debug("地址保存失败!")
                self.screenshot(self.browser, "save_address_failed")
                return False
            return True
        print("Can not find add new address page.")
        return False

    def judge_address_pop(self):
        """在支付界面选择address，如果已存在就直接选现成的,如果不存在就新建"""
        if "payment/address" in self.browser.current_url:  #老支付方式有address界面
            return False
        elif self.iselementexist_by_classname(self.browser, "add-form"):  # 单独只需要输入billing地址
            return False
        elif self.iselementexist_by_classname(self.browser, 'address-new'):  #新支付流程
            return False
        self.logger.info("Already have shipping address.")
        return True

    def switch_delivery_type(self):
        """在支付页切换配送方式"""
        if self.current_site == 'fr':
            if self.iselementexist_by_id(self.browser, 'delivery-first-chose'):
                delivery_types=self.browser.find_elements_by_class_name('a-radio')
                delivery_types[-1].click()
                self.logger.info("切换到最下面一种配送方式")
                all_inputs=self.browser.find_elements_by_class_name('text-field-input')
                all_inputs[0].send_keys("Big")
                all_inputs[1].send_keys("Diao brother")
                all_inputs[2].send_keys("202944-6000")
                self.browser.find_element_by_xpath("//a[@href='javascript:;']").click()
                if self.wait_until_exist_by_id(self.browser, 'pick-container', 5):
                    self.browser.find_element_by_class_name('pickup-bottom').click()
                    time.sleep(2)
                    self.browser.find_element_by_class_name('save-continue-button').click()
                    time.sleep(1)

    def checkout_pop(self):
        """在支付界面点击checkout直到付钱或者填地址界面,包含save&continue"""
        # checkout=self.browser.find_element_by_class_name('pay-btn')
        # save=self.browser.find_element_by_class_name('button-save')
        # while checkout&save:
        retry_times = 0
        while True and retry_times < 5:
            if "/payment/onepage" in self.browser.current_url and self.iselementexist_by_classname(self.browser,
                                                                                                   'radio-list'):  # 支付方式的列表
                self.logger.info("Current page have payment list.")
                return True
            elif "/payment/select" in self.browser.current_url:  # 新增的快捷支付页面
                self.browser.find_element_by_class_name('btn-primary').click()
                self.logger.info("Click Proceed to checkout.")
                time.sleep(4)
                retry_times += 1
                continue
            if self.iselementexist_by_classname(self.browser, 'pay-btn') and self.browser.find_element_by_class_name(
                    'pay-btn').is_enabled():
                self.scroll_to_element_by_class(self.browser, 'pay-btn')
                try:
                    self.browser.find_element_by_class_name('pay-btn').click()
                    print('Click proceed to checkout.')
                    if retry_times >= 3:
                        self.screenshot(self.browser, "%s_click_pay_button_%s_times" % (self.current_site, retry_times))
                    time.sleep(4)
                    retry_times += 1
                    continue
                except NoSuchElementException:
                    self.logger.info('NoSuchElementException,Can not find proceed to checkout button.')
                except ElementClickInterceptedException as e:
                    # print(e)
                    self.close_ad()
                    self.logger.info('ElementClickInterceptedException, continue loop the click.')
                    retry_times += 1
                    continue
            # elif self.iselementexist_by_xpath(self.browser, "//div[@class='container-table']/button[@class='button-save']"):
            # elif self.iselementexist_by_xpath(self.browser, "//div[@class='container-title' and contains(text(),'Select Shipping Option')]"):
            #     try:
            #         self.browser.find_element_by_class_name('button-save').click()
            #         print('Click save&contiune.')
            #         time.sleep(2)
            #         continue
            #     except NoSuchElementException:
            #         print('Can not find save&continue button.')
            print("Current page have no pay confirm button.")
            # self.screenshot(self.browser, "%s_have_no_pay_confirm_button" %self.current_site)
            return False

    def switch_pay_methods_pop(self):
        """切换一遍支付方式,通过支付方式判断是否要点击支付"""
        if self.iselementexist_by_classname(self.browser, 'radio-pay-item'):
            pay_list = self.browser.find_elements_by_class_name('radio-pay-item')
            value_key = ''
            if "/payment/checkout/" in self.browser.current_url:
                value_key = 'total-Price'
                price_default = self.browser.find_element_by_class_name(value_key).text
            elif "/payment/onepage/" in self.browser.current_url:
                value_key = 'price-text'
                price_default = self.browser.find_element_by_id(value_key).text
            # price_default = self.browser.find_element_by_class_name(value_key).text
            price = round(self.get_value_in_string(price_default) * 0.01, 2)  # 计算会有异常，只保留2位小数
            self.logger.info("当前订单总价为:%s" % price)
            for pay_method in pay_list:
                # pay_method_name = pay_method.find_element_by_xpath("//label[@class='radio-item']/div/span").text
                pay_method_name = pay_method.find_element_by_class_name('form-radio-label').text
                try:
                    # pay_method_name = pay_method.text[0]
                    pay_method.click()
                    self.logger.info('Switch to %s' % pay_method_name)
                    time.sleep(5)
                    if value_key == 'total-Price':
                        price_default = self.browser.find_element_by_class_name(value_key).text
                    elif value_key == 'price-text':
                        price_default = self.browser.find_element_by_id(value_key).text
                    price_now = round(self.get_value_in_string(price_default) * 0.01, 2)
                    price_gap = round(price_now - price, 2)
                    if price_now == 0:
                        self.logger.warning("切换到%s支付,总价显示为0" % pay_method_name)
                        self.screenshot(self.browser, '%s_pay_method_error' % pay_method_name)
                        self.send_warning_message(self.current_site, '支付', '切换到%s支付,总价显示为0' % pay_method_name)
                    elif price_gap != 0:
                        if pay_method_name == 'Contrassegno':
                            if round(price_gap-7.99, 1) != 0:
                                self.logger.warning("切换到%s支付,总价比默认贵了%s" % (pay_method_name, price_gap))
                            # self.logger.warning("切换到%s支付,界面异常" % pay_method_name)
                                self.screenshot(self.browser, '%s_%s_pay_price_higher' % (self.current_site, pay_method_name))
                        elif pay_method_name == 'Plata la livrare':
                            if round(price_gap-15.0, 1) != 0:
                                self.logger.warning("切换到%s支付,总价比默认贵了%s" % (pay_method_name, price_gap))
                            # self.logger.warning("切换到%s支付,界面异常" % pay_method_name)
                                self.screenshot(self.browser, '%s_%s_pay_price_higher' % (self.current_site, pay_method_name))
                        else:
                            self.logger.warning("切换到%s支付,总价比默认贵了%s" % (pay_method_name, price_gap))
                            # self.logger.warning("切换到%s支付,界面异常" % pay_method_name)
                            self.screenshot(self.browser,
                                            '%s_%s_pay_price_higher' % (self.current_site, pay_method_name))
                    pay_method_code = self.check_pay_status(pay_method)  # 是否点击支付状态，是则返回对应的支付code名
                    if self.current_site == 'es':  # ES站需要勾选政策
                        check_box = self.browser.find_elements_by_class_name('input-check')[-1]
                        if not check_box.is_selected():
                            check_box.click()
                            print("点击勾选政策确认框")
                    if pay_method_code:
                        if value_key == 'price-text':  # 如果是新支付流程的支付页
                            if self.iselementexist_by_classname(self.browser, 'pay-btn'):
                                time.sleep(1)
                                # loc=self.browser.find_element_by_class_name('pay-btn').location
                                # ActionChains(self.browser).move_by_offset(loc['x'], loc['y']).click().perform()
                                # ActionChains(self.browser).release()
                                # ActionChains(self.browser).click(self.browser.find_element_by_class_name('p-relative'))
                                self.browser.find_element_by_class_name('p-relative').click()
                                # self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_id('paypal-button'))
                                # self.browser.execute_script("arguments[0].click();",
                                #                             self.browser.find_element_by_class_name('paypal-buttons'))
                                # self.browser.execute_script("arguments[0].click();",
                                #                             self.browser.find_element_by_xpath('//*[@id="paypal-button"]'))
                                self.logger.info("点击新支付流程的pay button")
                        else:  # 如果是老支付流程的支付页
                            time.sleep(1)
                            if pay_method_code == 'adyen':
                                if self.iselementexist_by_classname(self.browser, 'adyen-checkout__button'):
                                    self.browser.find_element_by_class_name('adyen-checkout__button').click()
                                    self.logger.info("点击老支付流程的adyen pay button")
                            elif pay_method_code == 'paypal':
                                if self.iselementexist_by_classname(self.browser, 'paypal-buttons'):
                                    self.browser.find_element_by_class_name('paypal-buttons').click()
                                    self.logger.info("点击老支付流程的paypal pay button")
                            elif pay_method_code == 'amazon':
                                # if self.iselementexist_by_classname(self.browser, 'btn-primary'):
                                if self.iselementexist_by_id(self.browser, 'AmazonPayButton'):
                                    self.browser.find_element_by_id('AmazonPayButton').click()
                                    # self.browser.find_element_by_class_name('btn-primary').click()
                                    self.logger.info("点击老支付流程的Amazon pay button")
                        if pay_method_code == 'adyen':
                            if self.wait_until_exist_by_classname(self.browser, 'a-toasts--msg', 6):
                                toast_message = self.browser.find_element_by_class_name('a-toasts--msg').text
                                # print(toast_message)
                                if toast_message:
                                    if len(toast_message) > 40:
                                        self.logger.info("adyen支付得到预期的新版报错%s" % toast_message)
                                        continue
                                    if "FRAUD" in toast_message:
                                        self.logger.info("adyen支付得到预期的报错FRAUD")
                                        continue
                                    elif "CVC Declined" in toast_message:
                                        self.logger.info("adyen支付得到预期的报错CVC Declined")
                                        continue
                                    elif "3D Not Authenticated" in toast_message:
                                        self.logger.info("adyen支付得到预期的报错3D Not Authenticated")
                                        continue
                                # if self.current_site == 'at' or self.current_site == 'be' or self.current_site == 'pl':
                                #     if self.wait_until_exist_by_xpath(self.browser,
                                #                                       '//div[@class="a-toasts--msg"]/span[contains(text(),"FRAUD")]',
                                #                                       1):
                                #         self.logger.info("adyen支付得到预期的报错FRAUD")
                                #         continue
                                # else:
                                #     if self.wait_until_exist_by_xpath(self.browser,  '//div[@class="a-toasts--msg"]/span[contains(text(),"CVC Declined")]', 1):
                                #         self.logger.info("adyen支付得到预期的报错CVC Declined")
                                #         continue
                                    else:
                                        self.screenshot(self.browser, "%s_%s_pay_error" % (self.current_site, pay_method_code))
                                        self.logger.warning("%s支付没有找到对应的正确报错!" % pay_method_code)
                                        self.send_warning_message(self.current_site, "支付", "%s支付没有得到预期的错误提示,报错为：%s" % (pay_method_code, toast_message))
                                        continue
                            if "checkoutshopper-live.adyen.com" in self.browser.current_url or "customer/result/orderfail" in self.browser.current_url:
                                self.logger.debug("支付跳转到了3DS2验证页、支付失败，结束整个支付切换流程.")
                                time.sleep(4)
                                self.screenshot(self.browser, "%s_adyen_pay_to_failed_page" % self.current_site)
                                return False
                            self.logger.warning("%s支付没有弹出报错提醒!" % pay_method_code)
                            self.screenshot(self.browser, "%s_%s_pay_not_popup_error" % (self.current_site, pay_method_code))
                        elif pay_method_code == 'authorize':
                            if self.wait_until_exist_by_classname(self.browser, 'a-toasts--msg', 6):
                                toast_message = self.browser.find_element_by_class_name('a-toasts--msg').text
                                # print(toast_message)
                                if toast_message:
                                    if len(toast_message) > 40:
                                        self.logger.info("authorize支付得到预期的新版报错%s" % toast_message)
                                        continue
                                if self.wait_until_exist_by_xpath(self.browser,  '//div[@class="a-toasts--msg"]/span[contains(text(),"transaction has been declined")]', 1):
                                    self.logger.info("authorize支付得到预期的报错This transaction has been declined.")
                                    continue
                                self.logger.warning("%s支付没有找到对应的正确报错!" % pay_method_code)
                                self.screenshot(self.browser, "%s_%s_pay_error" % (self.current_site, pay_method_code))
                                self.send_warning_message(self.current_site, "支付", "%s支付没有得到预期的错误提示,报错为：%s" % (pay_method_code, toast_message))
                                continue
                            self.logger.warning("%s支付没有弹出报错提醒!" % pay_method_code)
                            self.screenshot(self.browser, "%s_%s_pay_not_popup_error" % (self.current_site, pay_method_code))
                        elif pay_method_code == 'paypal':
                            if self.wait_until_exist_by_classname(self.browser, 'a-toasts--msg', 3):
                                self.logger.warning("%s支付有报错!" % pay_method_code)
                                self.screenshot(self.browser, "%s_%s_pay_error" % (self.current_site, pay_method_code))
                                continue
                            windows = self.browser.window_handles
                            if len(windows) > 1:
                                print(windows)
                                main_window = self.browser.window_handles[0]
                                self.browser.switch_to.window(main_window)
                        elif pay_method_code == 'amazon':
                            if self.wait_until_exist_by_classname(self.browser, 'a-toasts--msg', 3):
                                self.logger.warning("%s支付有报错!" % pay_method_code)
                                self.screenshot(self.browser, "%s_%s_pay_error" % (self.current_site, pay_method_code))
                                continue
                            if self.wait_until_exist_by_xpath(self.browser, '//a[contains(@href,"amazon")]', 5):
                                self.logger.info("打开amazon支付界面成功")
                                self.browser.back()
                                print("Click back.")
                                if self.wait_until_exist_by_classname(self.browser, 'radio-pay-item', 8):
                                    # time.sleep(1)  # 等待支付列表加载出来，再多给1S
                                    return True  # 判定正常返回到支付列表页就算完结，继续点其他支付会有StaleElementReferenceException的异常
                                self.logger.debug("返回支付页超时.")
                                return False
                            self.logger.warning("打开%s支付界面超时" %pay_method_code)
                            self.screenshot(self.browser, "%s_%s_pay_timeout" % (self.current_site, pay_method_code))
                except ElementClickInterceptedException:
                    self.logger.warning("切换到%s支付界面任然在loading上一个支付方式." % pay_method_name)
                    self.screenshot(self.browser, "%s_switch_payment_%s_failed" % (self.current_site, pay_method_name))
                    time.sleep(5)
                # except Exception as e:
                #     print(e)
                continue
            return True
        self.logger.warning("找不到任何的支付方式")
        self.screenshot(self.browser, '%s_not_find_any_payment_method' % self.current_site)
        self.send_warning_message(self.current_site, '支付', '无法加载任何一种支付方式')
        return False

    def check_pay_status(self, pay_item):
        """判断当前支付方式，返回是否需要点击支付的状态，信用卡支付会自动填充卡信息"""
        # pay_method=self.browser
        pay_method=pay_item.find_element_by_tag_name('label').get_attribute('for')
        if "authorize_net" in pay_method:
            self.logger.info("美国信用卡authorize支付")
            self.input_credit_card_authorize_net()
            return "authorize"
        elif "paypal-pay" in pay_method:
            if "paypal_pay_paylater" in pay_method:
                self.logger.info("paypal paylater支付")
                return False
            else:
                self.logger.info("paypal支付")
                return 'paypal'
        elif "method-adyen-pay" in pay_method:
            self.logger.info("普通信用卡支付")
            # if self.current_site == 'pl' or self.current_site == 'at' or self.current_site == 'be':
            #     return False
            self.input_credit_card_pop()
            return "adyen"
        elif "amazon-pay" in pay_method:
            self.logger.info("亚马逊支付")
            return "amazon"
        elif "bank-transfer-pay" in pay_method:
            self.logger.info("普通银行转账支付")
            return False
        elif "adyen_klarna_soft" in pay_method:
            self.logger.info("adyen klarna支付")
            return False
        elif "clearpay" in pay_method:
            self.logger.info("clearpay支付")
            return False
        elif "bizum_pay" in pay_method:
            self.logger.info("bizum支付")
            return False
        elif "hipay_mb" in pay_method:
            if "hipay_mb_way" in pay_method:
                self.logger.info("hipay mbway支付")
                return False
            else:
                self.logger.info("hipay mb支付")
                return False
        elif "phoenix_cashondelivery" in pay_method:
            self.logger.info("货到付款支付")
            return False
        elif "scala_pay" in pay_method:
            self.logger.info("scalapay支付")
            return False
        else:
            self.logger.info("%s支付" %pay_method)
            return False

    def input_credit_card_pop(self, card_number='4351 3000 0000 0001', date='09/23', cvv=111, name='jack'):
        """判断是否存在信用卡信息输入框，是则输入信用卡信息并确认,这个界面镶嵌的是iframe框架，获取里面的东西需要进入这个框架
        VISA 4001919257537193 09/2023 738   Amex 374245455400126 05/2023 1111"""
        if not self.iselementexist_by_id(self.browser, "component-container"):
            print('Current not find card input iframe.')
            return False
        self.scroll_to_element_by_id(self.browser, "component-container")
        # self.browser.find_element_by_xpath("//span[contains(text(),'Add a credit or debit card')]").click()
        # print('Click switch to add a credit card.')
        iframe_cardnumber = self.browser.find_element_by_xpath(
            '//*[@id="component-container"]/div/div/div[2]/div[1]/div[1]/label/div/span/iframe')
        self.browser.switch_to.frame(iframe_cardnumber)
        if self.iselementexist_by_classname(self.browser, 'js-iframe-input'):
            self.browser.find_element_by_class_name('js-iframe-input').click()
            self.browser.find_element_by_class_name('js-iframe-input').send_keys(card_number)
        # self.browser.find_element_by_id('encryptedCardNumber').send_keys(card_number)
            print("Input card number:%s" % card_number)
        self.browser.switch_to.default_content()  # 返回到主界面
        time.sleep(0.5)
        iframe_date = self.browser.find_element_by_xpath(
            '//*[@id="component-container"]/div/div/div[2]/div[1]/div[2]/div[1]/label/div/span/iframe')
        self.browser.switch_to.frame(iframe_date)
        if self.iselementexist_by_classname(self.browser, 'js-iframe-input'):
            self.browser.find_element_by_class_name('js-iframe-input').click()
            self.browser.find_element_by_class_name('js-iframe-input').send_keys(date)
        # self.browser.find_element_by_id('encryptedExpiryDate').send_keys(date)
            print("Input expiry date:%s" % date)
        self.browser.switch_to.default_content()  # 返回到主界面
        time.sleep(0.5)
        iframe_cvv = self.browser.find_element_by_xpath(
            '//*[@id="component-container"]/div/div/div[2]/div[1]/div[2]/div[2]/label/div/span/iframe')
        self.browser.switch_to.frame(iframe_cvv)
        if self.iselementexist_by_classname(self.browser, 'js-iframe-input'):
            self.browser.find_element_by_class_name('js-iframe-input').click()
            self.browser.find_element_by_class_name('js-iframe-input').send_keys(cvv)
        # self.browser.find_element_by_id('encryptedSecurityCode').send_keys(cvv)
            print("Input CVC/CVV:%s" % cvv)
        self.browser.switch_to.default_content()  # 返回到主界面
        time.sleep(0.5)
        self.browser.find_element_by_xpath("//div[contains(@class,'card__holderName')]/label/div").click()
        self.browser.find_element_by_xpath("//div[contains(@class,'card__holderName')]/label/div/input").send_keys(name)
        # self.browser.find_element_by_xpath('//*[@id="component-container"]/div/div/div[2]/div[2]/label/div/input').send_keys(name)
        print("Input card holder name:%s" % name)
        # self.browser.find_element_by_xpath("//button[contains(@class,'checkout__button')]").click()
        # print("Click place order.")
        # self.browser.find_element_by_class_name("pay-btn").click()
        # time.sleep(10)

    def input_credit_card_authorize_net(self, card_number='4351 3000 0000 0001', date='09/23', cvv=111, name='jack'):
        """用于美国信用卡的authorize_net支付"""
        if not self.iselementexist_by_xpath(self.browser, '//div[@class="pay-method"]/span/span'):
            self.logger.debug("没有找到authorize_net支付的输入框")
            return False
        try:
            self.browser.find_element_by_xpath('//div[@class="pay-method"]/span/span[1]').find_element_by_class_name('text-field-input').send_keys(name)
            print("Input card holder name:%s" % name)
            self.browser.find_element_by_xpath('//div[@class="pay-method"]/span/span[2]').find_element_by_class_name('text-field-input').send_keys(card_number)
            print("Input card number:%s" % card_number)
            self.browser.find_element_by_xpath('//div[@class="pay-method"]/span/span[3]').find_element_by_class_name('text-field-input').click()
            time.sleep(1)
            self.browser.find_element_by_xpath('//div[@class="pay-method"]/span/span[3]/div[1]/div[2]/div[3]/ul/li[9]').click()
            print("Select month september")
            self.browser.find_element_by_xpath(
                '//div[@class="pay-method"]/span/span[4]').find_element_by_class_name('text-field-input').click()
            time.sleep(1)
            self.browser.find_element_by_xpath('//div[@class="pay-method"]/span/span[4]/div[1]/div[2]/div[3]/ul/li[2]').click()
            print("Select year 2023")
            self.browser.find_element_by_xpath('//div[@class="pay-method"]/span/span[5]').find_element_by_class_name('text-field-input').send_keys(cvv)
            print("Input CVC:%s" % cvv)
        except Exception as e:
            print(e)
            return False

    def get_search_keywords_pop(self):
        """从类目列表获取搜索的关键词"""
        if self.iselementexist_by_xpath(self.browser, "//div[contains(@class,'main-menu')]/div[2]/ul/li"):
            word_elements = self.browser.find_elements_by_xpath("//div[contains(@class,'main-menu')]/div[2]/ul/li")
            word_list = []
            for word_element in word_elements:
                if word_element.text:
                    word_list.append(word_element.text)
            del (word_list[-1])  # 删除最后一个值，一般不是类目的名字
            del (word_list[-1])  # 删除最后一个值，一般不是类目的名字
            print("Get hot search keyword list:%s" % word_list)
            return word_list
        return ['homcom', 'outsunny', 'pawhut']

    def open_cates_pop(self):
        """打开左上角的导航栏"""
        if self.iselementexist_by_classname(self.browser, 'cates'):
            try:
                self.browser.find_element_by_class_name('cates').click()
                self.logger.debug("Click open cates.")
                time.sleep(2)
                return True
            except ElementClickInterceptedException as e:
                print(e)
                self.close_ad()
                self.open_cates_pop()
                return False
            except ElementNotInteractableException as e:
                print(e)
                url=self.browser.current_url
                if 'page' in url:
                    mainurl=url.split("page")[0]
                elif 'activity' in url:
                    mainurl=url.split("activity")[0]
                # print(mainurl)
                self.browser.get(mainurl)
                # logo=self.browser.find_element_by_class_name('logo-wrap').click()
                # self.browser.find_element_by_xpath('//div[@class="cates ga-event"]').click()
                # self.browser.execute_script("arguments[0].click();", logo)
                time.sleep(5)
                self.open_cates_pop()
                return False

    def check_menu_count_pop(self):
        """统计页面上menu的数目"""
        # elements=self.browser.find_elements_by_xpath("//div[@class='main-menu']/div[2]/ul/li[@class='menu-li']") #子菜单的名字都雷同，在同一个页面隐藏显示
        # elements = self.browser.find_elements_by_xpath("//div[@class='menu-wrap main-menu show']/div[@class='menu-items']/ul/li")
        if self.iselementexist_by_xpath(self.browser, "//div[contains(@class,'show')]/div[2]/a"):  #新更新的元素结构发生了变化
            elements = self.browser.find_elements_by_xpath(
                "//div[contains(@class,'show')]/div[2]/a")
        else:
            elements = self.browser.find_elements_by_xpath(
                "//div[contains(@class,'show')]/div[2]/ul/li")  # 只有用上面的全名class才能定位到，所以改用contains
        count = len(elements)
        print("current page has %s menu." % count)
        return count

    def select_menu_pop(self):
        """随机选择类目,存储一个首级类目的元素，当点完最后一级菜单的时候，菜单关闭，判定首级类目元素相同则说明菜单已经关闭"""
        click_time = 0
        menu_list = ''
        first_element = ''
        while self.iselementexist_by_xpath(self.browser,
                                           "//div[contains(@class,'show') and contains(@class,'menu')]") and click_time < 4:  # 类目层级增加，适当增加循环次数
            total_count = self.check_menu_count_pop()
            if not first_element:
                first_element = self.browser.find_element_by_xpath("//div[contains(@class,'show') and contains(@class,'menu')]").get_attribute('class')
            else:
                current_element = self.browser.find_element_by_xpath("//div[contains(@class,'show') and contains(@class,'menu')]").get_attribute('class')
                if current_element == first_element:
                    print("Have selected the root menu.")
                    break
            if total_count < 1:
                self.logger.warning("Menu display error!")
                self.screenshot(self.browser, "%s_Menu_display_error" %self.current_site)
                return False
            if click_time == 0:
                if total_count - 2 > 8:
                    i = random.randint(1, 8)
                else:
                    i = random.randint(1, total_count - 3)  # 第一次点类目页回退3位把最下面2个类目去掉
            elif click_time == 1:
                i = random.randint(1, total_count - 1)  # 去掉末尾的一个，很可能是类目新品集合页
            else:
                i = random.randint(1, total_count - 1)
            if self.iselementexist_by_xpath(self.browser, "//div[contains(@class,'show')]/div[2]/a"):
                menus = self.browser.find_elements_by_xpath("//div[contains(@class,'show')]/div[2]/a")
            else:
                menus = self.browser.find_elements_by_xpath("//div[contains(@class,'show')]/div[2]/ul/li")
            try:
                menu = menus[i]
                if i == 0 and menu.get_attribute('href') == menus[1].get_attribute('href'): #如果首元素和第二个元素相等
                    menu = menus[1]
                menu_text = menu.text
                if menu.is_displayed():
                    menu.click()
                else:
                    print("Element not displayed")
                    continue
                print('Select :%s.' % menu_text)
                # menu_list='-'.join(menu_text)
                if menu_list == "":
                    menu_list += menu_text
                else:
                    menu_list += "->" + menu_text
                time.sleep(1)
            except ElementClickInterceptedException:
                if self.close_ad():  # 如果广告关闭成功就接着点
                    time.sleep(1)
                    click_time -= 1
                else:  # 如果广告关闭失败刷新了界面，就重头开始点
                    self.open_cates_pop()
                    self.select_menu_pop()
                    return False
            except ElementNotInteractableException:
                print("Element not interactable")
            except Exception as e:
                print(e)
                print("Can not click sub menu anymore.")
                break
            click_time += 1
        print(menu_list)
        if self.iselementexist_by_classname(self.browser, 'not-main'):  # 404的页面
            self.screenshot(self.browser, 'open_category_404')
            self.send_warning_message(self.current_site, '类目', '打开类目页%s 404' % menu_list)
            return False

    def login_parttime(self):
        """ send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
            send_keys(Keys.SPACE) 空格键(Space)
            send_keys(Keys.TAB) 制表键(Tab)
            send_keys(Keys.ESCAPE) 回退键（Esc）
            send_keys(Keys.ENTER) 回车键（Enter）
            send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
            send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
            send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
            send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
            send_keys(Keys.F1) 键盘 F1...F12
            使用的前提是我们必须引用keys模块。
            """
        self.browser.find_element_by_name("password").send_keys(Keys.TAB)
        while self.browser.current_url != "http://192.168.10.1/wcn/frame/.x":
            time.sleep(1)

    def get_site_url(self, site='us'):
        """获取站点名对应的地址"""
        site_info = self.read_config('url')
        # print(site_info)
        if site == 'random':  # 随机抽一个
            site = random.choice(list(site_info.keys()))
            self.logger.info("Random select site:%s" % site)
        if site in site_info.keys():
            self.logger.info("Get site:%s the url is:%s" % (site, site_info[site]))
            return site_info[site]
        return False

    def get_site_zip(self, site=''):
        site_info = self.read_config('zip')
        if site in site_info.keys():
            self.logger.info("Get site:%s the zip is:%s" % (site, site_info[site]))
            return site_info[site]
        return False

    def get_site_dict(self):
        """获取所有站点对应的字典"""
        site_info = self.read_config('url')
        return site_info

    def get_phonenumber_list(self):
        """获取配置文件中的短信号码列表"""
        mobile_info = self.read_config('mobile')
        # print(site_info)
        mobile_list = []
        for mobilenumber in mobile_info.values():
            mobile_list.append(mobilenumber)
        self.logger.info('Get mobilenumber list:%s' % mobile_list)
        return mobile_list

    def send_warning_message(self, site='US', module='支付', detail='点击支付无响应'):
        """发送通知短信"""
        mobile_list = self.get_phonenumber_list()
        self.send_error_message(mobile_list, site, module, detail)

    def send_finish_message(self, time='2022-11-11', total_site_count=15, error_site_list=[]):
        """执行结束后发送统计通知短信"""
        mobile_list = self.get_phonenumber_list()
        weather = self.weather()
        if weather:
            self.send_notification_message(mobile_list, time, total_site_count, error_site_list, weather)
        else:
            self.send_notification_message(mobile_list, time, total_site_count, error_site_list, '网络异常,无法获取')

    def get_all_page_text(self, url=''):
        """获取页面所有的text"""
        with contextlib.closing(self.browser) as browser:
            ignore_tags = ('script', 'noscript', 'style')
            browser.get(url)
            content = browser.page_source
            cleaner = clean.Cleaner()
            content = cleaner.clean_html(content)
            doc = LH.fromstring(content)
            for elt in doc.iterdescendants():
                if elt.tag in ignore_tags:
                    continue
                text = elt.text or ''
                tail = elt.tail or ''
                words = ' '.join((text, tail)).strip()
                if words:
                    print(words)

    def weather(self):
        """获取当天天气信息"""
        try:
            result = self.sessions.get('https://tianqi.2345.com/zhejiang-zhuangshijiedao1d/46799.htm')
            # print(result.html.html)
            today_weather = result.html.xpath('//div[@class="real-today"]/span/text()')
            # print(today_weather[0].strip())
            current_report = result.html.xpath('//p[@class="real-wea-info"]/text()')
            real_air = result.html.xpath('//ul[@class="real-air"]/li/a/span/text()')
            current_temp = result.html.xpath('//div[@class="real-icon wea-white-icon"]/span/text()')
            current_weather = result.html.xpath('//div[@class="real-icon wea-white-icon"]/em/text()')
            weather_info = ''
            if today_weather:
                weather_info += '天气' + today_weather[0].strip() + ' '
            if current_report:
                weather_info += current_report[0] + ' '
            if current_temp:
                weather_info += '当前气温:' + current_temp[0] + ' '
            if current_weather:
                weather_info += current_weather[0] + ' '
            if real_air:
                weather_info += '空气质量:' + real_air[0]
            print(weather_info)
            return weather_info
        except Exception as e:
            print(e)
            return False

    def part_test(self):
        # site_dict = self.get_site_dict()
        self.set_up(
            'https://www.aosom.co.uk', 'h5')
        st = time.time()
        # self.close_ad()
        self.close_cookie()
        self.current_site='uk'
        current_url = self.browser.current_url
        if '/category' not in current_url:
            self.open_cates_pop()
            # search_list = self.get_search_keywords_pop()
            self.select_menu_pop()
        # self.translate_review_in_detail_page()
        # asyncio.run(self.check_image_in_detail_page())
        # self.check_image_in_detail_page()
        # self.check_reviews_count_in_detail_page()
        # self.add_cart_in_detail_page_pop()
        # self.into_reviews_page()
        # self.sort_in_reviews_page()
        # # # self.search_pop('car')
        # # self.into_detail_page_pop()
        # # self.check_image_in_detail_page()
        # self.open_signin_page_pop()
        # # # account = self.random_info('email')
        # if self.login_pop('305594246@qq.com', '123456'):
        #     self.add_wishlist()
        #     self.FAQ()
        #     if self.open_cart_pop():
        #         self.checkout_pop()
        #         can_pay_status = True
        #         self.switch_delivery_type()
        #         if not self.judge_address_pop():
        #             zipcode = self.get_site_zip("uk")
        #             can_pay_status = self.add_address_book_pop(zip=zipcode)
        #         self.checkout_pop()
        #         if can_pay_status:
        #             self.switch_pay_methods_pop()
        #             return True
        # #     self.search_pop('car')
        # #     if self.into_detail_page_pop():
        #     self.FAQ()
        #     self.close_alart()
        # self.check_image_in_detail_page()
        dt = time.time()
        print(dt - st)

    def single_loop_test_pop(self, site='ie', site_dict={}):
        url = site_dict[site]
        self.current_site = site
        self.have_close_current_site_cookie = False
        if self.get_page(url):
            # self.close_cookie()
            self.close_ad()
            self.close_cookie()
            if self.swipe_banner(5):
                self.open_banner()
            for i in range(3):
                current_url = self.browser.current_url
                if '/category' not in current_url:
                    self.logger.info("Not in category page, reselect menu.")
                    self.open_cates_pop()
                    # search_list = self.get_search_keywords_pop()
                    self.select_menu_pop()
                    continue
                break
            if self.into_detail_page_pop():
                self.check_image_in_detail_page()
                self.add_cart_in_detail_page_pop(False)
                self.check_reviews_count_in_detail_page()
                if self.into_reviews_page():
                    self.sort_in_reviews_page()
            # self.add_cart_pop()
            search_name = self.random_info('shop')
            self.search_pop(search_name)
            self.open_signin_page_pop()
            account = self.random_info('email')
            if self.login_pop(account, '123456'):
                if self.into_detail_page_pop():
                    self.check_image_in_detail_page()
                    self.check_reviews_count_in_detail_page()
                    self.add_wishlist()
                    self.add_cart_in_detail_page_pop(True)
                    self.FAQ()
                    if self.switch_product_pop():
                        self.check_image_in_detail_page()
                        self.check_reviews_count_in_detail_page()
                        self.add_cart_in_detail_page_pop(True)
                if self.open_cart_pop():
                    self.select_discount_pop()
                    self.checkout_pop()
                    can_pay_status = True
                    self.switch_delivery_type()
                    if not self.judge_address_pop():
                        zipcode = self.get_site_zip(site)
                        can_pay_status = self.add_address_book_pop(zip=zipcode)
                    self.checkout_pop()
                    if can_pay_status:
                        self.switch_pay_methods_pop()
                        return True
                    return False
                return True  # 购物车为空不判定为fail
            return False
                    # self.input_credit_card_pop()
                    # self.place_order_pop()


if __name__ == '__main__':
    test = H5_test('POP_H5_TEST')
    # test.part_test()
    # test.send_warning_message()
    test.single_loop_test_pop('us', {'us': 'www.aosom.com'})
    # test.switch_pic()
