import allure
import pytest

from common.loggerhandler import Logger
from test_case_page.operation_and_maintenance_workbench.management_role_page import ManagementRolePage

logger = Logger()
@pytest.mark.usefixtures("login_driver")
@allure.title("管理角色,人员任务统计部分用例")
@allure.feature("管理角色")
class TestManagementRole05:

    """
    区域相关
    """

    def test_management_role_05(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page  = ManagementRolePage(login_driver)
            management_role_page.management_role_05_1()
            assert management_role_page.get_area_select_text() == "东部\n西北\n海外\n南方\n大储运维（宁夏）"
            management_role_page.management_role_05_2()
            assert management_role_page.get_area_select_text() == "东部\n西北\n海外\n南方"
            management_role_page.management_role_05_3()
            assert management_role_page.get_area_select_text() == ""

            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

