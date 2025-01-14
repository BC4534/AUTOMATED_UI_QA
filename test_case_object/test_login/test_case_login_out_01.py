import allure
from test_case_page.loginpage import LoginPage
from common.loggerhandler import logger



@allure.feature("登录模块")
@allure.story("登出功能")
# @pytest.mark.skip(reason="跳过用例")
class Test_Case_Login_Out_01:

    @allure.description("登出测试")
    @allure.title("登出")
    def test_case_login_out01(self, login_driver):
        loginpage = LoginPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            loginpage.logout()
            assert loginpage.sermatec_assert() == "采日运维管理系统"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            loginpage.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
