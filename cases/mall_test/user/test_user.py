import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.epic("用户模块")
@allure.feature("用户")
class TestUser:
    @allure.story("授权登录")
    @allure.title("授权登录")
    @pytest.mark.test
    @pytest.mark.p0
    def test_auth_login(self):
        with allure.step("调用【授权登录】接口"):
            response = gbl.userObj.auth_login()
            data = response['data']
            assert '' != data

    @allure.story("授权登录 - 云南和生活")
    @allure.title("授权登录 - 云南和生活")
    @pytest.mark.test
    @pytest.mark.p0
    def test_auth_login_cmcc(self):
        with allure.step("调用【授权登录 - 云南和生活】接口"):
            response = gbl.userObj.auth_login_cmcc()
            data = response['data']
            assert '' != data

    @allure.story("用户行为")
    @allure.title("用户行为")
    @pytest.mark.test
    @pytest.mark.p0
    def test_behavior(self):
        with allure.step("前置数据处理"):
            sql = f"""UPDATE nu_behavior SET delete_flag =1  WHERE source='H5' AND user_ref='221125144616547003993168';"""
            updateDBData(gbl.env, 'benefits_test', sql)
        with allure.step("调用【用户行为】接口"):
            response = gbl.userObj.behavior(user_id='221125144616547003993168')
            data = response['data']
            assert 1 == data
        with allure.step("校验行为表数据"):
            sql = f"""SELECT behavior_type FROM nu_behavior WHERE source='H5' AND user_ref='221125144616547003993168' AND 
            delete_flag=0  ORDER BY create_time DESC LIMIT 1;"""
            res = selectDBData(gbl.env, 'benefits_test', sql)
            behavior_type = res[0][0]
            assert '1' == behavior_type

    @allure.story("获取用户信息")
    @allure.title("获取用户信息")
    @pytest.mark.test
    @pytest.mark.p0
    def test_getUser(self):
        with allure.step("调用【获取用户信息】接口"):
            response = gbl.userObj.get_user()
            data = response['data']
            res_phone_no = data["phoneNo"]
            res_phone_no_mask = data["phoneNoMask"]
            assert '17700000555' == res_phone_no
            assert '177****0555' == res_phone_no_mask
