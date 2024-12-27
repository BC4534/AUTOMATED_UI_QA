import allure

from test_case_page.project_management.electronic_archives_page.add_operation_maintenance_management_info_page import \
    AddOperationMaintenanceManagementInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_basic_info_page import \
    AddProjectBaseInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_detail_info_page import \
    AddProjectDetailInfoPage
from test_case_page.project_management.electronic_archives_page.electronic_archives_page import ElectronicArchivesPage
from common.loggerhandler import logger


@allure.title("电子档案管理模块")
@allure.description("新增项目")
class TestElectronicArchives02:

    def test_electronic_archives_02(self, login_driver):
        add_election_archives_page = AddOperationMaintenanceManagementInfoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_election_archives_page.switch_to_electronic_archives()
            add_election_archives_page.click_first_project_edit_next()
            add_election_archives_page.click_next_button()
            add_election_archives_page.fill_operation_maintenance_management_info(
                operation_maintenance_person="系统管理员",
                first_inspection_time="2023-01-01",
                inspection_cycle="1",
                inspection_group="1"
            )
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_election_archives_page.get_screenshot_png(f"{self.__class__.__name__}")
