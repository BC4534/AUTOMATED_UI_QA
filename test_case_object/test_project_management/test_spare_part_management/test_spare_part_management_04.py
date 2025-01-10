import time

import allure
import pytest
from common.loggerhandler import logger
from test_case_page.project_management.spare_part_management_page import (
    SparePartManagementPage,
)

spare_part_receive_data = {
    "part_number": "0",
    "part_project": "1024",
    "part_remark": "UI测试备件领用备注",
}
spare_part_receive_data2 = {
    "part_number": "1",
    "part_project": "UI测试备件领用项目",
    "part_remark": "UI测试备件领用备注",
}
spare_part_receive_data3 = {
    "part_number": "10",
    "part_project": "UI测试备件领用项目",
    "part_remark": "UI测试备件领用备注",
}


@allure.feature("项目管理模块")
@allure.story("备件管理功能")
@allure.title("备件领用")
class TestSparePartManagement04:

    @allure.description("备件领用-领用必填项,备件领用界面title效验")
    def test_spare_part_management_04_1(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_first_spare_part_receive_button()
            assert (
                spare_part_management_page.get_spare_part_receive_title() == "备件领用"
            )
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            assert "参数校验失败:" in spare_part_management_page.get_page_tip_text()
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png(
                "备件领用-领用必填项,备件领用界面title效验"
            )
            raise e

    @allure.description("备件领用-领用数量需>0")
    def test_spare_part_management_04_2(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_first_spare_part_receive_button()
            spare_part_management_page.spare_part_receive(
                spare_part_receive_data["part_number"],
                spare_part_receive_data["part_project"],
                spare_part_receive_data["part_remark"],
            )
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            assert (
                "参数校验失败: 领用数量必须大于0"
                in spare_part_management_page.get_page_tip_text()
            )
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件领用-领用数量需>0")
            raise e

    @allure.description("备件领用-领用后点击取消")
    def test_spare_part_management_04_3(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_first_spare_part_receive_button()
            old_number = (
                spare_part_management_page.get_spare_part_receive_stock_number()
            )
            spare_part_management_page.spare_part_receive(
                spare_part_receive_data2["part_number"],
                spare_part_receive_data2["part_project"],
                spare_part_receive_data2["part_remark"],
            )
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            spare_part_management_page.click_first_spare_part_receive_button()
            assert (
                spare_part_management_page.get_spare_part_receive_stock_number()
                == old_number
            )
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件领用-领用后点击取消")
            raise e

    @allure.description("备件领用-领用后点击关闭")
    def test_spare_part_management_04_4(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_first_spare_part_receive_button()
            old_number = (
                spare_part_management_page.get_spare_part_receive_stock_number()
            )
            spare_part_management_page.spare_part_receive(
                spare_part_receive_data2["part_number"],
                spare_part_receive_data2["part_project"],
                spare_part_receive_data2["part_remark"],
            )
            spare_part_management_page.click_spare_part_inbound_close_button()
            spare_part_management_page.click_first_spare_part_receive_button()
            assert (
                spare_part_management_page.get_spare_part_receive_stock_number()
                == old_number
            )
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件领用-领用后点击关闭")
            raise e

    @allure.description("备件领用-领用后点击确认")
    def test_spare_part_management_04_5(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_first_spare_part_receive_button()
            old_number = (
                spare_part_management_page.get_spare_part_receive_stock_number()
            )
            spare_part_management_page.spare_part_receive(
                spare_part_receive_data2["part_number"],
                spare_part_receive_data2["part_project"],
                spare_part_receive_data2["part_remark"],
            )
            spare_part_management_page.click_spare_part_inbound_confirm_button()
            spare_part_management_page.click_first_spare_part_receive_button()
            assert (
                spare_part_management_page.get_spare_part_receive_stock_number()
                == str(int(old_number) - 1)
            )
            spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件领用-领用后点击确认")
            raise e

    @allure.description("备件领用-领用数量大于库存数量")
    def test_spare_part_management_04_6(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_first_spare_part_receive_button()
            old_number = (
                spare_part_management_page.get_spare_part_receive_stock_number()
            )
            if old_number == "0":
                logger.info(f"库存数量为0，无法进行测试")
            else:
                spare_part_management_page.spare_part_receive(
                    part_number=str(int(old_number) + 1),
                    part_project=spare_part_receive_data3["part_project"],
                    part_remark=spare_part_receive_data3["part_remark"],
                )
                spare_part_management_page.click_spare_part_inbound_confirm_button()
                spare_part_management_page.click_first_spare_part_receive_button()
                assert (
                    spare_part_management_page.get_spare_part_receive_stock_number()
                    == "0"
                )
                spare_part_management_page.click_spare_part_inbound_cancel_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件领用-领用后点击确认")
            raise e
