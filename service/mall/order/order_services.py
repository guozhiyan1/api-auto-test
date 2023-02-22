from untils.base_api import BaseApi
from untils.common_method import check_response


class OrderClass:

    def __init__(self, domain, token=''):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json",
            "X-user-token": token
        }

    def get_benefits_meal(self, address_code='9122', merchant_code='hy', source='H5', prod_code=''):
        # 接口地址
        url = '/app/order_benefitsmeal/v1.0.0/get_benefits_meal'
        params = {
            "addressCode": address_code,
            "merchantCode": merchant_code,
            "prodCode": prod_code,
            "source": source
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="根据产品编码获取套餐包")

        return check_response(response)

    def get_benefits_target_url(self, address_code='9122', merchant_code='hy', source='H5', card_no='', skuid='', prod_code='HYQGCSTC001'):
        # 接口地址
        url = '/app/order_benefitsmeal/v1.0.0/get_benefits_target_url'
        params = {
            "addressCode": address_code,
            "merchantCode": merchant_code,
            "prodCode": prod_code,
            "source": source,
            "cardNo": card_no,
            "skuid": skuid
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="获取权益跳转url")

        return check_response(response)

    def get_portal_benefits_url(self, address_code='9122', merchant_code='hy', source='H5', card_no='', skuid='', prod_code='HYQGCSTC001'):
        # 接口地址
        url = '/app/order_benefitsmeal/v1.0.0/get_portal_benefits_url'
        params = {
            "addressCode": address_code,
            "merchantCode": merchant_code,
            "prodCode": prod_code,
            "source": source,
            "cardNo": card_no,
            "skuid": skuid
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="获取门户权益落地页")

        return check_response(response)
