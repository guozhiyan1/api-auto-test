import logging
import time
from datetime import datetime
import pytest
import allure

import module.globals as gbl
from module.open.notify.notify_module import *
from untils.common_method import check_value_true, check_value_false, DateUtil
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.feature("通知模块-问诊")
class TestNotifyConsult:
    @allure.story("数据同步 - 极速图文")
    @pytest.mark.test
    @pytest.mark.p0
    def test_notify_consult_data(self):
        with allure.step("前置数据处理"):
            consult_order_no = '3qzvhku4vm230313173012227'
            phone = '17700000553'
            orderStatus_1 = '3'
            sql = f"""UPDATE nt_consult_order SET delete_flag =1  WHERE consult_order_no='{consult_order_no}' AND ext_order_ref='{phone}';"""
            updateDBData(gbl.env, 'benefits_test', sql)
        with allure.step("同步下单-调用【数据同步 - 极速图文】接口"):
            sign = 'c83df656bca77a865c14630cbeb08c41'
            timestamp = time.time()
            response = gbl.notifyObj.notify_consult_data(sign=sign, timestamp=timestamp, orderStatus=orderStatus_1)
            data = response['data']
            check_value_false('', data)
        with allure.step("校验问诊订单数据"):
            check_consult_order(gbl.env, phone, consult_order_no, orderStatus_1)
        with allure.step("同步状态-调用【数据同步 - 极速图文】接口"):
            sign_2 = '44b442e7b9dd22cc3c194efba94e3437'
            orderStatus_2 = '5'
            timestamp = time.time()
            response = gbl.notifyObj.notify_consult_data(sign=sign_2, timestamp=timestamp, orderStatus=orderStatus_2)
            data = response['data']
            check_value_false('', data)
        with allure.step("校验问诊订单数据"):
            check_consult_order(gbl.env, phone, consult_order_no, orderStatus_2)

    @allure.story("数据同步 - 续约会员卡号")
    @pytest.mark.test
    @pytest.mark.p0
    def test_notify_renewCardno_xk(self):
        with allure.step("前置数据处理"):
            req_cardNo = '700426382588641280'
            req_renewCardNo = '700426382588641281'
            req_start_time = '2023-02-14 11:20:23'
            req_end_time = '2023-03-01 00:00:00'
            sql = f"""UPDATE nt_benefits_meal_detail SET card_no='{req_cardNo}',benefits_start_time='{req_start_time}',benefits_end_time='{req_end_time}',contract_start_time='{req_end_time}' 
             WHERE card_no='{req_renewCardNo}';"""
            updateDBData(gbl.env, 'benefits_test', sql)
        with allure.step("调用【数据同步-续约会员卡号】接口"):
            response = gbl.notifyObj.notify_renewCardno(cardNo=req_cardNo, renewCardNo=req_renewCardNo, renewActionType=1)
            data = response['data']
            check_value_false('', data)
        with allure.step("校验权益业务数据"):
            get_local_time_by0 = DateUtil.get_local_time_by0()
            next_month_start = DateUtil.next_month_start()
            check_benefits_meal_detail_by_xd(gbl.env, cardNo=req_renewCardNo, ben_start_time=get_local_time_by0, ben_end_time=next_month_start,
                                             con_start_time=req_end_time)

    @allure.story("数据同步 - 退订会员卡号")
    @pytest.mark.test
    @pytest.mark.p0
    def test_notify_renewCardno_td(self):
        with allure.step("前置数据处理"):
            req_cardNo = '700453790129717253'
            sql = f"""UPDATE nt_benefits_meal_detail SET card_no='{req_cardNo}',status=0 WHERE card_no='{req_cardNo}';"""
            updateDBData(gbl.env, 'benefits_test', sql)
        with allure.step("调用【数据同步-退订会员卡号】接口"):
            response = gbl.notifyObj.notify_renewCardno(cardNo='700453790129717253', renewCardNo='', renewActionType=2)
            data = response['data']
            check_value_false('', data)
        with allure.step("调用【数据同步-退订会员卡号】接口"):
            check_benefits_meal_detail_by_td(gbl.env, cardNo=req_cardNo)
