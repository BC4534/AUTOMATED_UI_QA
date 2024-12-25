import time

from common.base_method import BasePage
from test_case_locator.operation_and_maintenance_workbench.management_role_locator.management_role_locator import \
    ManagementRoleLocator


class ManagementRolePage(BasePage):

    # 跳转至管理角色页面
    def switch_to_management_role_page(self):
        # class="ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-open ant-menu-submenu-selected" 展开时class属性值
        # class="ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-selected" 未展开时class属性值

        if self.get_operation_and_maintenance_workbench_basic_class() == 'ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-selected':
            self.click_element(ManagementRoleLocator.operation_and_maintenance_workbench)
        self.click_element(ManagementRoleLocator.management_role_loc)

    def get_operation_and_maintenance_workbench_basic_class(self):
        return self.get_attribute(ManagementRoleLocator.operation_and_maintenance_workbench_basic_loc, "class")
    # 切换数据维度
    def management_role_02(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.data_dimension_select_loc)
        time.sleep(0.5)
        self.click_element(ManagementRoleLocator.data_dimension_project_type_loc)
        time.sleep(1)
        self.click_element(ManagementRoleLocator.data_dimension_select_loc)
        time.sleep(0.5)
        self.click_element(ManagementRoleLocator.data_dimension_project_stage_loc)
        time.sleep(1)

    # 工单跳转 在途异常工单
    def management_role_03_1(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.abnormal_work_order_number_loc)
        time.sleep(2)
    # 工单跳转 在途其他工单
    def management_role_03_2(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.abnormal_other_work_order_number_loc)
        time.sleep(2)
    # 工单跳转 发起工单数量
    def management_role_03_3(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.initiate_work_order_number_loc)
        time.sleep(2)

    # 工单跳转，已执行工单
    def management_role_03_4(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.executed_work_order_number_loc)
        time.sleep(2)
    # 工单跳转 待执行工单总数
    def management_role_03_5(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.pending_work_order_number_loc)
        time.sleep(2)
    # 工单跳转 待执行异常工单
    def management_role_03_6(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.pending_abnormal_work_order_number_loc)
        time.sleep(2)

    # 任务过程看板 切换至周
    def management_role_04_1(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.week_loc)
        time.sleep(1)
    # 任务过程看板 切换至月
    def management_role_04_2(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.month_loc)
        time.sleep(1)

    # 人员任务统计部分用例
    def management_role_05_1(self):
        self.switch_to_management_role_page()
        self.click_element(ManagementRoleLocator.area_select_loc)
        time.sleep(1)
        self.click_element(ManagementRoleLocator.area_east_loc)
        time.sleep(1)
        self.click_element(ManagementRoleLocator.area_northwest_loc)
        time.sleep(1)
        self.click_element(ManagementRoleLocator.area_overseas_loc)
        time.sleep(1)
        self.click_element(ManagementRoleLocator.area_south_loc)
        time.sleep(1)
        self.click_element(ManagementRoleLocator.area_big_storage_operation_loc)
        time.sleep(1)

    # 取消 大储运维（宁夏）
    def management_role_05_2(self):
        self.click_element(ManagementRoleLocator.area_big_storage_operation_close_loc)
        time.sleep(2)

    # 点击 区域X按钮，取消所有选项
    def management_role_05_3(self):
        self.click_element(ManagementRoleLocator.area_cancel_all_loc)
        time.sleep(2)
    # 点击时间维度选择框 选择年
    def management_role_06_1(self):
        self.click_element(ManagementRoleLocator.time_dimension_loc)
        time.sleep(0.5)
        self.click_element(ManagementRoleLocator.time_dimension_year_loc)
        time.sleep(0.5)
    # 点击时间维度选择框，选择月
    def management_role_06_2(self):
        self.click_element(ManagementRoleLocator.time_dimension_loc)
        time.sleep(0.5)
        self.click_element(ManagementRoleLocator.time_dimension_month_loc)
        time.sleep(0.5)

    # # 读取时间维度选择框文本
    def get_time_dimension_text(self):
        return self.text(ManagementRoleLocator.time_dimension_loc)
    # 读取区域选择框文本值
    def get_area_select_text(self):
        return self.text(ManagementRoleLocator.area_select_loc)
    # 任务过程看板 断言元素
    def get_week_or_month_assert_text(self):
        return self.text(ManagementRoleLocator.week_or_month_assert_loc)


    # 获取在途项目看板按钮文本
    def get_in_transit_project_lookboard_text(self):
        return self.text(ManagementRoleLocator.in_transit_project_lookboard_loc)

    # 点击数据维度
    def click_data_dimension(self):
        self.click_element(ManagementRoleLocator.data_dimension_select_loc)
    # 点击数据维度 项目类型
    def click_data_dimension_project_type(self):
        self.click_element(ManagementRoleLocator.data_dimension_project_type_loc)
    # 点击数据维度 项目阶段
    def click_data_dimension_project_stage(self):
        self.click_element(ManagementRoleLocator.data_dimension_project_stage_loc)

    # 点击 在途异常工单数量按钮
    def click_pending_abnormal_work_order_number(self):
        self.click_element(ManagementRoleLocator.pending_abnormal_work_order_number_loc)
    # 点击 在途其他工单数量
    def click_abnormal_other_work_order_number(self):
        self.click_element(ManagementRoleLocator.abnormal_other_work_order_number_loc)

    # 点击 发起工单数量
    def click_initiate_work_order_number(self):
        self.click_element(ManagementRoleLocator.initiate_work_order_number_loc)
    # 点击 已执行工单总数
    def click_executed_work_order_number(self):
        self.click_element(ManagementRoleLocator.executed_work_order_number_loc)

    # 点击待执行工单数
    def click_pending_work_order_number(self):
        self.click_element(ManagementRoleLocator.pending_work_order_number_loc)
    # 点击待执行异常工单
    def click_pending_abnormal_work_order(self):
        self.click_element(ManagementRoleLocator.pending_abnormal_work_order_loc)

    # 点击 任务过程看板 周
    def click_week(self):
        self.click_element(ManagementRoleLocator.week_loc)
    # 点击 任务过程看板 月
    def click_month(self):
        self.click_element(ManagementRoleLocator.month_loc)

    # 点击 区域选择框




