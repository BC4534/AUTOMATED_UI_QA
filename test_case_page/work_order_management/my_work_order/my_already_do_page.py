import time

import allure
from selenium.webdriver.common.by import By

from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.work_order_management.my_work_order.my_already_done_locator import (
    MyAlreadyDoLocator,
)
from test_case_page.work_order_management.my_work_order.my_need_to_do_page import (
    MyNeedToDoPage,
)


class MyAlreadyDoPage(MyNeedToDoPage):

    @allure.step("判断工单管理是否展开")
    def _get_work_order_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            MyAlreadyDoLocator.work_order_management_expand_loc, "class"
        )

    @allure.step("判断是否在我的已办界面")
    def is_my_already_do_page(self):
        return self.get_attribute(MyAlreadyDoLocator.my_already_do_loc, "aria-selected")

    @allure.step("切换到我的已办界面")
    def switch_to_my_already_do_page(self):
        if self._get_work_order_management_is_expand():
            self.click_element(MyAlreadyDoLocator.work_order_management_loc)
        self.click_element(MyAlreadyDoLocator.my_work_order_loc)
        if self.is_my_already_do_page() == "false":
            self.click_element(MyAlreadyDoLocator.my_already_do_loc)
        time.sleep(1)

    @allure.step("输入工单接受人查询条件")
    def input_work_order_receiver(self, receiver):
        self.click_element(MyAlreadyDoLocator.work_order_receiver_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{receiver}"]'))
        self.random_sleep(0.5)

    @allure.step("输入当前处理人查询条件")
    def input_current_handler(self, current_handler):
        self.click_element(MyAlreadyDoLocator.current_handler_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{current_handler}"]'))
        self.random_sleep(0.5)

    @allure.step("获取第一个工单接收人")
    def get_first_work_order_receiver(self):
        try:
            return self.text(MyAlreadyDoLocator.first_work_order_receiver_loc)
        except Exception as e:
            logger.error("没有第一个工单接收人")
            return 1

    @allure.step("获取第一个当前处理人")
    def get_first_work_order_current_handler(self):
        try:
            return self.text(MyAlreadyDoLocator.first_work_order_current_handler_loc)
        except Exception as e:
            logger.error("没有第一个当前处理人")
            return 1

    @allure.step("获取查询条件当前处理状态")
    def get_handle_status_text(self):
        try:
            return self.text(MyAlreadyDoLocator.handle_current_status_loc)
        except Exception as e:
            logger.error("没有查询条件当前处理状态")
            return 1
