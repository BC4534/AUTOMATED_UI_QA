import allure
import pytest
from test_case_object.conftest import  login_driver
from test_case_page.loginpage import LoginPage
from common.loggerhandler import Logger

logger = Logger()


@allure.title("登出测试用例")
@allure.feature("登录模块")
# @pytest.mark.skip(reason="跳过用例")
class Test_Case_Login_Out_01():

    def test_case_login_out01(self, login_driver):

        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            loginpage = LoginPage(login_driver)
            loginpage.logout()
            assert loginpage.sermatec_assert() == "采日运维管理系统"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            loginpage.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
