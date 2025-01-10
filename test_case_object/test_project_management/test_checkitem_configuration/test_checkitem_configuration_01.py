import allure

from common.loggerhandler import logger
from test_case_page.project_management.checkitem_configuration_page import (
    CheckItemConfigurationPage,
)


@allure.feature("项目管理")
@allure.story("检查项配置")
@allure.title("检查项配置页面跳转")
class TestCheckItemConfiguration01:

    @allure.description("检查项配置页面跳转")
    def test_check_item_configuration_01(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            assert (
                check_item_configuration_page.get_checkitem_name_input_tip_text()
                == "巡检项名称"
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("检查项配置页面跳转")
            raise e
