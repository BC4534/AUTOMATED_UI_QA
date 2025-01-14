import allure

from common.loggerhandler import logger
from test_case_page.maintenance_tools.project_operation_report_page import ProjectOperationReportPage


@allure.feature("运维工具")
@allure.story("项目运行报告")
@allure.title("下载任务列表")
class TestProjectOperationReport08:

    @allure.description("验证项目名称查询功能")
    def test_project_operation_report_08_01(self,login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_download_task_list_button()
            report_page.click_reset_button()
            second_download_task_name = report_page.get_second_download_task_name()
            if second_download_task_name != 1:
                report_page.input_download_task_list_task_name(second_download_task_name)
                report_page.click_search_button()
                assert  second_download_task_name in report_page.get_first_download_task_name()
                report_page.click_reset_button()
            report_page.click_close_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("验证状态查询功能")
    def test_project_operation_report_08_02(self, login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_download_task_list_button()
            report_page.click_reset_button()
            report_page.input_download_task_list_task_status("进行中")
            report_page.click_search_button()
            s1 = report_page.get_first_download_task_status()
            if s1 != 1:
                assert s1 == "进行中"
            report_page.click_reset_button()
            report_page.input_download_task_list_task_status("已完成")
            report_page.click_search_button()
            s2 = report_page.get_first_download_task_status()
            if s2 != 1:
                assert s2 == "已完成"
            report_page.click_reset_button()
            report_page.input_download_task_list_task_status("已失败")
            report_page.click_search_button()
            s3 = report_page.get_first_download_task_status()
            if s3 != 1:
                assert s3 == "失败"
            report_page.click_close_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("验证创建时间查询功能")
    def test_project_operation_report_08_03(self, login_driver):
        report_page = ProjectOperationReportPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            report_page.switch_to_project_operation_report_daily_tab()
            report_page.click_download_task_list_button()
            report_page.click_reset_button()
            second_check_time = report_page.get_download_task_list_second_create_time()
            report_page.input_download_task_list_create_time(create_time=second_check_time)
            report_page.click_search_button()
            assert second_check_time[:10] == report_page.get_download_task_list_first_create_time()[:10]
            report_page.click_reset_button()
            report_page.click_close_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误原因{e}")
            report_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
