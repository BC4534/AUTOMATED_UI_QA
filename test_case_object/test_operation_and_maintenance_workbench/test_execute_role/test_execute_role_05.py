import allure
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.execute_role_page import (
    ExecuteRolePage,
)


@allure.feature("运维工作台")
@allure.story("执行角色")
@allure.title("执行角色，负责项目统计部分用例 ")
class TestExecuteRole05:

    # 负责项目统计部分用例”
    @allure.description("负责项目统计,区域切换")
    def test_execute_role_05(self, login_driver):
        execute_role_page = ExecuteRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            execute_role_page.execute_role_05_1()
            assert (
                execute_role_page.get_area_select_text()
                == "东部\n西北\n海外\n南方\n大储运维（宁夏）"
            )
            execute_role_page.execute_role_05_2()
            assert execute_role_page.get_area_select_text() == "东部\n西北\n海外\n南方"
            execute_role_page.execute_role_05_3()
            assert execute_role_page.get_area_select_text() == ""
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            execute_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
