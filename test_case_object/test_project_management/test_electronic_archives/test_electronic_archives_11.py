import allure

from test_case_page.project_management.electronic_archives_page.add_operation_maintenance_management_info_page import \
    AddOperationMaintenanceManagementInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_basic_info_page import \
    AddProjectBaseInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_detail_info_page import \
    AddProjectDetailInfoPage
from test_case_page.project_management.electronic_archives_page.electronic_archives_page import ElectronicArchivesPage
from common.loggerhandler import logger


@allure.feature("项目管理模块")
@allure.story("电子档案功能")
@allure.title("翻页功能")
class TestElectronicArchives10:

    @allure.description("通过点击界面的不同页面，实现翻页")
    def test_electronic_archives_08_1(self, login_driver):
        add_election_archives_page = AddOperationMaintenanceManagementInfoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_election_archives_page.switch_to_electronic_archives()
            add_election_archives_page.page_turning_by_click_next_page()
            add_election_archives_page.page_turning_by_click_previous_page()
            add_election_archives_page.page_turning_by_click_page_2()
            add_election_archives_page.page_turning_by_click_page_1()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_election_archives_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
