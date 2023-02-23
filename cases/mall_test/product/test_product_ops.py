import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false, check_list_value
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.feature("产品模块 - 运营位")
class TestProductOps:
    @allure.story("获取运营位集合")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_ops_list(self):
        with allure.step("调用【获取运营位集合】接口"):
            req_code = 'h5_platform'
            req_source = 'H5'
            response = gbl.productObj.get_ops_list(code=req_code, source=req_source)
            data = response['data']
            assert_data_list = [{'opsName': '全部服务', 'sortno': 10, 'url': 'h5_platform'},
                                {'opsName': '医学百科', 'sortno': 9, 'url': 'service017'},
                                {'opsName': '疾病库', 'sortno': 8, 'url': 'service014'},
                                {'opsName': '健康测评', 'sortno': 7, 'url': 'service012'},
                                {'opsName': '就医陪同', 'sortno': 6, 'url': 'service021'},
                                {'opsName': 'AI导诊', 'sortno': 5, 'url': 'service033'},
                                {'opsName': '重疾绿通', 'sortno': 4, 'url': 'service010'},
                                {'opsName': '公立体检', 'sortno': 3, 'url': 'service999'},
                                {'opsName': '开药问诊', 'sortno': 2, 'url': 'service002'},
                                {'opsName': '私人医生', 'sortno': 1, 'url': 'service019'}]
            check_list_value(assert_data_list, data, 'opsName')
            check_list_value(assert_data_list, data, 'sortno')
            check_list_value(assert_data_list, data, 'url')
