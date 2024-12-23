import allure

from common.loggerhandler import Logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

logger = Logger()
data = {
    "type":"巡检工单",
    "name":"工单名称",
    "description":"工单描述",
}
@allure.title("工单列表-新增取消验证")
@allure.feature("工单管理-工单列表")
class TestWorkOrderList04(object):
    """
    新增必填项 取消
    """
    # 新增 填写数据后，点击取消按钮
    def test_work_order_list_04_1(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            old_first_work_order = work_order_list_page.get_first_work_order_number()
            work_order_list_page.test_work_order_list_04_1(data["type"],data["name"],data["description"])
            new_first_work_order = work_order_list_page.get_first_work_order_number()
            assert work_order_list_page.get_manual_add_work_order_text() == "手工新增工单"
            assert old_first_work_order == new_first_work_order
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    # 新增 填写数据后，点击X按钮
    def test_work_order_list_04_2(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            old_first_work_order = work_order_list_page.get_first_work_order_number()
            work_order_list_page.test_work_order_list_04_2(data["type"], data["name"], data["description"])
            new_first_work_order = work_order_list_page.get_first_work_order_number()
            assert work_order_list_page.get_manual_add_work_order_text() == "手工新增工单"
            assert old_first_work_order == new_first_work_order
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
