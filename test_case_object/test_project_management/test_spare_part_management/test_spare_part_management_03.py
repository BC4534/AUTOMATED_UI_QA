import allure
from common.loggerhandler import logger
from test_case_page.project_management.spare_part_management_page import (
    SparePartManagementPage,
)

spare_part_inbound_data = {
    "part_attribute": "采日自采备件",
    "part_name": "UI测试备件名称-采日自采备件",
    "part_number": "0",
    "part_remark": "UI测试备件备注",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注",
}
spare_part_inbound_data2 = {
    "part_attribute": "采日自研备件",
    "part_name": "UI测试备件名称",
    "part_number": "0",
    "part_remark": "UI测试备件备注-采日自研备件",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注",
}
spare_part_inbound_data3 = {
    "part_attribute": "供应商预存备件",
    "part_name": "UI测试备件名称-供应商预存备件",
    "part_number": "0",
    "part_remark": "UI测试备件备注",
    "part_type": "EMS类附件",
    "part_vendor": "bms供应商",
    "part_warehouse": "上海备品仓",
    "part_inbound_remark": "UI测试备件入库备注",
}


@allure.feature("项目管理模块")
@allure.story("备件管理功能")
@allure.title("查看出入库记录")
class TestSparePartManagement03:

    @allure.description("查看出入库记录")
    def test_spare_part_management_03(self, login_driver):
        spare_part_management_page = SparePartManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            spare_part_management_page.switch_to_spare_part_management_page()
            spare_part_management_page.click_first_spare_part_view_inbound_record_button()
            assert (
                spare_part_management_page.get_spare_part_inbound_record_title()
                == "出入库记录"
            )
            spare_part_management_page.click_spare_part_inbound_record_close_button()
            logger.info(f"{self.__class__.__name__} 测试用例执行成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            spare_part_management_page.get_screenshot_png("备件管理-查看出入库记录")
            raise e
