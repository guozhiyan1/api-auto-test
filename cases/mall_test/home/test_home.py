import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false, check_list_value
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.epic("首页")
@allure.feature("首页")
class TestHome:
    @allure.story("授权产品列表")
    @allure.title("授权产品列表")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_auth_productList(self):
        with allure.step("调用【授权产品列表】接口"):
            req_address_code = '9122'
            req_source = 'H5'
            response = gbl.homeObj.get_auth_productList(address_code=req_address_code, source=req_source)
            data = response['data']
            res_mealName = data['mealName']
            res_sourceCode = data['sourceCode']
            res_goodsName = data['details'][0]['goodsName']
            res_goodsDesc = data['details'][0]['goodsDesc']
            res_skuid = data['details'][0]['skuid']
            res_categoryName = data['details'][0]['categoryName']
            res_cardNo = data['details'][0]['cardNo']
            res_timeLimit = data['details'][0]['timeLimit']
            res_timeRemain = data['details'][0]['timeRemain']
            res_subjectCode = data['details'][0]['subjectCode']
            check_value_true('杭研全国测试套餐', res_mealName)
            check_value_true('HYQGCSTC001', res_sourceCode)
            check_value_false('', res_goodsName)
            check_value_false('', res_goodsDesc)
            check_value_false('', res_skuid)
            check_value_false('', res_categoryName)
            check_value_false('', res_cardNo)
            check_value_false('', res_timeLimit)
            check_value_false('', res_timeRemain)
            check_value_false('', res_subjectCode)
