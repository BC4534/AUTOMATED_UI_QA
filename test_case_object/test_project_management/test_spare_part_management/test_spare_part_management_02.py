import time

import allure
import pytest
from common.loggerhandler import logger
from test_case_page.project_management.spare_part_management_page import SparePartManagementPage

spare_part_inbound_data = {
    "part_attribute": "采日自采备件",
    "part_name": "UI测试备件名称-采日自采备件",
    "part_number": "5",
    "part_remark": "UI测试备件备注",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注"
}
spare_part_inbound_data2 = {
    "part_attribute": "采日自研备件",
    "part_name": "UI测试备件名称",
    "part_number": "5",
    "part_remark": "UI测试备件备注-采日自研备件",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注"
}
spare_part_inbound_data3 = {
    "part_attribute": "供应商预存备件",
    "part_name": "UI测试备件名称-供应商预存备件",
    "part_number": "5",
    "part_remark": "UI测试备件备注",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注"
}


@allure.feature("项目管理模块")
@allure.story("备件管理功能")
@allure.title("备件管理")
class TestSparePartManagement02:
    """
    新增备件
    """

    @allure.description("新增备件-采日自采备件")
    @pytest.mark.parametrize("data", [spare_part_inbound_data, spare_part_inbound_data2, spare_part_inbound_data3])
    # @pytest.mark.parametrize("data", [spare_part_inbound_data])
    def test_spare_part_management_02_1(self, login_driver, data):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_spare_part_inbound_button()
            spare_part_management_page.add_spare_part_inbound(
                part_attribute=data["part_attribute"],
                part_name=data["part_name"],
                part_number=data["part_number"],
                part_remark=data["part_remark"],
                part_type=data["part_type"],
                part_vendor=data["part_vendor"],
                part_warehouse=data["part_warehouse"],
                part_inbound_remark=data["part_inbound_remark"]
            )
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-新增采日自采备件")
            if spare_part_management_page.is_in_spare_part_inbound_page():
                spare_part_management_page.click_spare_part_inbound_close_button()
            raise e

    @allure.description("新增备件,重复新增，名称重复")
    def test_spare_part_management_02_2(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            first_spart_part_name = spare_part_management_page.get_first_spare_part_name()
            spare_part_management_page.click_spare_part_inbound_button()
            spare_part_management_page.add_spare_part_inbound(
                part_attribute=spare_part_inbound_data["part_attribute"],
                part_name=first_spart_part_name,
                part_number=spare_part_inbound_data["part_number"],
                part_remark=spare_part_inbound_data["part_remark"],
                part_type=spare_part_inbound_data["part_type"],
                part_vendor=spare_part_inbound_data["part_vendor"],
                part_warehouse=spare_part_inbound_data["part_warehouse"],
                part_inbound_remark=spare_part_inbound_data["part_inbound_remark"]
            )
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            # 同名备件已存在, 不允许添加
            assert spare_part_management_page.get_page_tip_text() == "同名备件已存在, 不允许添加"
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件入库页面跳转")
            raise e

    @allure.description("新增备件,必填项效验")
    def test_spare_part_management_02_3(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_spare_part_inbound_button()
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            assert "参数校验失败" in spare_part_management_page.get_page_tip_text()
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件入库页面跳转")
            raise e

    @allure.description("维护已有备件")
    def test_spare_part_management_02_4(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_spare_part_inbound_button()
            spare_part_management_page.maintain_spare_part(
                part_name=spare_part_inbound_data["part_name"],
                part_number="1",
                part_inbound_remark=spare_part_inbound_data["part_inbound_remark"]
            )
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件入库页面跳转")
            raise e

    @allure.description("维护已有备件,数量=0")
    def test_spare_part_management_02_5(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_spare_part_inbound_button()
            spare_part_management_page.maintain_spare_part(
                part_name=spare_part_inbound_data["part_name"],
                part_number="0",
                part_inbound_remark=spare_part_inbound_data["part_inbound_remark"]
            )
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            assert spare_part_management_page.get_page_tip_text() == "参数校验失败: 入库数量必须大于0"
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件入库页面跳转")
            raise e



