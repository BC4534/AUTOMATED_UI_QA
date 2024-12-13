import allure

from common.mylogger import Logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

logger = Logger()

@allure.title("工单列表-删除工单")
@allure.feature("工单管理-工单列表")
class TestWorkOrderList07(object):

    # 不勾选，直接点击删除
    def test_work_order_list_07_1(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_07_1()
            assert work_order_list_page.get_page_tip() == "请先勾选需要删除的数据"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 多条删除
    def test_work_order_list_07_2(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            old_first_work_order_number = work_order_list_page.get_first_work_order_number()
            work_order_list_page.test_work_order_list_07_2()
            work_order_list_page.click_select_all_button()
            new_first_work_order_number = work_order_list_page.get_first_work_order_number()
            assert old_first_work_order_number == new_first_work_order_number


            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

