import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.my_work_order.my_already_do_page import MyAlreadyDoPage



@allure.feature("工单管理")
@allure.story("我的工单")
@allure.title("我的已办")
class TestMyAlreadyDo02:
    def test_my_already_do_02(self,login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            order_name = my_already_do_page.get_first_work_order_name()
            my_already_do_page.click_first_work_order_delete_button()
            my_already_do_page.click_cancel_delete_button()
            assert my_already_do_page.get_first_work_order_name() == order_name
            # my_already_do_page.click_first_work_order_delete_button() # 注释掉,防止误删
            # my_already_do_page.click_confirm_delete_button()
            # assert my_already_do_page.get_first_work_order_name() != order_name
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

