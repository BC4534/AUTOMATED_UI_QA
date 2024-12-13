
import allure
import pytest
from selenium import webdriver
from test_case_page.loginpage import LoginPage
from common.mylogger import Logger
from common.driverhandler import get_driver
logger = Logger()
'''
    用例：密码错误
'''
# 登录数据，先写在代码中，后面分离
login_data = {"url": "http://192.168.1.82:3322/", "username": "admin", "password": "*sermatecroot2411"}

@allure.title("登录界面测试用例")
@allure.feature("登录模块")
# @pytest.mark.skip(reason="跳过用例")
class Test_Case_Login_Fail_004():

    def test_login_fail_004(self):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            loginpage = LoginPage(get_driver())
            loginpage.login(url=login_data["url"], username=login_data["username"], password=login_data["password"])
            assert loginpage.login_fail_assert() == "用户名或密码错误!"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            loginpage.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
        finally:
            loginpage.quit()
