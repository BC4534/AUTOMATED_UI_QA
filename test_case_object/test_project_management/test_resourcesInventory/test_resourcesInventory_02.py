import allure

from common.loggerhandler import logger
from test_case_page.project_management.resourcesInventory_page import (
    ResourcesInventoryPage,
)


@allure.feature("项目管理模块")
@allure.story("人力资源复功能")
@allure.title("人力资源复盘-点击数量展开")
class TestResourcesInventory02:

    @allure.description("人力资源-负责项目总数点击")
    def test_resources_inventory_02_1(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-负责项目总数点击")
            raise e

    @allure.description("人力资源-实施阶段项目数点击")
    def test_resources_inventory_02_2(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_implementation_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_implementation_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_implementation_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-实施阶段项目数点击")
            raise e

    @allure.description("人力资源-售后质保项目数点击")
    def test_resources_inventory_02_3(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_after_sales_warranty_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_after_sales_warranty_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_after_sales_warranty_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-售后质保项目数点击")
            raise e

    @allure.description("人力资源-售后过保项目数点击")
    def test_resources_inventory_02_4(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_after_sales_expired_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_after_sales_expired_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_after_sales_expired_project_count()
            assert resources_inventory_page.get_project_name_loc_text() == "项目名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-售后过保项目数点击")
            raise e

    @allure.description("人力资源-处理任务总数点击")
    def test_resources_inventory_02_5(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_task_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_task_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_task_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-处理任务总数点击")
            raise e

    @allure.description("人力资源-处理实施工单数点击")
    def test_resources_inventory_02_6(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_implementation_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_implementation_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_implementation_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-处理实施工单数点击")
            raise e

    @allure.description("人力资源-处理巡检工单数点击")
    def test_resources_inventory_02_7(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_inspection_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_inspection_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_inspection_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-处理巡检工单数点击")
            raise e

    @allure.description("人力资源-处理异常工单数点击")
    def test_resources_inventory_02_8(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_abnormal_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_abnormal_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_abnormal_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-处理异常工单数点击")
            raise e

    @allure.description("人力资源-代办工单数点击")
    def test_resources_inventory_02_9(self, login_driver):
        resources_inventory_page = ResourcesInventoryPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            resources_inventory_page.switch_to_resources_inventory_page()
            resources_inventory_page.click_pending_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_cancel_button()
            resources_inventory_page.click_pending_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_close_button()
            resources_inventory_page.click_pending_work_order_count()
            assert resources_inventory_page.get_work_order_name_loc_text() == "工单名称"
            resources_inventory_page.click_confirm_button()
            assert (
                resources_inventory_page.get_resources_inventory_name_input_placeholder()
                == "请输入人员名称"
            )
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            resources_inventory_page.get_screenshot_png("人力资源-代办工单数点击")
            raise e
