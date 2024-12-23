import allure
from common.driverhandler import get_driver
from test_case_object.conftest import login_data, login_driver
from test_case_page.loginpage import LoginPage
from common.loggerhandler import logger




@allure.title("登录界面测试用例")
@allure.feature("登录模块")
# @pytest.mark.skip(reason="跳过用例")
class Test_Case_Login_Success_001():

    def test_case_login_success_001(self):
        loginpage = LoginPage(get_driver())
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            loginpage.login(url=login_data["url"], username=login_data["username"], password=login_data["password"])
            assert loginpage.login_assert() == "采日运维管理系统"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            loginpage.get_screenshot_png(f"{self.__class__.__name__}")
            raise e