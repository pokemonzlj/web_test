# -*- coding: utf-8 -*-
import sys

from typing import List
from Tea.core import TeaCore
#import json

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Message:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # AccessKey ID,
            access_key_id=access_key_id,
            # AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def send_error_message(numberlist=[], *args
        #*args: List[str],
    ) -> None:
        client = Message.create_client('LLLLLLLLLLLL', 'eEEEEEEEEE')
        # add_sms_template_request = dysmsapi_20170525_models.AddSmsTemplateRequest(
        #     template_type=1,
        #     template_name='执行报错',
        #     template_content='${name}模块执行异常',
        #     remark='报错反馈'
        # )
        # templatecode=add_sms_template_request["TemplateCode"]
        # client.add_sms_template(add_sms_template_request)
        # {
        #     "TemplateCode": "SMS_222275060",
        #     "Message": "OK",
        #     "RequestId": "233B147A-02B8-5943-B72D-97CC555C02E9",
        #     "Code": "OK"
        # }
        #签名
        # {
        #     "RequestId": "E7CA9068-D63C-5094-AE00-31EC0861EED4",
        #     "Message": "OK",
        #     "Code": "OK",
        #     "SignName": "朱哥"
        # }
        number_string = ''
        if numberlist:
            number_string=','.join(numberlist)
        message_info_dict={}
        message_info_dict['site_name'] = args[0]
        message_info_dict['module_name'] = args[1]
        message_info_dict['info'] = args[2]
        print(message_info_dict)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(phone_numbers=number_string, sign_name="遨森官网", template_code="SMS_222325107", template_param='%s'%message_info_dict)
        resp = client.send_sms(send_sms_request)
        # query_send_details_request = dysmsapi_20170525_models.QuerySendDetailsRequest(
        #     send_date='20210813',
        #     phone_number='15258177104',
        #     page_size=1,
        #     current_page=1
        # )
        # # 复制代码运行请自行打印 API 的返回值
        # client.query_send_details(query_send_details_request)
        #if "'Message': 'OK'" in resp:  #TypeError: argument of type 'SendSmsResponse' is not iterable
        if resp.body.message == 'OK':
            print("SMS send succeed!")
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    def send_notification_message(numberlist=[], *args
        #*args: List[str],
    ) -> None:
        client = Message.create_client('LLLLLLLLLLLL', 'eEEEEEEEEE')
        # add_sms_template_request = dysmsapi_20170525_models.AddSmsTemplateRequest(
        number_string = ''
        if numberlist:
            number_string=','.join(numberlist)
        message_info_dict={}
        message_info_dict['time'] = args[0]
        message_info_dict['total_site_count'] = args[1]
        message_info_dict['error_site_list'] = args[2]
        message_info_dict['today_weather'] = args[3]
        print(message_info_dict)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(phone_numbers=number_string, sign_name="遨森官网", template_code="SMS_244835067", template_param='%s'%message_info_dict)
        resp = client.send_sms(send_sms_request)
        # query_send_details_request = dysmsapi_20170525_models.QuerySendDetailsRequest(
        #     send_date='20210813',
        #     phone_number='15258177104',
        #     page_size=1,
        #     current_page=1
        # )
        # # 复制代码运行请自行打印 API 的返回值
        # client.query_send_details(query_send_details_request)
        #if "'Message': 'OK'" in resp:  #TypeError: argument of type 'SendSmsResponse' is not iterable
         #{'Message': 'OK', 'RequestId': 'FDFD49A6-1433-5512-B7E4-BC1FBC6E4DAD', 'Code': 'OK', 'BizId': '183503846890820055^0'} 返回是个Json格式
        result=resp.body   #类型<class 'alibabacloud_dysmsapi20170525.models.SendSmsResponseBody'>
        if result.message == 'OK':  #TypeError: 'SendSmsResponseBody' object is not subscriptable 返回是个Json格式
            print("SMS send succeed!")
        # if "'Message': 'OK'" in resp.body:
        #     print("SMS send succeed!")
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    async def send_error_message_async(   #在3.5过后，我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器，异步就可以在请求之后不一定要死等，而是可以做其他事情。
        args: List[str],
    ) -> None:
        message_info_dict = {}
        message_info_dict['site_name'] = args[0]
        message_info_dict['module_name'] = args[1]
        message_info_dict['info'] = args[2]
        client = Message.create_client('LLLLLLLLLLLL', 'eEEEEEEEEE')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(phone_numbers='158688028611', sign_name="遨森官网", template_code="SMS_222325107", template_param='%s'%message_info_dict)
        resp = await client.send_sms_async(send_sms_request)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    # Sample.main(sys.argv[1:])
    # Message.send_error_message(['158688028611'], 'US', '登陆', '点击登陆无响应')
    Message.send_notification_message(['111111111111'], '2022-03-10', 15, ['IE','FR'])
