import allure
from test_case_page.loginpage import LoginPage
from common.loggerhandler import logger
from common.driverhandler import get_driver


'''
    用例：用户名未填
'''
# 登录数据，先写在代码中，后面分离
login_data = {"url": "http://192.168.1.82:3322/", "username": "", "password": "1234"}


@allure.feature("登录模块")
@allure.story("登录失败")
# @pytest.mark.skip(reason="跳过用例")
class Test_Case_Login_Fail_001():


    @allure.title("账号必填项效验")
    @allure.description("账号必填项效验")
    def test_login_fail_001(self):
        loginpage = LoginPage(get_driver())
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            loginpage.login(url=login_data["url"], username=login_data["username"], password=login_data["password"])
            assert loginpage.username_null_assert() == "请输入必填字段"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            loginpage.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
        finally:
            loginpage.quit()
