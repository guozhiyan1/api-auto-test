import logging
import time
from datetime import datetime

import pytest
import allure

import module.globals as gbl
from untils.common_method import check_value_true, check_value_false
from untils.db_tool import selectDBData
from untils.db_tool import updateDBData


@allure.feature("权限模块-权益")
class TestOAuth:
    @allure.story("预分配权益-杭研-开通权益")
    @pytest.mark.test
    @pytest.mark.p0
    def test_benefitAdd_openBenefits(self):
        with allure.step("前置数据处理"):
            productId = 'YNJKZXB100071'
            phone = '17700000553'
            sql = f"""UPDATE nt_benefits_pre SET delete_flag =1  WHERE source_code='{productId}' AND phone_no='{phone}';"""
            updateDBData(gbl.env, 'benefits_test', sql)
        with allure.step("调用【预分配权益-杭研】接口"):
            response = gbl.oauthObj.auth_benefit_add(productId=productId, phone=phone, orderId=phone, userId=phone, status=1)
            data = response['data']
        with allure.step("查询预分配结果数据"):
            time.sleep(1)
            sql = f"""SELECT merchant_code,phone_no,ext_user_ref,ext_order_ref,source_code,prod_code,order_create_time,
            benefits_start_time,contract_start_time,contract_end_time,broadband_account FROM benefits_test.nt_benefits_pre t 
            WHERE phone_no = '17700000553' AND status = '0' AND delete_flag='0' ORDER BY create_time desc;"""
            res = selectDBData(gbl.env, 'benefits_test', sql)
            db_merchant_code = res[0][0]
            db_phone_no = res[0][1]
            db_ext_user_ref = res[0][2]
            db_ext_order_ref = res[0][3]
            db_source_code = res[0][4]
            db_prod_code = res[0][5]
            db_contract_end_time = res[0][9]
            db_broadband_account = res[0][10]
            check_value_true('hy', db_merchant_code)
            check_value_true(phone, db_phone_no)
            check_value_true(phone, db_ext_user_ref)
            check_value_true(phone, db_ext_order_ref)
            check_value_true(productId, db_source_code)
            check_value_true(productId, db_prod_code)
            check_value_true(productId, db_prod_code)
            check_value_true('None', str(db_contract_end_time))
            check_value_true(phone, db_broadband_account)
