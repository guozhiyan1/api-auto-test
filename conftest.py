# -*- coding: utf-8 -*-

import sys
import os

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)

from module import globals as gbl


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="test", help="--cmdopt: test, uat or prod")


def pytest_configure(config):
    gbl.cmdopt = config.getoption('--cmdopt')
