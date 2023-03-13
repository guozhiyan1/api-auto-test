import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.feature("权限模块-OAuth")
class TestOAuth:
    @allure.story("获取accessToken")
    @pytest.mark.test
    @pytest.mark.p0
    def test_oauth_token(self):
        with allure.step("调用【获取accessToken】接口"):
            response = gbl.oauthObj.get_oauth_token()
            data = response['data']['accessToken']
            check_value_false('', data)

    @allure.story("refreshToken刷新accessToken")
    @pytest.mark.test
    @pytest.mark.p0
    def test_oauth_refresh(self):
        with allure.step("调用【refreshToken刷新accessToken】接口"):
            accessToken = 'B8EB823AF7819154F1BD64950DA557C9'
            response = gbl.oauthObj.get_oauth_refresh(token=accessToken)
            data = response['data']['accessToken']
            check_value_false(accessToken, data)
