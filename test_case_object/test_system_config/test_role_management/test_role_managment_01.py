import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger


@allure.feature("系统配置")
@allure.story("角色管理")
@allure.title("角色管理-页面跳转")
class TestRoleManagment01:
    """
    角色管理-页面跳转
    """

    @allure.description("角色管理-页面跳转")
    def test_role_management_01(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_01()
            assert role_management_page.get_add_role_button_text() == "新增角色"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
