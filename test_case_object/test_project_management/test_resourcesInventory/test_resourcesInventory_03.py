import allure
from common.loggerhandler import logger
from test_case_page.project_management.resourcesInventory_page import (
    ResourcesInventoryPage,
)


@allure.feature("项目管理模块")
@allure.story("人力资源复功能")
@allure.title("人力资源复盘查询功能")
class TestResourcesInventory03:

    @allure.description("按人员名称查询")
    def test_resources_inventory_03_1(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_reset_button()
            second_name = resources_inventory_page.get_second_name_loc_text()
            resources_inventory_page.resources_inventory_search_by_name(second_name)
            resources_inventory_page.click_search_button()
            assert resources_inventory_page.get_first_name_loc_text() == second_name
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源复盘页面跳转")
            raise e

    @allure.description("按所属区域查询")
    def test_resources_inventory_03_2(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_reset_button()
            second_area = resources_inventory_page.get_second_area_loc_text()
            if (
                resources_inventory_page.resources_inventory_search_by_area(second_area)
                == 1
            ):
                resources_inventory_page.click_search_button()
                assert "东部" in resources_inventory_page.get_first_area_loc_text()
            else:
                resources_inventory_page.click_search_button()
                assert second_area in resources_inventory_page.get_first_area_loc_text()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")

        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源复盘页面跳转")
            raise e
