import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger



@allure.title("角色管理-验证新增角色界面弹框文本信息")
@allure.feature("角色管理")
class TestRoleManagment15():
    """
    角色管理-验证新增角色界面弹框文本信息

    """

    def test_role_management_15(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page = RoleManagementPage(login_driver)
            assert role_management_page.role_management_15()  == "新增角色"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

