import time

from common.base_method import BasePage
from test_case_locator.work_order_management.my_work_order.my_need_to_do_locator import MyNeedToDoLocator


class MyNeedToDoPage(BasePage):

    # 跳转至我的代办页面
    def switch_to_my_need_to_do_page(self):
        self.click_element(MyNeedToDoLocator.work_order_management_loc)
        self.click_element(MyNeedToDoLocator.my_work_order_loc)
        time.sleep(0.5)
        # self.click_element(MyNeedToDoLocator.my_need_to_do_loc)

    # 获取我的代办元素 aria-selected="true" 属性值
    def get_my_need_to_do_element_aria_selected_value(self):
        return self.get_attribute(MyNeedToDoLocator.my_need_to_do_loc, 'aria-selected')

    # 获取工单类型。系统异常工单文本值
    def get_system_abnormal_work_order_type_text(self):
        return self.text(MyNeedToDoLocator.system_abnormal_work_order_loc)
    # 获取工单类型。手工异常工单文本值
    def get_manual_abnormal_work_order_type_text(self):
        return self.text(MyNeedToDoLocator.manual_abnormal_work_order_loc)

