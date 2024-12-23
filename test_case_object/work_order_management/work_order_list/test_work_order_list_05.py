import allure

from common.loggerhandler import Logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

logger = Logger()

@allure.title("工单列表-查看详情")
@allure.feature("工单管理-工单列表")
class TestWorkOrderList01(object):


    def test_work_order_list_05(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_05()
            assert work_order_list_page.get_manual_add_work_order_text() == "手工新增工单"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

