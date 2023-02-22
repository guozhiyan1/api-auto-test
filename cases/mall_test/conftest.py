import pytest
from pathlib import Path
import sys
import os

from service.mall.dataConfig.dataConfig_services import DataConfigClass
from service.mall.tracking.tracking_services import TrackingClass
from service.mall.user.user_services import UserClass
from untils.log_helper import logger
from untils.common_method import readConfig
import module.globals as gbl

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)


@pytest.fixture(scope='session', autouse=True)
def auth_login():
    # 配置文件路径
    settings_file = 'mall.yml'
    settings_file_path = Path(base_path).joinpath(settings_file)

    # 环境变量
    gbl.env = gbl.cmdopt
    env_config = readConfig(gbl.env, settings_file_path)
    logger().info(f"环境信息：{gbl.env}, 配置文件路径：{settings_file_path}")

    # 域名
    mall_domain = env_config["mall_domain"]

    # token

    # gbl.userObj = UserClass(mall_domain, token)

    # # 用户登录对象
    loginObj = UserClass(mall_domain)

    phone_no = env_config["phone"]

    login_token = loginObj.auth_login(phone_no=phone_no)["data"]
    gbl.userObj = UserClass(mall_domain, login_token)
    gbl.trackObj = TrackingClass(mall_domain, login_token)
    gbl.dataConfigObj = DataConfigClass(mall_domain, login_token)
