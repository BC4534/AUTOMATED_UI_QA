import time
from test_case_page.loginpage import LoginPage
import pytest
from common.loggerhandler import logger
from common.yamlhandler import YamlHandler
from common import all_file_path
from common.driverhandler import get_driver


yamlhandler = YamlHandler(all_file_path.config_yaml_path)
login_data = yamlhandler.read("login_info")

@pytest.fixture(scope="module")
def login_driver():
    # 实现登录前置
    logger.debug("开始登录前置")
    driver = get_driver()
    driver.maximize_window()
    LoginPage(driver).login(url=login_data["url"], username=login_data["username"], password=login_data["password"])
    logger.debug("前置登录成功")
    yield driver
    logger.debug("开始登录后置")
    driver.close()
    logger.debug("登录后置完成")


@pytest.fixture(scope="module")
def moult_fixture():
    pass


@pytest.fixture(scope="class")
def class_fixture():
    pass


@pytest.fixture(scope="function")
def function_fixture():
    pass




if __name__ == '__main__':
    login_driver()
