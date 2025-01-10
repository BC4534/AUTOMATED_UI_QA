import allure
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.execute_role_page import (
    ExecuteRolePage,
)
from test_case_page.work_order_management.my_work_order.my_already_do_page import (
    MyAlreadyDoPage,
)
from test_case_page.work_order_management.my_work_order.my_need_to_do_page import (
    MyNeedToDoPage,
)


@allure.feature("运维工作台")
@allure.story("执行角色")
@allure.title("执行角色，我的代办工单跳转 ")
class TestExecuteRole03:

    # 1、点击“工单总数跳转”
    @allure.description("我的代办-点击工单总数跳转 ")
    def test_execute_role_03_1(self, login_driver):
        execute_role_page = ExecuteRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            execute_role_page.test_execute_role_03_1()
            assert MyNeedToDoPage(login_driver).is_my_need_to_do_page() == "true"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为：{e}")
            execute_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 点击已执行工单 跳转
    @allure.description("我的已办-点击已执行工单跳转 ")
    def test_execute_role_03_2(self, login_driver):
        execute_role_page = ExecuteRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            execute_role_page.test_execute_role_03_2()
            assert MyAlreadyDoPage(login_driver).is_my_already_do_page() == "true"
            assert MyAlreadyDoPage(login_driver).get_handle_status_text() == "已完成"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为：{e}")
            execute_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 点击 待执行工单 跳转
    @allure.description("我的已办-点击待执行工单跳转 ")
    def test_execute_role_03_3(self, login_driver):
        execute_role_page = ExecuteRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            execute_role_page.test_execute_role_03_3()
            assert MyNeedToDoPage(login_driver).is_my_need_to_do_page() == "true"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为：{e}")
            execute_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
