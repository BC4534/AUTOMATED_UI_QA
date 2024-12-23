import allure

from common.loggerhandler import Logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

logger = Logger()

@allure.title("工单列表-删除工单")
@allure.feature("工单管理-工单列表")
class TestWorkOrderList06(object):

    # 单条删除
    def test_work_order_list_06_1(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_06_1()
            assert work_order_list_page.get_page_tip() == "删除成功"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 多条删除
    def test_work_order_list_06_2(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_06_2()
            assert work_order_list_page.get_page_tip() == "删除成功"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

