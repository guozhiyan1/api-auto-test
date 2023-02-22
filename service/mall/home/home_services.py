from untils.base_api import BaseApi
from untils.common_method import check_response


class HomeClass:

    def __init__(self, domain, token=''):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json",
            "X-user-token": token
        }

    def get_auth_productList(self, address_code='9122', source='H5'):
        # 接口地址
        url = '/app/home/v1.0.0/get_auth_productList'
        params = {
            "addressCode": address_code,
            "prodCode": None,
            "source": source
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="授权产品列表")

        return check_response(response)
