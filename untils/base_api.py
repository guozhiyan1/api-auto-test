import requests
import json
from time import time, sleep
from untils.log_helper import logger


# 定义一个common的类，它的父类是object
class BaseApi(object):
    # common的构造函数
    def __init__(self, url_root):
        # 被测系统的跟路由
        self.url_root = url_root

    # 封装你自己的get请求，uri是访问路由，params是get请求的参数，如果没有默认为空
    def get(self, url, params='', headers=None, content=None):
        # 请求地址拼接：域名+接口地址
        url = self.url_root + url

        # 通过get请求访问对应地址
        requests.packages.urllib3.disable_warnings()

        # 请求地址
        start = time()  # 记录执行时间
        res = requests.get(url, params=params, headers=headers, verify=False)
        response = res.json()
        end = time()  # 记录执行完成时间

        # 打印日志
        logger().info(f"{'-' * 100}")
        logger().warning(f"接口名称：{content}，请求时间：{end - start}秒")
        logger().info(f"接口地址：{url}")
        logger().info(f"请求参数：{params}")
        logger().info(f"请求响应：{response}")

        # 接口发生异常，无msg字段，捕获打印接口返回
        try:
            code = response['code']
            repeatCode = "200"
            if repeatCode == code:
                sleep(10)
                res = requests.get(url, data=params, headers=headers)
                response = res.json()
                logger().info(f"请求响应：{response}")
        except:
            logger().error(f"请求响应：{response}")

        return response

    # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
    def post(self, url, params='', headers=None, content=None):
        # 请求地址拼接：域名+接口地址
        url = self.url_root + url

        # 获取请求头类型
        try:
            content_type = headers['Content-Type']
            if 'json' in content_type:
                params = json.dumps(params)
        except:
            pass

        # 如果是json，那么通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
        # 返回request的Response结果，类型为requests的Response类型
        requests.packages.urllib3.disable_warnings()

        # 请求地址
        start = time()  # 记录执行时间
        res = requests.post(url, data=params, headers=headers)
        response = res.json()
        end = time()  # 记录执行完成时间

        # 打印日志
        logger().info(f"{'=' * 100}")
        logger().warning(f"接口名称：{content}，请求时间：{end - start}秒")
        logger().info(f"接口地址：{url}")
        logger().info(f"请求参数：{params}")
        logger().info(f"请求响应：{response}")

        # 接口发生异常，无msg字段，捕获打印接口返回
        try:
            msg = response['message']
            repeatMsg = "重复提交，请稍后再试"
            if repeatMsg == msg:
                sleep(10)
                res = requests.post(url, data=params, headers=headers)
                response = res.json()
                logger().info(f"请求响应：{response}")
        except:
            logger().error(f"请求响应：{response}")
        return response
