import time

from common.loggerhandler import logger
from test_case_locator.project_management.electronic_archives_locator.supplier_maintenance_locator import \
    SupplierMaintenanceLocator
from test_case_page.project_management.electronic_archives_page.electronic_archives_page import ElectronicArchivesPage


class SupplierMaintenancePage(ElectronicArchivesPage):

    # 进入供应商维护页面
    def switch_to_supplier_maintenance(self):
        self.refresh()
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_button_loc)
        self.random_sleep(0.5)

    # 获取供应商维护页面标题
    def get_supplier_maintenance_title(self):
        return self.text(SupplierMaintenanceLocator.supplier_maintenance_title_loc)

    # 点击新增按钮
    def supplier_maintenance_click_add_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_add_button_loc)
        self.random_sleep(0.5)

    # 点击取消按钮
    def supplier_maintenance_click_cancel_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_cancel_button_loc)
        self.random_sleep(0.5)

    # 点击关闭按钮
    def supplier_maintenance_click_close_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_close_button_loc)
        self.random_sleep(0.5)
    # 点击确认按钮
    def supplier_maintenance_click_confirm_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_confirm_button_loc)
        self.random_sleep(0.5)

    # 点击保存按钮
    def supplier_maintenance_click_save_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_save_button_loc)
        self.random_sleep(0.5)
    # 点击清空按钮
    def supplier_maintenance_click_clear_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_clear_button_loc)
        self.random_sleep(0.5)

    # 点击编辑按钮
    def supplier_maintenance_click_edit_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_edit_button_loc)
        self.random_sleep(0.5)

    def supplier_maintenance_edit_supplier_name(self,name):
        old_name = self.supplier_maintenance_get_first_supplier_name()
        self.supplier_maintenance_click_edit_button()
        self.supplier_maintenance_input_supplier_name(name)
        self.supplier_maintenance_click_save_button()
        return old_name



    # 点击删除按钮
    def supplier_maintenance_click_delete_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_delete_button_loc)
        self.random_sleep(0.5)

    # 点击确认删除按钮
    def supplier_maintenance_click_confirm_delete_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_delete_confirm_button_loc)
        self.random_sleep(0.5)

    # 点击取消删除按钮
    def supplier_maintenance_click_cancel_delete_button(self):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_delete_cancel_button_loc)
        self.random_sleep(0.5)

    # 输入供应商名称
    def supplier_maintenance_input_supplier_name(self, supplier_name):
        self.send_keys_by_clear_and_typing(SupplierMaintenanceLocator.supplier_maintenance_supplier_name_input_loc, supplier_name)
        self.random_sleep(0.5)

    # 选择供应商类型
    def supplier_maintenance_select_supplier_type(self, supplier_type):
        self.click_element(SupplierMaintenanceLocator.supplier_maintenance_supplier_type_select_loc)
        self.random_sleep(0.5)
        try:
            self.click_element(('xpath', f'//*[@title="{supplier_type}" and contains(@class,"ant-select-item ant-select-item-option")]'))
            self.click_element(SupplierMaintenanceLocator.supplier_maintenance_title_loc)
        except Exception as e:
            self.move_to_element(SupplierMaintenanceLocator.supplier_maintenance_supplier_type_select_loc)
            self.scroll_element_by_pixel(SupplierMaintenanceLocator.supplier_maintenance_supplier_type_select_loc,
                                         'down', 100)
            # 确保XPath字符串正确闭合
            self.click_element(('xpath',f'//*[@title="{supplier_type}" and contains(@class,"ant-select-item ant-select-item-option")]'))
            self.click_element(SupplierMaintenanceLocator.supplier_maintenance_title_loc)
            logger.warring(f'{supplier_type}供应商类型没找见，尝试使用滚动条解决')


    # 获取已输入的供应商名称 第一个供应商
    def supplier_maintenance_get_first_supplier_name(self):
        time.sleep(1)
        return self.text(SupplierMaintenanceLocator.supplier_maintenance_first_supplier_name_loc)

    # 获取已输入的供应商类型
    def supplier_maintenance_get_first_supplier_type(self):
        return self.text(SupplierMaintenanceLocator.supplier_maintenance_first_supplier_type_loc)

    # 新增供应商必填项效验
    def supplier_maintenance_add_supplier_required_item_validation(self):
        self.switch_to_supplier_maintenance()
        self.supplier_maintenance_click_add_button()
        self.supplier_maintenance_click_save_button()
    # 获取供应商名称是必填项 供应商名称 是必填的!!
    def supplier_maintenance_get_supplier_name_required_text(self):
        return self.text(SupplierMaintenanceLocator.supplier_maintenance_get_supplier_name_required_loc)
    # 获取供应商类型是必填项  供货范围 是必填的!!
    def supplier_maintenance_get_supplier_type_required_text(self):
        return self.text(SupplierMaintenanceLocator.supplier_maintenance_get_supplier_type_required_loc)

    # 正常新增供应商
    def test_electronic_archives_12_4(self,supplier_name,supplier_type):
        self.switch_to_supplier_maintenance()
        self.supplier_maintenance_click_add_button()
        self.supplier_maintenance_input_supplier_name(supplier_name)
        self.supplier_maintenance_select_supplier_type(supplier_type)
        self.supplier_maintenance_click_save_button()
    # 新增一条临时数据，用于后续删除操作，并返回新增的供应商名称
    def temp_supplier_maintenance(self):
        self.switch_to_supplier_maintenance()
        self.supplier_maintenance_click_add_button()
        name = "UI测试临时供应商名称"
        self.supplier_maintenance_input_supplier_name(name)
        self.supplier_maintenance_select_supplier_type("BMS")
        self.supplier_maintenance_click_save_button()
        self.supplier_maintenance_click_confirm_button()
        return name

    # 删除临时增加的供应商数据
    def delete_temp_supplier_maintenance(self):
        self.switch_to_supplier_maintenance()
        self.supplier_maintenance_click_delete_button()
        self.supplier_maintenance_click_confirm_delete_button()
        self.supplier_maintenance_click_confirm_button()

    # 添加重复供应商名称
    def test_electronic_archives_12_5(self,supplier_name,supplier_type):
        self.switch_to_supplier_maintenance()
        name = self.supplier_maintenance_get_first_supplier_name()
        self.supplier_maintenance_click_add_button()
        self.supplier_maintenance_input_supplier_name(name)
        self.supplier_maintenance_select_supplier_type(supplier_type)
        self.supplier_maintenance_click_save_button()

    # 删除操作
    def delete_supplier_maintenance(self):
        time.sleep(0.5)
        self.switch_to_supplier_maintenance()
        time.sleep(0.5)
        self.supplier_maintenance_click_delete_button()










