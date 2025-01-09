import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.my_work_order.my_already_do_page import MyAlreadyDoPage



@allure.feature("工单管理")
@allure.story("我的工单")
@allure.title("我的已办")
class TestMyAlreadyDo03:

    @allure.description("我的已办,详情按钮")
    def test_my_already_do_03(self,login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            if my_already_do_page.click_first_work_order_detail_button() != 1:
                assert my_already_do_page.get_work_order_detail_title() == "工单详情"
                my_already_do_page.close_work_order_detail_page()
                assert my_already_do_page.is_close_work_order_detail_page_success() == False
                logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

