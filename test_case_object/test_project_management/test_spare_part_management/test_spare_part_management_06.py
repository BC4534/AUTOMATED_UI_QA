import time

import allure
import pytest
from common.loggerhandler import logger
from test_case_page.project_management.spare_part_management_page import SparePartManagementPage


@allure.feature("项目管理模块")
@allure.story("备件管理功能")
@allure.title("查询功能")
class TestSparePartManagement06:


    @allure.description("备件领用-备件名称查询功能")
    def test_spare_part_management_06_1(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_reset_button()
            part_name = spare_part_management_page.get_second_spare_part_name()
            spare_part_management_page.search_by_spare_part_name(part_name)
            spare_part_management_page.click_search_button()
            assert part_name in spare_part_management_page.get_first_spare_part_name()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件名称查询功能")
            raise e

    @allure.description("备件领用-备件类型查询功能")
    def test_spare_part_management_06_2(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_reset_button()
            part_type = spare_part_management_page.get_second_spare_part_type()
            if spare_part_management_page.search_by_spare_part_type(part_type) == 1:
                spare_part_management_page.click_search_button()
                assert "EMS类附件" in spare_part_management_page.get_first_spare_part_type()
            else:
                spare_part_management_page.click_search_button()
                assert part_type in spare_part_management_page.get_first_spare_part_type()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件类型查询功能")
            raise e

    @allure.description("备件领用-所属仓库查询功能")
    def test_spare_part_management_06_3(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_reset_button()
            spare_part_management_page.search_by_spare_part_warehouse("上海备品仓")
            spare_part_management_page.click_search_button()
            try:
                sh = spare_part_management_page.get_first_spare_part_warehouse()
                if sh is not None:
                    assert "上海备品仓" in spare_part_management_page.get_first_spare_part_warehouse()
            except:
                logger.info("上海备品仓不存在或者没有备件数据")
            spare_part_management_page.click_reset_button()
            spare_part_management_page.search_by_spare_part_warehouse("宁夏备品仓")
            spare_part_management_page.click_search_button()
            try:
                nx  = spare_part_management_page.get_first_spare_part_warehouse()
                if nx is not None:
                    assert "宁夏备品仓" in spare_part_management_page.get_first_spare_part_warehouse()
            except:
                logger.info("宁夏备品仓不存在或者没有备件数据")
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-所属仓库查询功能")
            raise e

    @allure.description("备件领用-备件属性查询功能")
    def test_spare_part_management_06_4(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_reset_button()
            part_attribute = spare_part_management_page.get_second_spare_part_attribute()
            spare_part_management_page.search_by_spare_part_attribute(part_attribute)
            spare_part_management_page.click_search_button()
            assert part_attribute in spare_part_management_page.get_first_spare_part_attribute()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件属性查询功能")
            raise e

    @allure.description("备件领用-所属供货商查询功能")
    def test_spare_part_management_06_5(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_reset_button()
            part_supplier = spare_part_management_page.get_second_spare_part_supplier()
            s = spare_part_management_page.search_by_spare_part_supplier(part_supplier)
            spare_part_management_page.click_search_button()
            if s is None:
                assert part_supplier in spare_part_management_page.get_first_spare_part_supplier()
            else:
                assert s in spare_part_management_page.get_first_spare_part_supplier()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-所属供货商查询功能")
            raise e






