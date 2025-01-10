import allure
from common.loggerhandler import logger
from test_case_page.project_management.resourcesInventory_page import (
    ResourcesInventoryPage,
)


@allure.feature("项目管理模块")
@allure.story("人力资源复功能")
@allure.title("人力资源复盘页面跳转")
class TestResourcesInventory01:

    @allure.description("人力资源复盘页面跳转")
    def test_resources_inventory_01(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源复盘页面跳转")
            raise e
