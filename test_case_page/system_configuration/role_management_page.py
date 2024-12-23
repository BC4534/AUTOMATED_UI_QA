import time
from common.base_method import BasePage
from test_case_locator.system_configuration.role_management_locator.role_management_locator import RoleManagementLocator
from common.loggerhandler import logger


class RoleManagementPage(BasePage):

    # 角色管理，页面跳转
    def role_management_01(self):
        self.click_element(RoleManagementLocator.system_config_loc)
        time.sleep(0.5)
        self.click_element_by_js(RoleManagementLocator.role_management_loc)

    # 角色管理-新增-正常新增
    def role_management_02(self, name, remark):
        self.click_add_role_button()
        self.fill_add_role_data(name, remark)
        self.click_confirm_button()

    # 新增必填项效验
    def role_management_03(self):
        self.role_management_01()
        self.click_add_role_button()
        self.click_confirm_button()
    # 正常新增，填写数据后点关闭
    def role_management_04(self, name, remark):
        self.click_add_role_button()
        self.fill_add_role_data(name, remark)
        self.click_close_button()
        time.sleep(1)

    # 正常新增，填写数据后点取消按钮
    def role_management_05(self, name, remark):
        self.click_add_role_button()
        self.fill_add_role_data(name, remark)
        self.click_cancel_button()
        time.sleep(1)

    # 编辑已有角色信息，再点击新增
    def role_management_06(self):
        self.role_management_01()
        self.click_first_data_edit_button()
        self.click_cancel_button()
        self.click_add_role_button()
        return self.text(RoleManagementLocator.add_role_name_input_loc)

    # 勾选已有数据，新增
    def role_management_07(self, name, remark):
        self.click_first_data_checkbox()
        self.click_add_role_button()
        self.fill_add_role_data(name, remark)
        self.click_confirm_button()

    # 删除角色，直接点击删除按钮
    def role_management_08(self):
        self.role_management_01()
        self.click_batch_delete_button()
    # 删除角色 ，单条
    def role_management_09(self, name, remark):
        self.click_add_role_button()
        self.fill_add_role_data(name, remark)
        time.sleep(0.5)
        self.click_confirm_button()
        time.sleep(0.5)
        self.test_case_data_recover()
    # 重复新增
    def role_management_10(self, name, remark):
        self.role_management_01()
        self.role_management_02(name, remark)
        self.role_management_02(name, remark)

    # 批量删除，多条
    def role_management_11(self, name, remark):
        self.click_add_role_button()
        self.fill_add_role_data(name, remark)
        time.sleep(0.5)
        self.click_confirm_button()
        time.sleep(0.5)
    # 针对 role_management_11的删除
    def role_management_11_delete(self):
        time.sleep(0.5)
        self.click_first_data_checkbox()
        time.sleep(0.5)
        self.click_first_data_checkbox()
        time.sleep(0.5)
        self.click_batch_delete_button()
        time.sleep(1)
        self.click_confirm_batch_delete_button()
        time.sleep(0.5)

    # 全选 删除
    def role_management_12(self):
        self.role_management_01()
        self.click_all_checkbox()
        self.click_batch_delete_button()
        time.sleep(0.5)
        self.click_confirm_batch_delete_button()
        time.sleep(0.5)

    # 编辑
    def role_management_13(self, name, remark):
        self.click_first_data_edit_button()
        self.fill_add_role_data(name, remark)

    # 验证编辑页面打开是否正确
    def role_management_14(self):
        self.role_management_01()
        self.click_first_data_edit_button()
        return self.text(RoleManagementLocator.page_name_loc)


    # 验证新增页面打开是否正确
    def role_management_15(self):
        self.role_management_01()
        self.click_add_role_button()
        return self.text(RoleManagementLocator.page_name_loc)

    # 验证查询功能
    def role_management_16(self,name):
        self.search_role_name(name)

    # 想橘色名称查询框输入查询条件
    def search_role_name(self, name):
        self.send_keys(RoleManagementLocator.select_role_name_input_loc, name)

    # 读取角色名称查询框输入值
    def get_select_role_name_input(self):
        return self.text(RoleManagementLocator.select_role_name_input_loc)
    # 点击全选按钮
    def click_all_checkbox(self):
        self.click_element(RoleManagementLocator.all_role_checkbox_loc)
    # 点击第一条数据的编辑按钮
    def click_first_data_edit_button(self):
        self.click_element(RoleManagementLocator.first_role_edit_button_loc)

    # 勾选第一条数据，新增角色
    def click_first_data_checkbox(self):
        self.click_element(RoleManagementLocator.first_role_checkbox_loc)
    # 获取新增角色界面断言元素的style属性值。
    def get_add_role_style(self):
        return self.get_attribute(RoleManagementLocator.role_page_assert_loc, "style")
    # 新增角色，必填项效验  角色名称提示信息
    def get_add_role_name_required(self):
        return self.text(RoleManagementLocator.add_role_name_required_loc)
    # 新增角色，必填项效验，角色说明提示信息
    def get_add_role_remark_required(self):
        return self.text(RoleManagementLocator.add_role_remark_required_loc)
    # 新增角色数据恢复
    def test_case_data_recover(self):
        self.refresh()
        self.click_element(RoleManagementLocator.first_role_checkbox_loc)
        time.sleep(0.5)
        self.click_batch_delete_button()
        time.sleep(0.5)
        self.click_confirm_batch_delete_button()
        time.sleep(0.5)


    # 新增角色数据填写步骤
    def fill_add_role_data(self, role_name, remark):
        self.select_all(RoleManagementLocator.add_role_name_input_loc)
        self.delete(RoleManagementLocator.add_role_name_input_loc)
        self.send_keys(RoleManagementLocator.add_role_name_input_loc, role_name)
        self.click_element(RoleManagementLocator.permission_config_operation_loc)
        self.click_element(RoleManagementLocator.permission_config_work_order_loc)
        self.click_element(RoleManagementLocator.permission_config_project_loc)
        self.click_element(RoleManagementLocator.permission_config_tool_loc)
        self.click_element(RoleManagementLocator.permission_config_knowledge_loc)
        self.click_element(RoleManagementLocator.permission_config_system_loc)
        self.select_all(RoleManagementLocator.add_role_remark_input_loc)
        self.delete(RoleManagementLocator.add_role_remark_input_loc)
        self.send_keys_by_clear(RoleManagementLocator.add_role_remark_input_loc, remark)

    # 点击确认按钮
    def click_confirm_button(self):
        time.sleep(0.5)
        self.click_element(RoleManagementLocator.confirm_button_loc)


    # 点击取消按钮
    def click_cancel_button(self):
        self.click_element(RoleManagementLocator.cancel_button_loc)

    # 点击X按钮
    def click_close_button(self):
        self.click_element(RoleManagementLocator.close_button_loc)


    # 获取角色管理界面，新增角色按钮文本值
    def get_add_role_button_text(self):
        try:
            return self.text(RoleManagementLocator.add_role_button_loc)
        except Exception as e:
            raise e
    # 获取第一个角色名称
    def get_first_role_name(self):
        time.sleep(2)
        return self.text(RoleManagementLocator.first_role_name_loc)
    # 获取第二个角色名称
    def get_second_role_name(self):
        time.sleep(2)
        return self.text(RoleManagementLocator.second_role_name_loc)
    #------------界面按基础钮操作----------------
    # 点击新增角色按钮
    def click_add_role_button(self):
        self.click_element(RoleManagementLocator.add_role_button_loc)
    # 点击编辑按钮
    def click_edit_button(self):
        pass
    # 点击批量删除按钮
    def click_batch_delete_button(self):
        self.click_element(RoleManagementLocator.batch_delete_button_loc)

    # 点击确认批量删除按钮
    def click_confirm_batch_delete_button(self):
        self.click_element(RoleManagementLocator.confirm_batch_delete_button_loc)

    # 点击取消批量删除按钮
    def click_cancel_batch_delete_button(self):
        self.click_element(RoleManagementLocator.cancel_batch_delete_button_loc)

    # 点击搜索按钮
    def click_search_button(self):
        self.click_element(RoleManagementLocator.search_button_loc)

    # 点击重置按钮
    def click_reset_button(self):
        self.click_element(RoleManagementLocator.reset_button_loc)

    #----------------------------#
    # 获取界面弹窗提示信息
    def get_page_tip(self):
        try:
            return self.text(RoleManagementLocator.page_tip_loc)
        except Exception as e:
            raise e
