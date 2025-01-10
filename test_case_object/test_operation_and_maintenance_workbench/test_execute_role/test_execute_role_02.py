import allure
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.execute_role_page import (
    ExecuteRolePage,
)


@allure.title("执行角色，数据维度切换 ")
@allure.feature("执行角色")
class TestExecuteRole02:

    def test_execute_role_02(self, login_driver):
        execute_role_page = ExecuteRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            execute_role_page.test_execute_role_02_1()
            assert execute_role_page.get_data_dimension_text() == "项目类型图"
            execute_role_page.test_execute_role_02_2()
            assert execute_role_page.get_data_dimension_text() == "项目阶段图"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            execute_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
