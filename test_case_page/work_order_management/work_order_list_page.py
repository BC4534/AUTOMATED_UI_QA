import time

import allure
from selenium.webdriver import ActionChains

from common.base_method import BasePage
from test_case_locator.system_configuration.account_management_locator.account_management_locator import \
    AccountManagementLocator
from test_case_locator.work_order_management.work_order_list_locator import WorkOrderListLocator


class WorkOrderListPage(BasePage):

    # 页面跳转
    def switch_to_work_order_list_page(self):
        self.click_element(WorkOrderListLocator.work_order_management_loc)
        self.click_element(WorkOrderListLocator.work_order_list_loc)

    # 手工新增巡检工单
    def test_work_order_list_02(self, order_type, name, description):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.manual_add_work_order_loc)
        time.sleep(0.5)
        self.select_work_order_type(order_type)
        self.fill_work_order_data(name, description)
        # 确认 单独点击不可以实现手动点击效果，两个点击都加上
        # element = self.visibility_of_element_located(WorkOrderListLocator.confirm_button_loc)
        # self.execute_script("arguments[0].click();", element)
        # self.click_element(WorkOrderListLocator.confirm_button_loc)
        # self.action_chains_click(WorkOrderListLocator.confirm_button_loc)
        # 双击
        self.double_click(WorkOrderListLocator.confirm_button_loc)

    # 新增 必填项效验
    def test_work_order_list_03(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.manual_add_work_order_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.confirm_button_loc)
        time.sleep(0.5)

    # 新增 点击取消按钮
    def test_work_order_list_04_1(self, order_type, name, description):
        # self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.manual_add_work_order_loc)
        time.sleep(0.5)
        self.select_work_order_type(order_type)
        self.fill_work_order_data(name, description)
        self.click_element(WorkOrderListLocator.cancel_button_loc)

    # 新增 点击x按钮
    def test_work_order_list_04_2(self, order_type, name, description):
        # self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.manual_add_work_order_loc)
        time.sleep(0.5)
        self.select_work_order_type(order_type)
        self.fill_work_order_data(name, description)
        self.click_element(WorkOrderListLocator.close_button_loc)

    # 查看详情
    def test_work_order_list_05(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.first_data_detail_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.detail_close_button_loc)
        time.sleep(0.5)

    # 单条数据删除
    def test_work_order_list_06_1(self):
        self.switch_to_work_order_list_page()
        self.test_work_order_list_02('巡检工单', 'test_work_order_list_06_1', 'test_work_order_list_06')
        self.refresh()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.first_data_checkbox_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.delete_work_order_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.confirm_button_loc)
        time.sleep(0.5)

    #  多条批量删除
    def test_work_order_list_06_2(self):
        self.switch_to_work_order_list_page()
        self.test_work_order_list_02('巡检工单', 'test_work_order_list_06_2_1', 'test_work_order_list_06')
        self.test_work_order_list_02('巡检工单', 'test_work_order_list_06_2_2', 'test_work_order_list_06')
        self.refresh()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.second_data_checkbox_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.first_data_checkbox_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.delete_work_order_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.confirm_button_loc)
        time.sleep(0.5)

    # 不勾选数据直接点击删除
    def test_work_order_list_07_1(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.delete_work_order_loc)

    # 删除数据，点击取消删除按钮
    def test_work_order_list_07_2(self):
        # self.switch_to_work_order_list_page()
        self.click_select_all_button()
        self.click_element(WorkOrderListLocator.delete_work_order_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.cancel_button_loc)

    # 全选 验证
    def test_work_order_list_08_1(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_select_all_button()

    # 单选 验证
    def test_work_order_list_08_2(self):

        self.refresh()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.second_data_checkbox_loc)
        time.sleep(0.5)

    # 搜索功能验证
    # 发布时间 验证
    def test_work_order_list_09_1(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.publish_time_expand_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.start_time_1_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.next_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.next_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.end_time_28_button_loc)
        time.sleep(0.5)

    # 处理状态搜索框
    # 未完成
    def test_work_order_list_09_2_1(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_handle_status_button_loc()
        time.sleep(0.5)
        self.click_handle_status_unfinished_loc()
        time.sleep(0.5)

    # 已完成
    def test_work_order_list_09_2_2(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_handle_status_button_loc()
        time.sleep(0.5)
        self.click_handle_status_finished_loc()
        time.sleep(0.5)

    # 工单编号搜索
    def test_work_order_list_09_3(self):
        self.switch_to_work_order_list_page()
        first_work_order = self.get_first_work_order_number()
        time.sleep(0.5)
        self.send_keys(WorkOrderListLocator.work_order_number_input_loc, first_work_order)
        time.sleep(0.5)
        self.click_search_button_loc()
        return first_work_order

    # 工单名称搜搜
    def test_work_order_list_09_4(self):
        self.switch_to_work_order_list_page()
        first_work_order = self.get_first_work_order_name()
        time.sleep(0.5)
        self.send_keys(WorkOrderListLocator.select_work_order_name_input_loc, first_work_order)
        time.sleep(0.5)
        self.click_search_button_loc()
        return first_work_order

    # 关联项目搜索
    def test_work_order_list_09_5(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.select_association_project_select_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.association_project_first_option_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    # 工单类型搜索
    def test_work_order_list_09_6_1(self):  # 定期标准巡检工单
        self.click_element(WorkOrderListLocator.work_order_type_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.regular_standard_inspection_work_order_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    def test_work_order_list_09_6_2(self):  # 手工标准巡检工单
        self.click_element(WorkOrderListLocator.work_order_type_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.manual_standard_inspection_work_order_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    def test_work_order_list_09_6_3(self):  # 实施工单
        self.click_element(WorkOrderListLocator.work_order_type_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.implement_work_order_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    def test_work_order_list_09_6_4(self):  # system_abnormal_work_order_loc
        self.click_element(WorkOrderListLocator.work_order_type_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.system_abnormal_work_order_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    def test_work_order_list_09_6_5(self):  # 手工异常工单
        self.click_element(WorkOrderListLocator.work_order_type_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.manual_abnormal_work_order_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    def test_work_order_list_09_6_6(self):  # 手工其他工单
        self.click_element(WorkOrderListLocator.work_order_type_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.manual_non_standard_inspection_work_order_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    def test_work_order_list_09_6_7(self):  # 手工其他工单
        self.click_element(WorkOrderListLocator.work_order_type_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.other_work_order_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    # 计划开始时间
    def test_work_order_list_09_7(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.plan_start_time_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.plan_time_next_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.plan_time_next_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.start_time_1_button_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    # 计划结束时间搜索
    def test_work_order_list_09_8(self):
        self.switch_to_work_order_list_page()
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.plan_end_time_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.previous_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.plan_time_next_year_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.plan_time_next_month_button_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.start_time_28_button_loc)
        time.sleep(0.5)
        self.click_search_button_loc()

    # 获取计划开始时间搜索框文本
    def get_plan_start_time_text(self):
        return self.get_attribute(WorkOrderListLocator.plan_start_time_button_loc, 'value')
        # return self.text(WorkOrderListLocator.plan_start_time_button_loc)
    # 获取计划结束时间搜索框文本
    def get_plan_end_time_text(self):
        return self.get_attribute(WorkOrderListLocator.plan_end_time_button_loc, 'value')
        # return self.text(WorkOrderListLocator.plan_end_time_button_loc)
    # 获取第一条数据的计划开始时间
    def get_first_data_plan_start_time(self):
        return self.text(WorkOrderListLocator.first_data_plan_start_time_loc)

    # 获取第一条数据的计划结束时间
    def get_first_data_plan_end_time(self):
        return self.text(WorkOrderListLocator.first_data_plan_end_time_loc)

    # 获取搜索框工单类型文本
    def get_work_order_type_text(self):
        return self.text(WorkOrderListLocator.work_order_type_loc)

    # 获取第一条数据的工单类型
    def get_first_data_work_order_type_text(self):
        return self.text(WorkOrderListLocator.first_data_work_order_type_loc)

    # 获取关联项目文本
    def get_association_project_text(self):
        return self.text(WorkOrderListLocator.select_association_project_text_loc)

    # 获取第一条数据关联项目文本
    def get_first_data_association_project_text(self):
        return self.text(WorkOrderListLocator.first_data_association_project_loc)

    # 获取第一条数据的处理状态文本
    def get_first_data_handle_status_text(self):
        return self.text(WorkOrderListLocator.first_data_handle_status_loc)

    # # 点击处理状态按钮
    def click_handle_status_button_loc(self):
        self.click_element(WorkOrderListLocator.handle_status_select_loc)

    # 选择 处理状态的未完成按钮
    def click_handle_status_unfinished_loc(self):
        self.click_element(WorkOrderListLocator.handle_status_unfinished_loc)

    # 选择 处理状态的已完成按钮
    def click_handle_status_finished_loc(self):
        self.click_element(WorkOrderListLocator.handle_status_finished_loc)

    # 点击搜索按钮
    def click_search_button_loc(self):
        self.click_element(WorkOrderListLocator.search_button_loc)
        time.sleep(0.5)

    # 点击重置按钮
    def click_reset_button_loc(self):
        self.click_element(WorkOrderListLocator.reset_button_loc)
        time.sleep(0.5)

    # 点击清除时间按钮
    def click_clear_time_button_loc(self):
        self.move_to_element(WorkOrderListLocator.publish_time_expand_button_loc)
        self.click_element(WorkOrderListLocator.clear_time_button_loc)
        time.sleep(0.5)

    # 获取勾选复选框后的数量显示
    def get_select_number_text(self):
        return self.text(WorkOrderListLocator.checkbox_number_loc)

    # 点击全选按钮
    def click_select_all_button(self):
        self.click_element(WorkOrderListLocator.select_all_loc)
        time.sleep(0.5)

    # 获取第一个工单编号
    def get_first_work_order_number(self):
        return self.text(WorkOrderListLocator.first_work_order_number_loc)

    # 获取第一个工单名称
    def get_first_work_order_name(self):
        return self.text(WorkOrderListLocator.first_data_work_order_name_loc)

    # 工单类型必填项验证文本
    def get_work_order_type_required_text(self):
        return self.text(WorkOrderListLocator.work_order_type_select_loc)

    # 工单名称必填项验证文本
    def get_work_order_name_required_text(self):
        return self.text(WorkOrderListLocator.work_order_name_required_loc)

    # 工单描述必填项验证文本
    def get_work_order_description_required_text(self):
        return self.text(WorkOrderListLocator.work_order_description_required_loc)

    # 关联项目必选项验证文本
    def get_association_project_required_text(self):
        return self.text(WorkOrderListLocator.association_project_required_loc)

    # 负责人必选项验证文本
    def get_responsible_person_required_text(self):
        return self.text(WorkOrderListLocator.responsible_person_required_loc)

    # 开始时间必选项验证文本
    def get_plan_start_time_required_text(self):
        return self.text(WorkOrderListLocator.plan_start_time_required_loc)

    # 结束时间必选项验证文本
    def get_plan_end_time_required_text(self):
        return self.text(WorkOrderListLocator.plan_end_time_required_loc)

    # 测试新增数据恢复
    def test_case_data_recovered(self):
        self.refresh()
        time.sleep(1)
        self.click_element(WorkOrderListLocator.first_data_checkbox_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.delete_work_order_loc)
        time.sleep(0.5)
        self.click_element(WorkOrderListLocator.confirm_button_loc)
        time.sleep(0.5)

    # 获取界面提示
    def get_page_tip(self):
        return self.text(WorkOrderListLocator.page_tip_loc)

    # 选择工单类型
    def select_work_order_type(self, order_type: str):
        self.click_element(WorkOrderListLocator.work_order_type_select_loc)
        if order_type == '巡检工单':
            self.click_element(WorkOrderListLocator.work_order_type_inspection_loc)
        elif order_type == '异常工单':
            self.click_element(WorkOrderListLocator.work_order_type_abnormal_loc)
        else:
            self.click_element(WorkOrderListLocator.work_order_type_other_loc)

    # 填写工单数据流程
    def fill_work_order_data(self, name, description):
        self.send_keys(WorkOrderListLocator.work_order_name_input_loc, name)
        time.sleep(0.5)
        self.send_keys(WorkOrderListLocator.work_order_description_input_loc, description)
        time.sleep(0.5)  # 关联项目
        self.click_element(WorkOrderListLocator.association_project_select_loc)
        self.click_element(WorkOrderListLocator.association_project_first_loc)
        time.sleep(0.5)  # 选择负责人
        self.click_element(WorkOrderListLocator.responsible_person_select_loc)
        self.click_element(WorkOrderListLocator.responsible_person_first_loc)
        time.sleep(0.5)  # 计划开始时间
        self.click_element(WorkOrderListLocator.plan_start_time_loc)
        self.click_element(WorkOrderListLocator.plan_start_time_now_loc)
        time.sleep(1)  # 计划结束时间
        self.click_element(WorkOrderListLocator.plan_end_time_loc)
        self.click_element(WorkOrderListLocator.plan_end_time_now_loc)
        time.sleep(0.5)

    # 获取手工新增工单 按钮文本
    def get_manual_add_work_order_text(self):
        return self.text(WorkOrderListLocator.manual_add_work_order_loc)

    # 获取工单类型 系统异常工单元素文本 ，
    def get_system_abnormal_work_order_type_text(self):
        return self.text(WorkOrderListLocator.system_abnormal_work_order_loc)

    # 获取工单类型 手工异常工单元素文本 ，
    def get_manual_abnormal_work_order_type_text(self):
        return self.text(WorkOrderListLocator.manual_abnormal_work_order_loc)

    # 获取工单类型 定期标准巡检工单文本
    def get_regular_standard_inspection_work_order_type_text(self):
        return self.text(WorkOrderListLocator.regular_standard_inspection_work_order_loc)

    # 获取工单类型 手工标准巡检工单文本
    def get_manual_standard_inspection_work_order_type_text(self):
        return self.text(WorkOrderListLocator.manual_standard_inspection_work_order_loc)

    # 获取工单类型 手工非标巡检工单文本
    def get_manual_non_standard_inspection_work_order_type_text(self):
        return self.text(WorkOrderListLocator.manual_non_standard_inspection_work_order_loc)

    # 获取工单类型 其他工单文本
    def get_other_work_order_type_text(self):
        return self.text(WorkOrderListLocator.other_work_order_loc)

    # 获取工单类型 实施工单
    def get_implement_work_order_type_text(self):
        return self.text(WorkOrderListLocator.implement_work_order_loc)

    # 获取工单发起人-系统管理员元素文本，把工单发起人也加在方法中，方便调用
    def get_initiator_of_work_order_system_administrator_text(self):
        return self.text(WorkOrderListLocator.initiator_of_work_order_system_administrator_loc)

    # 获取 处理状态，已完成元素文本
    def get_handle_status_completed_text(self):
        return self.text(WorkOrderListLocator.handle_status_completed_loc)

    @allure.step('获取工单列表界面,工单编号输入框values值')
    def get_work_order_number_input_values(self):
        return self.get_attribute(WorkOrderListLocator.work_order_number_input_loc, 'value')
