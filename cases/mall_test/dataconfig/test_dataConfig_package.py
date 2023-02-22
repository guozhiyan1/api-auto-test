import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.epic("配置模块 - APK包")
@allure.feature("配置模块 - APK包")
class TestDataConfigPackage:
    @allure.story("根据包名获取apk信息")
    @allure.title("根据包名获取apk信息")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_apkinfo(self):
        with allure.step("调用【根据包名获取apk信息】接口"):
            req_name = 'com.wy.wykj.ydcn'
            response = gbl.dataConfigObj.get_apkinfo(name='com.wy.wykj.ydcn')
            data = response['data']
            res_name = data['name']
            res_video_name = data['videoCategoryList'][0]['videoName']
            res_ops_name = data['opsVos'][0]['opsName']
            check_value_true(req_name, res_name)
            check_value_false('', res_video_name)
            check_value_false('', res_ops_name)

    @allure.story("获取菜单配置")
    @allure.title("获取菜单配置")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_apkinfo(self):
        with allure.step("调用【获取菜单配置】接口"):
            req_merchant_code = 'yd'
            req_base_address_ref = 'CN'
            response = gbl.dataConfigObj.menu_config(merchant_code=req_merchant_code, base_address_ref=req_base_address_ref)
            data = response['data']
            res_merchant_code = data['merchantCode']
            res_base_address_ref = data['baseAddressRef']
            res_template_code = data['templateCode']
            check_value_true(req_merchant_code, res_merchant_code)
            check_value_true(req_base_address_ref, res_base_address_ref)
            check_value_true('template1', res_template_code)
