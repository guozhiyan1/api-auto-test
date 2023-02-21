import pytest
from pathlib import Path
import sys
import os

from untils.log_helper import logger
from untils.common_method import readConfig
import module.globals as gbl
from service.mall.demo.user_services import UserClass

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)


@pytest.fixture(scope='session', autouse=True)
def auth_login():
    # 配置文件路径
    settings_file = 'mall_user.yml'
    settings_file_path = Path(base_path).joinpath(settings_file)

    # 环境变量
    gbl.env = gbl.cmdopt
    env_config = readConfig(gbl.env, settings_file_path)
    logger().info(f"环境信息：{gbl.env}, 配置文件路径：{settings_file_path}")

    # 域名
    mall_domain = env_config["mall_domain"]

    gbl.userObj = UserClass(mall_domain)
