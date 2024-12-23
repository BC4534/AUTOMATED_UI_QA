import allure

from common.loggerhandler import Logger
from test_case_page.work_order_management.my_work_order.my_need_to_do_page import MyNeedToDoPage

logger = Logger()

@allure.title("测试我的待办页面")
@allure.feature("我的工单")
class TestMyWorkOrder01:
    def test_my_work_order_01(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_need_to_do_page = MyNeedToDoPage(login_driver)
            my_need_to_do_page.switch_to_my_need_to_do_page()
            assert my_need_to_do_page.get_my_need_to_do_element_aria_selected_value() == "true"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_need_to_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

