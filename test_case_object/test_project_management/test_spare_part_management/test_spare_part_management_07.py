import allure
import pytest
from common.loggerhandler import logger
from test_case_page.project_management.spare_part_management_page import (
    SparePartManagementPage,
)

spare_part_inbound_data = {
    "part_attribute": "采日自采备件",
    "part_name": "UI测试备件名称-采日自采备件",
    "part_number": "5",
    "part_remark": "UI测试备件备注",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注",
}
spare_part_inbound_data2 = {
    "part_attribute": "采日自研备件",
    "part_name": "UI测试备件名称",
    "part_number": "5",
    "part_remark": "UI测试备件备注-采日自研备件",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注",
}
spare_part_inbound_data3 = {
    "part_attribute": "供应商预存备件",
    "part_name": "UI测试备件名称-供应商预存备件",
    "part_number": "5",
    "part_remark": "UI测试备件备注",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注",
}


@allure.feature("项目管理模块")
@allure.story("备件管理功能")
@allure.title("备件管理")
class TestSparePartManagement07:
    """
    删除前面新增的三个备件
    """

    @allure.description("删除备件，备件数量不等于0")
    def test_spare_part_management_07(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.check_all_spare_part_checkbox()
            spare_part_management_page.click_delete_spare_part_button()
            # 库存不为0的备品或备件不能删除!
            assert (
                spare_part_management_page.get_page_tip_text()
                == "库存不为0的备品或备件不能删除!"
            )
            spare_part_management_page.refresh()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-备件数量不等于0")
            raise e

    @allure.description("删除备件，备件数量不等于0")
    def test_spare_part_management_07(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            while True:
                first_spare_part_name = (
                    spare_part_management_page.get_first_spare_part_name()
                )
                if "UI测试" in first_spare_part_name:
                    if spare_part_management_page.get_first_spare_part_number() != "0":
                        spare_part_management_page.click_first_spare_part_receive_button()
                        old_number = (
                            spare_part_management_page.get_spare_part_receive_stock_number()
                        )
                        spare_part_management_page.spare_part_receive(
                            part_number=str(int(old_number) + 1),
                            part_project="_",
                            part_remark="_",
                        )
                        spare_part_management_page.click_spare_part_inbound_confirm_button()
                    spare_part_management_page.check_first_spare_part_checkbox()
                    spare_part_management_page.click_delete_spare_part_button()
                    spare_part_management_page.refresh()
                    assert (
                        spare_part_management_page.get_first_spare_part_name()
                        != first_spare_part_name
                    )
                    logger.info(f"{self.__class__.__name__} 测试用例执行成功")
                else:
                    logger.info("结束循环")
                    break
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-新增采日自采备件")
            raise e
