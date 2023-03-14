from untils.base_api import BaseApi
from untils.common_method import check_response


class NotifyClass:

    def __init__(self, domain):
        # 基础变量
        self.common = BaseApi(domain)
        self.headers = {
            "Content-Type": "application/json"
        }

    def notify_consult_data(self, sign, timestamp, orderStatus):
        """
        数据同步 - 极速图文
        :return:
        """
        # 接口地址
        url = f'/app/notify_consult/v1.0.0/data?sign={sign}&&timestamp={timestamp}'
        params = {
            "consultType": 9,
            "deductId": "700164787073581062",
            "endTime": "",
            "orderKey": "3qzvhku4vm230313173012227",
            "orderStatus": orderStatus,
            "patientCertNo": "330183199105200310",
            "patientId": "123124459260",
            "patientMobile": "17700000553",
            "patientName": "许宏霞",
            "sceneCode": "weiyi_consult",
            "startTime": "2023-03-13 16:57:52",
            "subjectCode": "wy01.01.52.WwRPX1pb",
            "tagCode": "HY_QG_CS001",
            "userId": "221214190718131001384667",
            "yuFenZhen": "0"
        }
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="数据同步 - 极速图文")

        return check_response(response)

    def notify_renewCardno(self, cardNo, renewCardNo, renewActionType):
        """
        数据同步-续约/退订会员卡号
        :return:
        """
        # 接口地址
        url = '/app/notify_renewCardno/v1.0.0/data'

        if renewActionType == 1:
            params = {"cardRenewItemList": [{
                "cardNo": cardNo,
                "renewActionType": 1,
                "renewCardNo": renewCardNo
            }]}
        else:
            params = {"cardRenewItemList": [{
                "cardNo": cardNo,
                "renewActionType": 2
            }]}
        # 请求地址
        response = self.common.post(url, params=params, headers=self.headers, content="数据同步-续约/退订会员卡号")

        return check_response(response)
