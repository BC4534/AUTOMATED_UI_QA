import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage


@allure.feature("工单管理")
@allure.story("工单列表")
@allure.title("工单列表-删除工单")
class TestWorkOrderList06(object):

    @allure.description("删除,正常删除")
    def test_work_order_list_06_1(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_06_1()
            assert work_order_list_page.get_page_tip() == "删除成功！"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("删除,取消删除")
    def test_work_order_list_06_2(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            num = work_order_list_page.get_first_work_order_number()
            work_order_list_page.test_work_order_list_06_2()
            assert work_order_list_page.get_first_work_order_number() == num
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
