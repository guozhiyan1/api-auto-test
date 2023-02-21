from untils.base_api import BaseApi
from untils.common_method import check_response


class TrackingClass:

    def __init__(self, domain, token=''):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json",
            "X-user-token": token
        }

    def tracking_add(self, source='H5', channel='hy', event_key='event_open_default', device_name='', trace_id=''):
        # 接口地址
        url = '/app/tracking_ntrenventtrackingrecord/v1.0.0/add'
        params = {
            "traceId": trace_id,
            "source": source,
            "deviceName": device_name,
            "browserName": "",
            "channel": channel,
            "eventKey": event_key,
            "url": "http://121.41.220.186:9998/#/refresh?path=%2Fhome",
            "referUrl": "http://121.41.220.186:9998/#/"
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="新增埋点")

        return check_response(response)
