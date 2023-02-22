from untils.base_api import BaseApi
from untils.common_method import check_response
import untils.db_tool


class UserClass:

    def __init__(self, domain, token=''):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json",
            "X-user-token": token
        }

    def auth_login(self, source='H5', merchant_code='hy', address_code=9120, phone_no='17700000555'):
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

    def auth_login_cmcc(self, source='H5', chan_code='1608739200', address_code=9125, app_type='yncmcc', phone_no='17700000555'):
        # 接口地址
        url = '/app/user/v1.0.0/auth_login_cmcc'
        params = {
            "source": source,
            "chanCode": chan_code,
            "addressCode": address_code,
            "appType": app_type,
            "authCode": "3f98becde6d24ed7ba0e133ca558e5f9",
            "mockPhoneNo": phone_no
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="授权登录 - 云南和生活")

        return check_response(response)

    def behavior(self, source='H5', user_id=''):
        # 接口地址
        url = '/app/user/v1.0.0/behavior'
        params = {
            "source": source,
            "userid": user_id
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="用户行为")

        return check_response(response)

    def get_user(self, source='H5'):
        # 接口地址
        url = '/app/user/v1.0.0/getUser'
        params = {
            "source": source
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="获取用户信息")

        return check_response(response)

    def sync(self, source='H5'):
        # 接口地址
        url = '/app/user_patient/v1.0.1/sync'
        params = {
            "source": source
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="同步微医云就诊人")

        return check_response(response)
