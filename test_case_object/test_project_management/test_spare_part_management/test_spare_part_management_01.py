import allure
from common.loggerhandler import logger
from test_case_page.project_management.spare_part_management_page import (
    SparePartManagementPage,
)


@allure.feature("项目管理模块")
@allure.story("备件管理功能")
@allure.title("备件管理")
class TestSparePartManagement01:

    @allure.description("备件管理-备件入库页面跳转")
    def test_spare_part_management_01(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            assert (
                spare_part_management_page.get_spare_part_inbound_button_text()
                == "备件入库"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件入库页面跳转")
            raise e
