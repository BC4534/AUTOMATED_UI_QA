import time
import allure
from selenium.webdriver.common.by import By
from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.work_order_management.my_work_order.my_need_to_do_locator import (
    MyNeedToDoLocator,
)
from test_case_locator.work_order_management.work_order_list_locator import (
    WorkOrderListLocator,
)
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage


class MyNeedToDoPage(WorkOrderListPage):

    @allure.step("判断工单管理是否展开")
    def _get_work_order_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            MyNeedToDoLocator.work_order_management_expand_loc, "class"
        )

    @allure.step("判断是否在我的待办界面")
    def is_my_need_to_do_page(self):
        return self.get_attribute(MyNeedToDoLocator.my_need_to_do_loc, "aria-selected")

    @allure.step("切换到我的待办界面")
    def switch_to_my_need_to_do_page(self):
        if self._get_work_order_management_is_expand():
            self.click_element(MyNeedToDoLocator.work_order_management_loc)
        self.click_element(MyNeedToDoLocator.my_work_order_loc)
        if self.is_my_need_to_do_page() == "false":
            self.click_element(MyNeedToDoLocator.my_need_to_do_loc)

    # 查询相关方法
    @allure.step("点击搜索按钮")
    def click_search_button(self):
        self.click_element(MyNeedToDoLocator.search_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击重置按钮")
    def click_reset_button(self):
        self.click_element(MyNeedToDoLocator.reset_button_loc)
        self.random_sleep(0.5)

    @allure.step("输入工单编号查询条件")
    def input_work_order_number(self, work_order_number):
        self.send_keys_by_clear_and_typing(
            MyNeedToDoLocator.work_order_number_input_loc, work_order_number
        )
        self.random_sleep(0.5)

    @allure.step("获取第一个工单编号")
    def get_first_work_order_number(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_number_loc)
        except:
            logger.warning("获取第一个工单编号失败")
            return 1

    @allure.step("获取第二个工单编号")
    def get_second_work_order_number(self):
        try:
            return self.text(MyNeedToDoLocator.second_work_order_number_loc)
        except:
            logger.warning("获取第二个工单编号失败")
            return 1

    @allure.step("输入工单名称查询条件")
    def input_work_order_name(self, work_order_name):
        self.send_keys(MyNeedToDoLocator.work_order_name_input_loc, work_order_name)
        self.random_sleep(0.5)

    @allure.step("获取第一个工单名称")
    def get_first_work_order_name(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_name_loc)
        except:
            logger.warning("获取第一个工单名称失败")
            return 1

    @allure.step("获取第二个工单名称")
    def get_second_work_order_name(self):
        try:
            return self.text(MyNeedToDoLocator.second_work_order_name_loc)
        except:
            logger.warning("获取第二个工单名称失败")
            return 1

    @allure.step("输入工单类型查询条件")
    def input_work_order_type(self, work_order_type):
        self.click_element(MyNeedToDoLocator.work_order_type_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{work_order_type}"]'))
        self.random_sleep(0.5)

    @allure.step("获取第一个工单类型")
    def get_first_work_order_type(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_type_loc)
        except:
            logger.warning("获取第一个工单类型失败")
            return 1

    @allure.step("输入工单关联项目查询条件")
    def input_association_project(self, association_project):
        self.click_element(MyNeedToDoLocator.association_project_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{association_project}"]'))
        self.random_sleep(0.5)

    @allure.step("获取第一个工单关联项目")
    def get_first_association_project(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_association_project_loc)
        except:
            logger.warning("获取第一个工单关联项目失败")
            return 1

    @allure.step("获取第二个工单关联项目")
    def get_second_association_project(self):
        try:
            return self.text(
                MyNeedToDoLocator.second_work_order_association_project_loc
            )
        except:
            logger.warning("获取第二个工单关联项目失败")
            return 1

    @allure.step("获取第一个工单计划开始时间")
    def get_first_plan_start_date(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_plan_start_time_loc)
        except:
            logger.warning("获取第一个工单计划开始时间失败")
            return 1

    @allure.step("获取第二个工单计划开始时间")
    def get_second_plan_start_date(self):
        try:
            return self.text(MyNeedToDoLocator.second_work_order_plan_start_time_loc)
        except:
            logger.warning("获取第二个工单计划开始时间失败")
            return 1

    @allure.step("获取第一个工单计划结束时间")
    def get_first_plan_end_date(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_plan_end_time_loc)
        except:
            logger.warning("获取第一个工单计划结束时间失败")
            return 1

    @allure.step("获取第二个工单计划结束时间")
    def get_second_plan_end_date(self):
        try:
            return self.text(MyNeedToDoLocator.second_work_order_plan_end_time_loc)
        except:
            logger.warning("获取第二个工单计划结束时间失败")
            return 1

    @allure.step("输入工单计划开始时间查询条件")
    def input_plan_start_date(self, plan_start_date):
        self.input_time(plan_start_date, MyNeedToDoLocator.plan_start_date_input_loc)

    @allure.step("输入工单计划结束时间查询条件")
    def input_plan_end_date(self, plan_end_date):
        self.input_time(plan_end_date, MyNeedToDoLocator.plan_end_date_input_loc)

    @allure.step("获取第一个工单所属区域")
    def get_first_work_order_belong_area(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_belong_area_loc)
        except:
            logger.warning("获取第一个工单所属区域失败")
            return 1

    @allure.step("输入工单所属区域查询条件")
    def input_work_order_belong_area(self, work_order_belong_area):
        self.click_element(MyNeedToDoLocator.work_order_belong_area_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{work_order_belong_area}"]'))
        self.random_sleep(0.5)

    @allure.step("输入工单发起人查询条件")
    def input_work_order_initiator(self, work_order_initiator):
        self.click_element(MyNeedToDoLocator.work_order_initiator_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{work_order_initiator}"]'))
        self.random_sleep(0.5)

    @allure.step("获取第一个工单发起人")
    def get_first_work_order_initiator(self):
        try:
            return self.text(MyNeedToDoLocator.first_work_order_initiator_loc)
        except:
            logger.warning("获取第一个工单发起人失败")
            return 1

    # 编辑操作
    @allure.step("点击第一个工单详情按钮")
    def click_first_work_order_detail_button(self):
        try:
            self.click_element(MyNeedToDoLocator.first_work_order_detail_button_loc)
        except:
            logger.warning("点击第一个工单详情按钮失败")
            return 1

    @allure.step("获取工单详情页面标题")
    def get_work_order_detail_title(self):
        try:
            return self.text(MyNeedToDoLocator.work_order_detail_title_loc)
        except:
            logger.warning("获取工单详情页面标题失败")
            return 1

    @allure.step("关闭工单详情页面")
    def close_work_order_detail_page(self):
        try:
            self.click_element(MyNeedToDoLocator.work_order_detail_close_button_loc)
        except:
            logger.warning("关闭工单详情页面失败")
            return 1

    @allure.step("判断是否关闭工单详情页面成功")
    def is_close_work_order_detail_page_success(self):
        try:
            self.visibility_of_element_located(
                MyNeedToDoLocator.work_order_detail_mask_loc, 5, 1
            )
            return True
        except:
            logger.warning("判断是否关闭工单详情页面成功失败")
            return False

    # 删除工单
    @allure.step("点击第一个工单删除按钮")
    def click_first_work_order_delete_button(self):
        try:
            self.click_element(MyNeedToDoLocator.first_work_order_delete_button_loc)
        except:
            logger.warning("点击第一个工单删除按钮失败")
            return 1

    @allure.step("点击确认删除按钮")
    def click_confirm_delete_button(self):
        self.click_element(MyNeedToDoLocator.confirm_delete_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击取消删除按钮")
    def click_cancel_delete_button(self):
        self.click_element(MyNeedToDoLocator.cancel_delete_button_loc)

    @allure.step("新增一个工单,用于删除")
    def add_work_order_for_delete(self):
        self.switch_to_work_order_list_page()
        self.test_work_order_list_02(
            "巡检工单", "UI测试用于我的工单删除功能", "UI测试用于我的工单删除功能"
        )
        self.switch_to_my_need_to_do_page()
