import allure
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.management_role_page import (
    ManagementRolePage,
)


@allure.title("管理角色页面跳转")
@allure.feature("管理角色")
class TestManagementRole01:

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
