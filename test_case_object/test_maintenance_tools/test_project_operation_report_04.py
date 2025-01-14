import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_report_page import ProjectOperationReportPage


@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("项目运行日报")
class TestProjectOperationReport04:

    @allure.description("点击第一条数据的导出云平台巡检记录按钮")
    def test_project_operation_report_04_01(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_export_cloud_platform_inspection_data_button()
            report_page.click_close_button()
            assert report_page._get_content_page() is False
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("点击第一条数据的导出云平台巡检记录按钮,巡检记录点击一个导出按钮")
    def test_project_operation_report_04_02(self, login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_export_cloud_platform_inspection_data_button()
            report_page.click_inspection_record_export_button()
            assert len(report_page.get_window_handles()) == 2
            report_page.click_close_button()

        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("点击第一条数据的导出云平台巡检记录按钮,巡检记录点击导出全部文件按钮")
    def test_project_operation_report_04_03(self, login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_export_cloud_platform_inspection_data_button()
            report_page.click_inspection_record_export_all_file_button()
            assert len(report_page.get_window_handles()) == 2
            report_page.click_close_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

