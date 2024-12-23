import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger



data = {
    "name": "系统管理员",
    "remark": "测试角色备注"
}
@allure.title("角色管理-查询角色")
@allure.feature("角色管理")
class TestRoleManagment16():
    """
        验证查询组件

    """

    def test_role_management_16_1(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_01()
            role_management_page.role_management_16(data["name"])
            role_management_page.click_search_button()
            assert data["name"] in role_management_page.get_first_role_name()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    def test_role_management_16_2(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_16(data["name"])
            role_management_page.click_reset_button()
            assert  role_management_page.get_select_role_name_input() == ""
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

