import allure
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.management_role_page import (
    ManagementRolePage,
)


@allure.feature("运维工作")
@allure.story("管理角色")
@allure.title("跳转至管理角色页面")
class TestManagementRole01:

    @allure.description("跳转至管理角色页面")
    def test_management_role_01(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.switch_to_management_role_page()
            assert (
                management_role_page.get_in_transit_project_lookboard_text()
                == "在途项目看板"
            )
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
