import allure

from common.loggerhandler import logger
from test_case_page.project_management.checkitem_configuration_page import (
    CheckItemConfigurationPage,
)


@allure.feature("项目管理")
@allure.story("检查项配置")
@allure.title("查询功能")
class TestCheckItemConfiguration03:

    @allure.description("巡检项名称查询")
    def test_check_item_configuration_03(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.click_reset_button()
            second_name = check_item_configuration_page.get_second_checkitem_name()
            check_item_configuration_page.search_checkitem_by_name(second_name)
            check_item_configuration_page.click_search_button()
            assert (
                second_name in check_item_configuration_page.get_first_checkitem_name()
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("巡检项名称查询")
            raise e
