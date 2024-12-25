import time
from common.base_method import BasePage
from test_case_locator.operation_and_maintenance_workbench.execute_role_locator.execute_role_locator import \
    ExecuteRoleLocator


class ExecuteRolePage(BasePage):

    # 切换至执行角色界面
    def switch_to_execute_role_page(self):

        # class="ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-open ant-menu-submenu-selected" 展开时class属性值
        # class="ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-selected" 未展开时class属性值

        if self.get_operation_and_maintenance_workbench_basic_class() == 'ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-selected':
            self.click_element(ExecuteRoleLocator.operation_and_maintenance_workbench)
        self.click_element(ExecuteRoleLocator.execute_role_loc)
        time.sleep(0.5)

    # 获取运维工作台元素的class属性值
    def get_operation_and_maintenance_workbench_basic_class(self):
        return self.get_attribute(ExecuteRoleLocator.operation_and_maintenance_workbench_basic_loc, "class")


    # 数据维度切换用例
    def test_execute_role_02_1(self):
        self.switch_to_execute_role_page()
        self.click_data_dimension()
        time.sleep(1)
        self.click_data_dimension_project_type()
        time.sleep(1)

    def test_execute_role_02_2(self):
        self.click_data_dimension()
        time.sleep(1)
        self.click_data_dimension_project_stage()
        time.sleep(1)

    # 我的代办工单跳转
    # 工单总数跳转
    def test_execute_role_03_1(self):
        self.switch_to_execute_role_page()
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.work_order_number_loc)
        time.sleep(1)

    # 已执行工单跳转
    def test_execute_role_03_2(self):
        self.switch_to_execute_role_page()
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.executed_work_order_number_loc)
        time.sleep(1)

    # 待执行工单跳转
    def test_execute_role_03_3(self):
        self.switch_to_execute_role_page()
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.pending_work_order_number_loc)
        time.sleep(1)

    # 任务过程看板 切换至周
    def execute_role_04_1(self):
        self.switch_to_execute_role_page()
        self.click_element(ExecuteRoleLocator.week_loc)
        time.sleep(1)

    # 任务过程看板 切换至月
    def execute_role_04_2(self):
        self.switch_to_execute_role_page()
        self.click_element(ExecuteRoleLocator.month_loc)
        time.sleep(1)
    # 区域部分用例
    def execute_role_05_1(self):
        self.switch_to_execute_role_page()
        self.click_element(ExecuteRoleLocator.area_select_loc)
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.area_east_loc)
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.area_northwest_loc)
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.area_overseas_loc)
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.area_south_loc)
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.area_big_storage_operation_loc)
        time.sleep(1)

    # 取消 大储运维（宁夏）
    def execute_role_05_2(self):
        self.click_element(ExecuteRoleLocator.area_big_storage_operation_close_loc)
        time.sleep(2)

    # 点击 区域X按钮，取消所有选项
    def execute_role_05_3(self):
        # 鼠标移入 显示隐藏的全删按钮
        self.move_to_element(ExecuteRoleLocator.area_select_loc)
        time.sleep(1)
        self.click_element(ExecuteRoleLocator.area_cancel_all_loc)
        time.sleep(2)


    # 读取区域选择框文本值
    def get_area_select_text(self):
        return self.text(ExecuteRoleLocator.area_select_loc)

    # 任务过程看板 断言元素
    def get_week_or_month_assert_text(self):
        return self.text(ExecuteRoleLocator.week_or_month_assert_loc)
    # 获取在途任务看板元素文本
    def get_in_transit_project_lookboard_text(self):
        return self.text(ExecuteRoleLocator.in_transit_project_lookboard_loc)


    # 点击数据维度
    def click_data_dimension(self):
        self.click_element(ExecuteRoleLocator.data_dimension_select_loc)


    # 点击数据维度 项目类型
    def click_data_dimension_project_type(self):
        self.click_element(ExecuteRoleLocator.data_dimension_project_type_loc)
        # 点击数据维度 项目阶段


    def click_data_dimension_project_stage(self):
        self.click_element(ExecuteRoleLocator.data_dimension_project_stage_loc)


    # 获取数据维度元素文本
    def get_data_dimension_text(self):
        return self.text(ExecuteRoleLocator.data_dimension_select_loc)
