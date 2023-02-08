import pytest
import allure

import module.globals as gbl
from untils.db_tool import selectDBData


@allure.epic("用户模块")
@allure.feature("用户")
class TestUser:
    @allure.story("授权登录")
    @allure.title("授权登录")
    @pytest.mark.test
    def test_user_auth_login(self):
        with allure.step("授权登录"):
            response = gbl.userObj.auth_login(phone_no='13666621484')
            data = response['data']
            assert '' != data

    @allure.story("查询用户表")
    @allure.title("查询用户表")
    @pytest.mark.test
    def test_select_user_db(self):
        with allure.step("查询用户表"):
            sql = f"""SELECT user_id,phone_no FROM nu_user WHERE phone_no='13666621484' AND delete_flag=0;"""
            res = selectDBData(gbl.env, 'benefits_test', sql)
            db_user_id = res[0][0]
            phone_no = res[0][1]
            assert '211219095047000001001' == db_user_id
            assert '13666621484' == phone_no
