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


@allure.feature("产品模块 - 视频")
class TestProductOps:
    @allure.story("根据类目获取视频列表")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_product_meal(self):
        with allure.step("调用【根据类目获取视频列表】接口"):
            req_baseAddressRef = 'CN'
            req_categoryRef = '1'
            req_merchantCode = 'yd'
            response = gbl.productObj.get_video_list(baseAddressRef=req_baseAddressRef, categoryRef=req_categoryRef, merchantCode=req_merchantCode)
            data = response['data']['resultData'][0]
            res_id = data['id']
            res_title = data['title']
            res_categoryRef = data['categoryRef']
            res_titleCapital = data['titleCapital']
            res_imgUrl = data['imgUrl']
            res_playAmount = data['playAmount']
            check_value_true('CN009', res_id)
            check_value_true('去妇科看病，碰到男医生怎么办？', res_title)
            check_value_true('1', res_categoryRef)
            check_value_true('QFKKB，PDNYSZMB？', res_titleCapital)
            check_value_false('', res_imgUrl)
            check_value_false(0, res_playAmount)

    @allure.story("根据视频ID获取视频详情")
    @pytest.mark.test
    @pytest.mark.p0
    def test_get_product_meal(self):
        with allure.step("调用【根据视频ID获取视频详情】接口"):
            req_baseAddressRef = 'CN'
            req_videoRef = 'CN009'
            req_merchantCode = 'yd'
            response = gbl.productObj.get_video_detail(baseAddressRef=req_baseAddressRef, videoRef=req_videoRef, merchantCode=req_merchantCode)
            data = response['data']
            res_videoRef = data['videoRef']
            res_title = data['title']
            res_titleCapital = data['titleCapital']
            res_introduce = data['introduce']
            res_videoUrl = data['videoUrl']
            res_labels = data['labels'][0]
            check_value_true(req_videoRef, res_videoRef)
            check_value_true('去妇科看病，碰到男医生怎么办？', res_title)
            check_value_true('QFKKB，PDNYSZMB？', res_titleCapital)
            check_value_false('', res_introduce)
            check_value_false('', res_videoUrl)
            check_value_false('', res_labels)
