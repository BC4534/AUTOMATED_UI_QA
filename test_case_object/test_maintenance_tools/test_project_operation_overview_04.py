import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_overview_page import ProjectOperationOverviewPage


@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("项目运行总览")
class TestProjectOperationReport04:

    @allure.description("验证项目名称查询功能")
    def test_project_operation_report_07_01(self, login_driver):
        overview_page = ProjectOperationOverviewPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            overview_page.switch_to_project_operation_overview_page()
            overview_page.click_reset_button()
            second_project_name = overview_page.get_second_project_name()
            overview_page.input_project_name(second_project_name)
            overview_page.click_search_button()
            assert second_project_name in overview_page.get_first_project_name()
            overview_page.click_reset_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            overview_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("验证电站名称查询功能")
    def test_project_operation_report_07_02(self, login_driver):
        overview_page = ProjectOperationOverviewPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            overview_page.switch_to_project_operation_overview_page()
            overview_page.click_reset_button()
            second_station_name = overview_page.get_second_station_name()
            overview_page.input_station_name(second_station_name)
            overview_page.click_search_button()
            assert second_station_name in overview_page.get_first_station_name()
            overview_page.click_reset_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            overview_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e