import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.epic("埋点记录")
@allure.feature("埋点记录")
class TestTracking:
    @allure.story("新增埋点")
    @allure.title("新增埋点")
    @pytest.mark.test
    @pytest.mark.p0
    def test_tracking_add(self):
        with allure.step("前置数据处理"):
            res_user_ref = '221125144616547003993168'
            sql = f"""UPDATE ntr_envent_tracking_record SET delete_flag =1  WHERE user_ref='{res_user_ref}';"""
            updateDBData(gbl.env, 'benefits_test', sql)
        with allure.step("调用【用户行为】接口"):
            req_event_key = 'event_open_default'
            req_device_name = 'api_test'
            req_trace_id = '56d9c760-aa3a-4750-8593-9b98ea9abcfe'
            response = gbl.trackObj.tracking_add(event_key=req_event_key, device_name=req_device_name, trace_id=req_trace_id)
            data = response['data']
            assert 1 == data
        with allure.step("校验埋点表数据"):
            sql = f"""SELECT event_key,`channel`, `source`,trace_id,device_name FROM ntr_envent_tracking_record WHERE user_ref='{res_user_ref}' AND delete_flag=0  ORDER BY create_time DESC LIMIT 1;"""
            res = selectDBData(gbl.env, 'benefits_test', sql)
            data_event_key = res[0][0]
            data_channel = res[0][1]
            data_source = res[0][2]
            data_trace_id = res[0][3]
            data_device_name = res[0][4]
            assert req_event_key == data_event_key
            assert 'hy' == data_channel
            assert 'H5' == data_source
            assert req_trace_id == data_trace_id
            assert req_device_name == data_device_name
