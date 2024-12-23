import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger


@allure.title("角色管理-验证编辑角色弹框名称是否正确")
@allure.feature("角色管理")
class TestRoleManagment14():
    """
    角色管理-验证编辑角色弹框名称是否正确
    实现思路 ：

    """

    def test_role_management_14(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            assert role_management_page.role_management_14()  == "编辑角色"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

