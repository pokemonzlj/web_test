# -*- coding: utf-8 -*-
import sys

from typing import List
from Tea.core import TeaCore

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
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
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('LLLLLLLLLLLL', 'eEEEEEEEEEEEEee')
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
        message_info_dict={}
        message_info_dict['site_name'] = args[0]
        message_info_dict['module_name'] = args[1]
        message_info_dict['info'] = args[2]
        print(message_info_dict)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(phone_numbers='111111111', sign_name="官网", template_code="SMS_222325107", template_param='%s'%message_info_dict)
        resp = client.send_sms(send_sms_request)
        # query_send_details_request = dysmsapi_20170525_models.QuerySendDetailsRequest(
        #     send_date='20210813',
        #     phone_number='111111111',
        #     page_size=1,
        #     current_page=1
        # )
        # # 复制代码运行请自行打印 API 的返回值
        # client.query_send_details(query_send_details_request)
        print(resp)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    async def main_async(   #在3.5过后，我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器，异步就可以在请求之后不一定要死等，而是可以做其他事情。
        args: List[str],
    ) -> None:
        message_info_dict = {}
        message_info_dict['site_name'] = args[0]
        message_info_dict['module_name'] = args[1]
        message_info_dict['info'] = args[2]
        client = Sample.create_client('LLLLLLLLLLLL', 'eEEEEEEEEEEEEee')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(phone_numbers='11111111', sign_name="官网", template_code="SMS_222325107", template_param='%s'%message_info_dict)
        resp = await client.send_sms_async(send_sms_request)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    # Sample.main(sys.argv[1:])
    Sample.main(['US', '登陆', '点击登陆无响应'])
