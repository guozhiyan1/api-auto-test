from untils.base_api import BaseApi
from untils.common_method import check_response
import untils.db_tool


class UserClass:

    def __init__(self, domain):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json"
        }

    def auth_login(self, source='Large', merchant_code='hy', address_code=9120, phone_no='13666621484'):
        # 接口地址
        url = '/app/user/v1.0.0/auth_login'
        params = {
            "source": source,
            "merchantCode": merchant_code,
            "addressCode": address_code,
            "authCode": "3f98becde6d24ed7ba0e133ca558e5f9",
            "mockPhoneNo": phone_no
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="授权登录")

        return check_response(response)