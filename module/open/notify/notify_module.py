import time

from untils.common_method import check_value_true
from untils.db_tool import selectDBData


def check_consult_order(env, phone, consult_order_no, orderStatus):
    """
    校验问诊订单
    :param env: 环境标识
    :param phone: 手机号
    :param consult_order_no: 问诊订单号
    :return:
    """
    time.sleep(1)
    sql = f"""SELECT benefits_pre_ref,benefits_meal_detail_ref,skuid,card_no,patient_name,prod_code,tag_code,busi_type,benefits_type,consult_status
                  FROM nt_consult_order WHERE ext_order_ref='{phone}' and consult_order_no='{consult_order_no}' and delete_flag='0';"""
    res = selectDBData(env, 'benefits_test', sql)
    db_benefits_pre_ref = res[0][0]
    db_benefits_meal_detail_ref = res[0][1]
    db_skuid = res[0][2]
    db_card_no = res[0][3]
    db_patient_name = res[0][4]
    db_prod_code = res[0][5]
    db_tag_code = res[0][6]
    db_busi_type = res[0][7]
    benefits_type = res[0][8]
    db_consult_status = res[0][9]
    check_value_true('230313180034565001993168', db_benefits_pre_ref)
    check_value_true('230313180054425021384667', db_benefits_meal_detail_ref)
    check_value_true('weiyi006', db_skuid)
    check_value_true('700164787073581062', db_card_no)
    check_value_true('许宏霞', db_patient_name)
    check_value_true('HYQGCSTC001', db_prod_code)
    check_value_true('HY_QG_CS001', db_tag_code)
    check_value_true('consult', db_busi_type)
    check_value_true('4', benefits_type)
    check_value_true(orderStatus, db_consult_status)


def check_benefits_meal_detail_by_xd(env, cardNo, ben_start_time, ben_end_time, con_start_time):
    """
    校验业务订单数据
    :param env: 环境标识
    :param cardNo: 套餐卡号
    :param ben_start_time: 权益开始时间
    :param ben_end_time: 权益结束时间
    :param con_start_time: 合同开始时间
    :return:
    """
    time.sleep(1)
    sql = f"""SELECT card_no,benefits_start_time,benefits_end_time,contract_start_time,status
                  FROM nt_benefits_meal_detail WHERE card_no='{cardNo}' and delete_flag='0' LIMIT 1;"""
    res = selectDBData(env, 'benefits_test', sql)
    db_card_no = res[0][0]
    db_benefits_start_time = res[0][1]
    db_benefits_end_time = res[0][2]
    db_contract_start_time = res[0][3]
    db_status = res[0][4]
    check_value_true(cardNo, db_card_no)
    check_value_true(str(ben_start_time), str(db_benefits_start_time))
    check_value_true(str(ben_end_time), str(db_benefits_end_time))
    check_value_true(str(con_start_time), str(db_contract_start_time))
    check_value_true(0, db_status)


def check_benefits_meal_detail_by_td(env, cardNo):
    """
    校验业务订单数据
    :param env: 环境标识
    :param cardNo: 套餐卡号
    :return:
    """
    time.sleep(1)
    sql = f"""SELECT card_no,benefits_start_time,benefits_end_time,contract_start_time,status
                  FROM nt_benefits_meal_detail WHERE card_no='{cardNo}' and delete_flag='0' LIMIT 1;"""
    res = selectDBData(env, 'benefits_test', sql)
    db_card_no = res[0][0]
    db_status = res[0][4]
    check_value_true(cardNo, db_card_no)
    check_value_true(-2, db_status)
