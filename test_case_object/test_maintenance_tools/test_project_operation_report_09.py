import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_report_page import ProjectOperationReportPage
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("项目运行日报")
class TestProjectOperationReport09:

    @allure.description("累计告警数（支持点击跳转至项目告警明细）")
    def test_project_operation_report_09_01(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            a = report_page.click_accumulated_alarm_count()

            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("累计工单数（支持点击跳转至项目工单列表）")
    def test_project_operation_report_09_02(self, login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            project_name = report_page.click_accumulated_work_order_count()
            if project_name != 1:
                assert work_order_list_page.get_association_project_text() == project_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("累计异常工单数（支持点击跳转至项目告警明细）")
    def test_project_operation_report_09_03(self, login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            _ = report_page.click_accumulated_abnormal_work_order_count()
            if _ != 1:
                assert work_order_list_page.get_work_order_type_search_entered_1_loc_text() == "系统异常工单"
                assert work_order_list_page.get_work_order_type_search_entered_2_loc_text() == "手工异常工单"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

