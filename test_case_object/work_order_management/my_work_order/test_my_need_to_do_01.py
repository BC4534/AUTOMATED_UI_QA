import allure

from common.loggerhandler import logger
from test_case_page.work_order_management.my_work_order.my_need_to_do_page import (
    MyNeedToDoPage,
)


@allure.feature("工单管理")
@allure.story("我的工单")
@allure.title("我的待办")
class TestMyNeedToDo01:
    @allure.description("切换至我的待办页")
    def test_my_need_to_do_01(self, login_driver):
        my_need_to_do_page = MyNeedToDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_need_to_do_page.switch_to_my_need_to_do_page()
            assert my_need_to_do_page.is_my_need_to_do_page() == "true"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_need_to_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
