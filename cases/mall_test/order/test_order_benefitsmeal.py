import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false, check_list_value
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.epic("订单模块-权益套餐包")
@allure.feature("订单模块-权益套餐包")
class TestOrderBenefitsMeal:
    @allure.story("根据产品编码获取套餐包")
    @allure.title("根据产品编码获取套餐包")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_benefits_meal(self):
        with allure.step("调用【根据产品编码获取套餐包】接口"):
            req_address_code = '9122'
            req_merchant_code = 'hy'
            req_prod_code = 'HYQGCSTC001'
            req_source = 'H5'
            response = gbl.orderObj.get_benefits_meal(address_code=req_address_code, merchant_code=req_merchant_code, source=req_source, prod_code=req_prod_code)
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

    @allure.story("获取权益跳转url")
    @allure.title("获取权益跳转url")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_benefits_target_url(self):
        with allure.step("调用【获取权益跳转url】接口"):
            req_address_code = '9122'
            req_merchant_code = 'hy'
            req_prod_code = 'HYQGCSTC001'
            req_source = 'H5'
            req_card_no = '693222865738268680'
            req_skuid = 'weiyi005'
            response = gbl.orderObj.get_benefits_target_url(address_code=req_address_code, merchant_code=req_merchant_code, source=req_source, card_no=req_card_no,
                                                            skuid=req_skuid, prod_code=req_prod_code)
            data = response['data']
            check_value_false('', data)

    @allure.story("获取门户权益落地页")
    @allure.title("获取门户权益落地页")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_portal_benefits_url(self):
        with allure.step("调用【获取门户权益落地页】接口"):
            req_address_code = '9122'
            req_merchant_code = 'hy'
            req_prod_code = 'HYQGCSTC001'
            req_source = 'H5'
            req_card_no = '693222865738268680'
            req_skuid = 'weiyi005'
            response = gbl.orderObj.get_portal_benefits_url(address_code=req_address_code, merchant_code=req_merchant_code, source=req_source, card_no=req_card_no,
                                                            skuid=req_skuid, prod_code=req_prod_code)
            data = response['data']
            check_value_false('', data)
