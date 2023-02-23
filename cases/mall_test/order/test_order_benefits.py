import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false, check_list_value
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.feature("订单模块-权益")
class TestOrderBenefits:
    @allure.story("领取权益")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_benefits_meal(self):
        with allure.step("调用【领取权益】接口"):
            req_source = 'H5'
            response = gbl.productObj.receive_benefits(source=req_source)
            data = response['data']
            check_value_true(1, data)

    @allure.story("领取会员卡号")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_benefits_target_url(self):
        with allure.step("调用【领取会员卡号】接口"):
            req_source = 'H5'
            response = gbl.productObj.receive_carno(source=req_source)
            data = response['data']
            check_value_true(1, data)
