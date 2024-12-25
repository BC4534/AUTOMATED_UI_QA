import allure
import pytest
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.management_role_page import ManagementRolePage


@pytest.mark.usefixtures("login_driver")
@allure.title("管理角色,切换数据维度")
@allure.feature("管理角色")
class TestManagementRole02:

    def test_management_role_02(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_02()
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e