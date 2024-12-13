import allure

from common.mylogger import Logger
from test_case_page.operation_and_maintenance_workbench.execute_role_page import ExecuteRolePage

logger = Logger()



@allure.title("执行角色页面跳转")
@allure.feature("执行角色")
class TestExecuteRole01():

    def test_management_role_01(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page  = ExecuteRolePage(login_driver)
            management_role_page.switch_to_execute_role_page()
            assert (management_role_page.get_in_transit_project_lookboard_text()
                    == "在途项目看板")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e