import allure
import pytest
from common.loggerhandler import logger
from test_case_page.operation_and_maintenance_workbench.management_role_page import ManagementRolePage
from test_case_page.work_order_management.my_work_order.my_need_to_do_page import MyNeedToDoPage
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage




@pytest.mark.usefixtures("login_driver")
@allure.title("管理角色,工单跳转")
@allure.feature("管理角色")
class TestManagementRole03:

    # 在途异常工单跳转
    def test_management_role_03_1(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_03_1()
            assert WorkOrderListPage(login_driver).get_manual_abnormal_work_order_type_text() == "手工异常工单"
            assert WorkOrderListPage(login_driver).get_system_abnormal_work_order_type_text() == "系统异常工单"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 在途其他工单跳转
    def test_management_role_03_2(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_03_2()
            assert WorkOrderListPage(login_driver).get_regular_standard_inspection_work_order_type_text() == "定期标准巡检工单"
            assert WorkOrderListPage(
                login_driver).get_manual_non_standard_inspection_work_order_type_text() == "手工非标巡检工单"
            assert WorkOrderListPage(login_driver).get_manual_standard_inspection_work_order_type_text() == "手工标准巡检工单"
            assert WorkOrderListPage(login_driver).get_other_work_order_type_text() == "手工其他工单"
            assert WorkOrderListPage(login_driver).get_implement_work_order_type_text() == "实施工单"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 发起工单数跳转
    def test_management_role_03_3(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_03_3()
            assert WorkOrderListPage(login_driver).get_initiator_of_work_order_system_administrator_text() == "系统管理员"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 已执行工单总数跳转
    def test_management_role_03_4(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_03_4()
            assert WorkOrderListPage(login_driver).get_initiator_of_work_order_system_administrator_text() == "系统管理员"
            assert WorkOrderListPage(login_driver).get_handle_status_completed_text() == "已完成"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 待执行工单数跳转
    def test_management_role_03_5(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_03_5()
            assert MyNeedToDoPage(login_driver).get_my_need_to_do_element_aria_selected_value() == "true"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 待执行异常工单跳转
    def test_management_role_03_6(self, login_driver):
        management_role_page = ManagementRolePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            management_role_page.management_role_03_6()
            assert MyNeedToDoPage(login_driver).get_my_need_to_do_element_aria_selected_value() == "true"
            assert WorkOrderListPage(login_driver).get_manual_abnormal_work_order_type_text() == "手工异常工单"
            assert WorkOrderListPage(login_driver).get_system_abnormal_work_order_type_text() == "系统异常工单"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            management_role_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
