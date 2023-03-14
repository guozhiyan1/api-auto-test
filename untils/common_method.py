import random
from dateutil.relativedelta import relativedelta
from untils.log_helper import logger
import pytest
import yaml
import calendar
import datetime
from datetime import timedelta


def check_list_value(l1, l2, key, check_type=True):
    """
    断言list-value
    :param l1:期望结果
    :param l2:实际结果
    :param key:
    :param check_type: True-相等，False-不等
    :return:
    """
    for i in range(len(l2)):
        v1 = l1[i][key] == '' and '空' or l1[i][key]
        v2 = l2[i][key]
        if check_type:
            pytest.assume(v1 == v2, f"【断言结果】--> 期望结果：{v1}, 实际结果：{v2}")
            logger().info(f"【断言结果】--> 期望结果：{v1}, 实际结果：{v2}")
        else:
            pytest.assume(v1 != v2, f"【断言结果】--> 期望结果：不为{v1}, 实际结果：{v2}")
            logger().info(f"【断言结果】--> 期望结果：不为{v1}, 实际结果：{v2}")


def check_value_true(v1, v2):
    """
    断言为True
    :param v1: 期望结果
    :param v2: 实际结果
    :return:
    """
    v1 = v1 == '' and '空' or v1
    pytest.assume(v1 == v2, f"【断言结果】--> 期望结果：{v1}, 实际结果：{v2}")
    logger().info(f"【断言结果】--> 期望结果：{v1}, 实际结果：{v2}")


def check_value_false(v1, v2):
    """
    断言为Fasle
    :param v1: 期望结果
    :param v2: 实际结果
    :return:
    """
    v1 = v1 == '' and '空' or v1
    pytest.assume(v1 != v2, f"【断言结果】--> 期望结果：不等于{v1}, 实际结果：{v2}")
    logger().info(f"【断言结果】--> 期望结果：不等于{v1}, 实际结果：{v2}")


def check_response(resp, msg=None, code='200'):
    """
    :param resp:
    :param msg:msg不为空则验证msg
    :param code:默认code=200，如果传了其他值，断言这个值
    :return: dic_resp
    """

    if msg:
        assert msg in resp['message']
        return resp

    if code:
        assert code == resp['code']

    return resp


def readConfig(env, file_path):
    # 读取配置文件
    with open(file_path, encoding='UTF-8') as f:
        data = yaml.safe_load(f)
    return data[env]


class DateUtil:
    @staticmethod
    def get_local_time():
        """
        当天时间
        :return:
        """
        now = datetime.datetime.now()
        print(f"当天时间:{now}")
        return now

    @staticmethod
    def get_local_time_by0():
        """
        当天时间0点
        :return:
        """
        now = datetime.datetime.now()
        now = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
        print(f"当天时间0点:{now}")
        return now

    @staticmethod
    def last_month_start():
        """
        本月第一天
        :return:
        """
        now = datetime.datetime.now()
        this_month_start = datetime.datetime(now.year, now.month, 1)
        print(f"本月第一天:{this_month_start}")
        return this_month_start

    @staticmethod
    def last_month_end():
        """
        本月最后一天
        :return:
        """
        now = datetime.datetime.now()
        this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1], 23, 59, 59)
        print(f"本月最后一天:{this_month_end}")
        return this_month_end

    @staticmethod
    def next_month_start():
        """
        次月第一天
        :return:
        """
        now = datetime.datetime.now()
        next_month_start = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]) + timedelta(days=1)
        print(f"次月第一天:{next_month_start}")
        return next_month_start


if __name__ == '__main__':
    date = DateUtil()
    date.get_local_time()
    date.last_month_start()
    date.last_month_end()
    date.next_month_start()
    date.get_local_time_by0()
