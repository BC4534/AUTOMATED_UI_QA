import allure
import pytest

from common.loggerhandler import logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

data1 = {
    "type": "巡检工单",
    "name": "UI测试新增巡检工单",
    "description": "UI测试新增巡检工单描述",
}
data2 = {
    "type": "异常工单",
    "name": "UI测试新增异常工单",
    "description": "异常工单描述",
}
data3 = {
    "type": "其他工单",
    "name": "UI测试新增其他工单",
    "description": "其他工单描述",
}


@allure.feature("工单管理")
@allure.story("工单列表")
@allure.title("手工新增工单")
class TestWorkOrderList02(object):

    # 手工新增巡检工单
    @allure.description("手工新增巡检工单-三种类型工单")
    @pytest.mark.parametrize("data", [data1, data2, data3])
    def test_work_order_list_02_1(self, login_driver, data):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_02(
                data["type"], data["name"], data["description"]
            )
            assert work_order_list_page.get_page_tip() == "新增成功"
            work_order_list_page.test_case_data_recovered()
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
