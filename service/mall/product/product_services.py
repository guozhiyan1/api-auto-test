from untils.base_api import BaseApi
from untils.common_method import check_response


class ProductClass:

    def __init__(self, domain, token=''):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json",
            "X-user-token": token
        }

    def get_ops_list(self, code='h5_platform', source='H5'):
        # 接口地址
        url = '/app/ops/v1.0.0/list'
        params = {
            "code": code,
            "source": source
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="获取运营位集合")

        return check_response(response)
