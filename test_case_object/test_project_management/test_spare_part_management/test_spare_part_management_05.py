import allure
from common.loggerhandler import logger
from test_case_page.project_management.spare_part_management_page import (
    SparePartManagementPage,
)


@allure.feature("项目管理模块")
@allure.story("备件管理功能")
@allure.title("翻页功能")
class TestSparePartManagement05:

    @allure.description("备件领用-翻页功能")
    def test_spare_part_management_05(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            if spare_part_management_page.page_turning() != 1:
                assert spare_part_management_page.is_current_page()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-翻页功能")
            raise e
