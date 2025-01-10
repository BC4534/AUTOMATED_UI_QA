import allure
from test_case_page.loginpage import LoginPage
from common.loggerhandler import logger
from common.driverhandler import get_driver

"""
    用例：掩码按钮
"""
# 登录数据，先写在代码中，后面分离
login_data = {
    "url": "http://192.168.1.82:3322/",
    "username": "admin",
    "password": "*sermatecroot24",
}


@allure.title("登录界面测试用例")
@allure.feature("登录模块")
# @pytest.mark.skip(reason="跳过用例")
class Test_Case_Login_Fail_005:

    @allure.story("验证掩码按钮")
    def test_login_fail_005(self):
        loginpage = LoginPage(get_driver())
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            loginpage.login(url=login_data["url"], username=login_data["username"], password=login_data["password"])
            password_value = loginpage.read_password_value()
            assert password_value == login_data["password"]
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            loginpage.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
        finally:
            loginpage.quit()
