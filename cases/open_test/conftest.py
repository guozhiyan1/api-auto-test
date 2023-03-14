import pytest
from pathlib import Path
import sys
import os

from service.open.notify.notify_services import NotifyClass
from service.open.oauth.auth_services import OAuthClass
from untils.log_helper import logger
from untils.common_method import readConfig
import module.globals as gbl

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)


@pytest.fixture(scope='session', autouse=True)
def get_token():
    # 配置文件路径
    settings_file = 'open.yml'
    settings_file_path = Path(base_path).joinpath(settings_file)

    # 环境变量
    gbl.env = gbl.cmdopt
    env_config = readConfig(gbl.env, settings_file_path)
    logger().info(f"环境信息：{gbl.env}, 配置文件路径：{settings_file_path}")

    # 域名
    open_domain = env_config["open_domain"]

    # # 获取oauth_token
    loginObj = OAuthClass(open_domain)

    oauth_token = loginObj.get_oauth_token()["data"]["tokenType"] + ' ' + loginObj.get_oauth_token()["data"]["accessToken"]
    gbl.oauthObj = OAuthClass(open_domain, oauth_token)
    gbl.notifyObj = NotifyClass(open_domain)
