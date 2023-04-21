# -*- coding: utf-8 -*-
import time

from H5_control import H5_test
import requests
import json
import traceback
import sys


class do_test(H5_test):

    def total_test_pop(self, wait_time='6'):
        while True:
            if self.check_time('6') or self.check_time('12') or self.check_time('19'):
                # logger= self.createlogger('POP_H5_TEST')
                # sys.stdout = self.output_print
                site_dict = self.get_site_dict()
                total_site_count = len(site_dict)
                error_site_list = []
                if self.set_up('https://www.aosom.co.uk/', 'h5'):
                    for site in site_dict:
                        try:
                            start_time = time.time()
                            if self.single_loop_test_pop(site, site_dict) == False:
                                error_site_list.append(site)
                            end_time = time.time()
                            duration_time = end_time - start_time
                            print("%s站执行时间为:%s秒" % (site, duration_time))
                        except Exception as e:
                            print(e)
                            traceback.print_exc()
                            self.logger.warning("%s站发生了预期之外的错误，截图并跳过" % site)
                            self.screenshot(self.browser, "%s_unexpected_error" % site)
                            error_site_list.append(site)
                        # self.delete_account("123456")
                    self.close()
                    if error_site_list == []:
                        error_site_list = '没有'
                    self.logger.info("%s站发生了奇奇怪怪的错误." % error_site_list)
                    day = self.get_current_date()
                    if error_site_list:
                        self.send_finish_message(day, total_site_count, error_site_list)
                    # self.delay(72000)
                self.delay(10800)   #无论执没执行，都要等待
            else:
                self.delay(1800)
                # 每半个小时判定一次


if __name__ == '__main__':
    test = do_test('POP_H5_TEST')
    # sys.stdout = test.output_print
    test.total_test_pop('9')
    # test.total_step_test1()
