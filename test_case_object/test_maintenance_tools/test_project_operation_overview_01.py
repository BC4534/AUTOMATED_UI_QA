import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_overview_page import ProjectOperationOverviewPage


@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("项目运行总览")
class TestProjectOperationReport01:

    @allure.description("进入项目运行总览界面")
    def test_project_operation_report_01(self,login_driver):
        overview_page = ProjectOperationOverviewPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            overview_page.switch_to_project_operation_overview_page()
            assert overview_page._get_project_operation_overview_is_current_page() == "true"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            overview_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
