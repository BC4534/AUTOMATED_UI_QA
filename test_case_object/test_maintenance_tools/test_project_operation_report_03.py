import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_report_page import ProjectOperationReportPage


@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("项目运行日报")
class TestProjectOperationReport03:

    @allure.description("点击批量导出云平台巡检数据按钮")
    def test_project_operation_report_03_01(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_batch_export_cloud_platform_inspection_data_button()
            assert report_page.get_page_tip() == "请勾选需要导出的数据"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("勾选待导出数据后,点击批量导出云平台巡检数据按钮")
    def test_project_operation_report_03_02(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_select_all_checkbox()
            report_page.click_batch_export_cloud_platform_inspection_data_button()
            assert len(report_page.get_window_handles()) == 2
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

