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

    def get_product_meal(self, source='H5', product_list=[]):
        # 接口地址
        url = '/app/product_productmeal/v1.0.0/get_product_meal'
        params = {
            "source": source,
            "productList": product_list
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="根据产品套餐编码获取产品套餐详情")

        return check_response(response)

    def get_video_list(self, baseAddressRef='CN', categoryRef='1', merchantCode='yd'):
        # 接口地址
        url = '/app/product_video/v1.0.0/get_video_list'
        params = {
            "baseAddressRef": baseAddressRef,
            "categoryRef": categoryRef,
            "merchantCode": merchantCode,
            "pageNum": 1,
            "pageSize": 20,
            "source": "Large"
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="根据类目获取视频列表")

        return check_response(response)

    def get_video_detail(self, baseAddressRef='CN', videoRef='', merchantCode='yd'):
        # 接口地址
        url = '/app/product_videodetail/v1.0.0/get_video_detail'
        params = {
            "baseAddressRef": baseAddressRef,
            "videoRef": videoRef,
            "merchantCode": merchantCode
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="根据视频ID获取视频详情")

        return check_response(response)

    def receive_benefits(self, source='H5'):
        # 接口地址
        url = '/app/order_benefits/v1.0.0/receive_benefits'
        params = {
            "source": source
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="领取权益")

        return check_response(response)

    def receive_carno(self, source='H5'):
        # 接口地址
        url = '/app/order_benefits/v1.0.0/receive_carno'
        params = {
            "source": source
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="领取会员卡号")

        return check_response(response)