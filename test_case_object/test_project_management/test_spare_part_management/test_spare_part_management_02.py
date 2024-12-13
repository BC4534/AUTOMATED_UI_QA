import allure
import pytest

from common.mylogger import Logger
from test_case_page.project_management.spare_part_management_page import SparePartManagementPage

logger = Logger()


@allure.title("备件管理-备件入库 新增备件")
@allure.feature("备件管理")
@pytest.mark.usefixtures("login_driver")
class TestSparePartManagement02:

    """
    新增备件
    """

    def test_spare_part_management_02(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page = SparePartManagementPage(login_driver)
            spare_part_management_page.switch_to_spare_part_management_page()
            assert spare_part_management_page.get_spare_part_inbound_button_text() == "备件入库"
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件入库页面跳转")
            raise e
