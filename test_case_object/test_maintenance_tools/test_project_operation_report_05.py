import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_report_page import ProjectOperationReportPage


@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("项目运行日报")
class TestProjectOperationReport05:

    @allure.description("点击第一条数据的导出导出当日充放原数据按钮")
    def test_project_operation_report_05(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_export_daily_charge_and_discharge_data_button()
            assert report_page.get_page_tip() == "导出任务已启动"
            first_project_name = report_page.get_first_project_name()
            report_page.click_download_task_list_button()
            assert first_project_name in report_page.get_first_download_task_name()
            report_page.click_close_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
