import allure
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.execute_role_page import (
    ExecuteRolePage,
)


@allure.feature("运维工作台")
@allure.story("执行角色")
@allure.title("执行角色，数据维度切换 ")
class TestExecuteRole02:
    @allure.description("在途项目看板,数据维度切换 ")
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
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息:{e}")
            execute_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
