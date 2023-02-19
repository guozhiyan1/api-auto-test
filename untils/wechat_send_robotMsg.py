import logging
import os
from pathlib import Path
import requests
import pandas as pd
import time
import sys

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)
from untils.db_tool import updateDBData

# 机器人key
keyDict = {
    # "test": "e9a62b13-5c43-45ad-ba74-4619be336f12"
    # 调试用
    "test": "e9a62b13-5c43-45ad-ba74-4619be336f121"
}
# 测试联系人
tester_contact = {
    "王勇俊": '13666621484'
}

# 消息接收人
receiverDict = {
    "all": [tester_contact['王勇俊']]
}


# 获取当前时间
def getNowTime():
    TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
    nowtime = time.strftime(TIMEFORMAT, time.localtime(time.time()))
    return nowtime


def get_case_num(filePath):
    """
    获取总用例数和失败用例数
    :param filePath:
    :return:
    """

    # 读取csv
    try:
        df = pd.read_csv(filePath)
    except:
        logging.error(f"{filePath}，不存在")
        raise

    # 计算总数
    failed_total = sum(list(df.FAILED))
    broken_total = sum(list(df.BROKEN))
    passed_total = sum(list(df.PASSED))
    skipped_total = sum(list(df.SKIPPED))
    unknown_total = sum(list(df.UNKNOWN))
    not_pass_total = failed_total + broken_total
    total_case = not_pass_total + passed_total + skipped_total + unknown_total
    # print(f"用例总数：{total_case}，失败用例数：{failed_total}，通过用例数：{passed_total}")

    return total_case, passed_total, not_pass_total


def saveCaseData(project_name, total_case, pass_case, failed_case, pass_rate):
    # 获取当前时间
    nowtime = getNowTime()

    # 执行sql
    sql = f'''INSERT INTO api_auto_data (project_name, total_case, pass_case, failed_case, pass_rate, create_time, update_time, is_deleted) 
    VALUES ('{project_name}', {total_case}, {pass_case}, {failed_case}, '{pass_rate}', '{nowtime}', '{nowtime}', 0)'''
    updateDBData('qa', 'data_test_db', sql)


def sendMsgRobot(project_name, notify_key, pass_rate):
    """
    企业微信机器人发送消息
    :param project_name:
    :param notify_key:
    :return:
    """

    # 报告路径
    allureReport = f"http://47.101.221.124:8080/job/{project_name}/allure/"

    # 消息接收人
    upper_project_name = project_name.lower()
    receiver_key = upper_project_name.split("_")[0]
    try:
        receiver_list = receiverDict[receiver_key]
    except:
        # raise Exception("该工程未维护测试负责人，请维护！")
        logging.info("该工程未维护测试负责人，请维护！")
        receiver_list = ["13666621484"]

    # 消息内容
    msgContent = f"消息类型：API自动化通知\n" \
                 f"工程名：{project_name}\n" \
                 f"脚本情况(成功/失败/总数)：{pass_case}/{failed_case}/{total_case}\n" \
                 f"通过率：{pass_rate}\n" \
                 f"查看详情：{allureReport}\n" \
                 f"执行时间：{getNowTime()}"

    # 消息体
    send_message = {
        "msgtype": "text",  # 消息类型，此时固定为text
        "text": {
            "content": msgContent,  # 文本内容，最长不超过2048个字节，必须是utf8编码
            # "mentioned_list": ["@all"], # userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
            "mentioned_mobile_list": receiver_list  # 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人
        }
    }

    # 请求地址
    key = keyDict[notify_key]
    send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}".format(key)

    # 请求头
    headers = {
        "Content-Type": "text/plain"
    }

    # 机器人发送消息
    logging.info(send_message)
    response = requests.post(url=send_url, headers=headers, json=send_message, verify=False)
    logging.info(response.json())


if __name__ == '__main__':
    print(base_path)
    project_name = sys.argv[1]
    notify_key = sys.argv[2]
    # project_name = 'mall_api_test'
    # notify_key = 'test'
    logging.info(f"参数，{project_name}，{notify_key}")

    # 获取执行结果
    allureReportPath = f"/var/lib/jenkins/workspace/api_auto_test/report/{project_name}/allure-report/data/behaviors.csv"
    logging.info(f"报告路径：{allureReportPath}")
    total_case, pass_case, failed_case = get_case_num(allureReportPath)
    pass_rate = "%.2f" % (pass_case / total_case * 100) + "%"

    # 执行数据入库
    saveCaseData(project_name, total_case, pass_case, failed_case, pass_rate)

    # 发送消息
    notify_key_list = notify_key.split(',')
    for notify_key in notify_key_list:
        notify_key = notify_key.lower()
        sendMsgRobot(project_name, notify_key, pass_rate)
