import allure

from common.loggerhandler import logger
from test_case_page.work_order_management.my_work_order.my_need_to_do_page import (
    MyNeedToDoPage,
)


@allure.feature("工单管理")
@allure.story("我的工单")
@allure.title("我的待办")
class TestMyNeedToDo03:
    @allure.description("我的代办,详情页面展示")
    def test_my_need_to_do_03(self, login_driver):
        my_need_to_do_page = MyNeedToDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_need_to_do_page.switch_to_my_need_to_do_page()
            if my_need_to_do_page.click_first_work_order_detail_button() != 1:
                assert my_need_to_do_page.get_work_order_detail_title() == "工单详情"
                my_need_to_do_page.close_work_order_detail_page()
                assert (
                    my_need_to_do_page.is_close_work_order_detail_page_success()
                    == False
                )
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_need_to_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
