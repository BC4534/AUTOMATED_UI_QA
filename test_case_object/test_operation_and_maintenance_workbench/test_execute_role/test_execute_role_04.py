import allure
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.execute_role_page import (
    ExecuteRolePage,
)


@allure.feature("运维工作台")
@allure.story("执行角色")
@allure.title("执行角色，任务过程看板切换年月 ")
class TestExecuteRole04:

    # 任务过程看片切换年月”
    @allure.description("执行角色，任务过程看板切换年月 ")
    def test_execute_role_04(self, login_driver):
        execute_role_page = ExecuteRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            execute_role_page.execute_role_04_1()
            assert execute_role_page.get_week_or_month_assert_text() == "月"
            execute_role_page.execute_role_04_2()
            assert execute_role_page.get_week_or_month_assert_text() == "周"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            execute_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
