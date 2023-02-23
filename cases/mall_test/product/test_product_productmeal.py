import json
import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false, check_list_value
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.feature("产品模块 - 产品套餐")
class TestProductOps:
    @allure.story("根据产品套餐编码获取产品套餐详情")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_product_meal(self):
        with allure.step("调用【根据产品套餐编码获取产品套餐详情】接口"):
            req_source = 'H5'
            req_product_list = ["HYQGCSTC001"]
            response = gbl.productObj.get_product_meal(source=req_source, product_list=req_product_list)
            data = response['data'][0]
            res_mealName = data['mealName']
            res_sourceCode = data['sourceCode']
            res_tagCode = data['tagCode']
            res_skuids = data['skuids']
            res_productVos = data['productVos'][0]['skuid']
            check_value_true('杭研全国测试套餐', res_mealName)
            check_value_true('HYQGCSTC001', res_sourceCode)
            check_value_true('HY_QG_CS001', res_tagCode)
            check_value_false('', res_skuids)
            check_value_false('', res_productVos)