import time

from common.base_method import BasePage
from test_case_locator.work_order_management.my_work_order.my_already_done_locator import MyAlreadyDoneLocator


class MyAlreadyDonePage(BasePage):

    # 切换至我的已办界面
    def switch_to_my_already_done_page(self):
        self.click_element(MyAlreadyDoneLocator.work_order_management_loc)
        time.sleep(0.5)
        self.click_element(MyAlreadyDoneLocator.my_work_order_loc)
        time.sleep(0.5)
        self.click_element(MyAlreadyDoneLocator.my_already_done_loc)
        time.sleep(0.5)

    # 获取我的已办元素 aria-selected="true" 属性值
    def get_my_already_done_element_aria_selected_value(self):
        return self.get_attribute(MyAlreadyDoneLocator.my_already_done_loc, 'aria-selected')

    # 获取处理状态下拉框的文本值
    def get_handle_status_text(self):
        return self.text(MyAlreadyDoneLocator.handle_status_loc)




