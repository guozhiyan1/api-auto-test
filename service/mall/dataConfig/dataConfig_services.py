from untils.base_api import BaseApi
from untils.common_method import check_response


class DataConfigClass:

    def __init__(self, domain, token=''):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json",
            "X-user-token": token
        }

    def get_apkinfo(self, name='com.wy.wykj.ydcn'):
        # 接口地址
        url = '/app/dataconfig_package/v1.0.0/get_apkinfo'
        params = {
            "name": name
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="根据包名获取apk信息")

        return check_response(response)

    def menu_config(self, merchant_code='yd', base_address_ref='CN', isInject='1'):
        # 接口地址
        url = '/app/dataconfig_package/v1.0.0/menu_config'
        params = {
            "merchantCode": merchant_code,
            "baseAddressRef": base_address_ref,
            "isInject": isInject
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="根据包名获取apk信息")

        return check_response(response)
