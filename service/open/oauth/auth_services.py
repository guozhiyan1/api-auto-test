from untils.base_api import BaseApi
from untils.common_method import check_response
import untils.db_tool


class OAuthClass:

    def __init__(self, domain, authorization=''):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": authorization
        }

    def get_oauth_token(self):
        """
        获取accessToken
        :return:
        """
        # 接口地址
        url = '/app/auth/v1.0.0/oauth/token'
        params = {
            "grantType": "client_credentials",
            "clientId": "1608739200",
            "clientSecret": "test20201224"
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="获取accessToken")

        return check_response(response)

    def get_oauth_refresh(self, token):
        """
        refreshToken刷新accessToken
        :param token:
        :return:
        """
        # 接口地址
        url = '/app/auth/v1.0.0/oauth/refresh'
        params = {
            "refreshToken": token
        }
        # 请求地址
        response = self.common.get(url, params=params, headers=self.headers, content="refreshToken刷新accessToken")

        return check_response(response)

    def auth_benefit_add(self, productId, userId, phone, status, orderId):
        """
        预分配权益-杭研
        :param productId:
        :param userId:
        :param phone:
        :param status: 1-开通，2-退订
        :param orderId:
        :return:
        :return:
        """
        # 接口地址
        url = '/app/auth/v1.0.0/benefit/add'
        params = {
            "productId": productId,
            "userId": userId,
            "phone": phone,
            "status": status,
            "timestamp": "1638523804",
            "orderId": orderId
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="预分配权益-杭研")

        return check_response(response)
