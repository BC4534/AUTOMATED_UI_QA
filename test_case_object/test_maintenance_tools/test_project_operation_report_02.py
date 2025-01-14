import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_report_page import ProjectOperationReportPage


@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("项目运行日报")
class TestProjectOperationReport02:

    @allure.description("点击导出查询数据按钮")
    def test_project_operation_report_02(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_export_query_data_button()
            assert report_page.get_page_tip() == "至少搜索一个项目"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("对第一个项目进行搜索,点击导出当日充放原数据按钮")
    def test_project_operation_report_02(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            second_project_name = report_page.get_second_project_name()
            report_page.input_project_name(second_project_name)
            report_page.click_search_button()
            report_page.click_export_query_data_button()
            assert len(report_page.get_window_handles()) == 2
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e



