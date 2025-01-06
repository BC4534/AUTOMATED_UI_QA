import time

from selenium.webdriver.common.by import By

from common.base_method import BasePage
from test_case_locator.project_management.checkitem_configuration_locator.checkitem_configuration_locator import \
    CheckitemConfigurationLocator


class CheckItemConfigurationPage(BasePage):

    # 获取项目管理模块是否展开
    def get_project_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            CheckitemConfigurationLocator.project_management_is_expand_loc, "class")

    # 切换至人力资源复盘界面
    def switch_to_resources_inventory_page(self):
        if self.get_project_management_is_expand():
            self.click_element(CheckitemConfigurationLocator.project_management_loc)
        self.click_element(CheckitemConfigurationLocator.checkitem_configuration_loc)
        time.sleep(0.5)

    # 获取巡检项配置界面 巡检项名称查询输入框前面的 巡检项名称文本
    def get_checkitem_name_input_tip_text(self):
        return self.text(CheckitemConfigurationLocator.checkitem_name_input_tip_loc)


    # 点击新增按钮
    def click_add_checkitem_button(self):
        self.click_element(CheckitemConfigurationLocator.add_checkitem_button_loc)
        self.random_sleep(0.5)

    # 点击批量删除按钮
    def click_delete_checkitem_button(self):
        self.click_element(CheckitemConfigurationLocator.delete_checkitem_button_loc)
        time.sleep(1)

    # 点击确认删除
    def click_delete_checkitem_confirm_button(self):
        self.click_element(CheckitemConfigurationLocator.delete_checkitem_button_confirm_loc)
        time.sleep(1)
    # 点击取消删除
    def click_delete_checkitem_cancel_button(self):
        self.click_element(CheckitemConfigurationLocator.delete_checkitem_button_cancel_loc)
        time.sleep(1)

    # 点击第一条巡检项的编辑按钮
    def click_first_checkitem_edit_button(self):
        self.click_element(CheckitemConfigurationLocator.first_checkitem_edit_button_loc)
        time.sleep(0.5)

    # 获取编辑巡检项的标题文本
    def get_edit_checkitem_title_text(self):
        return self.text(CheckitemConfigurationLocator.edit_checkitem_title_loc)


    # 点击新增巡检项的确定按钮
    def click_add_checkitem_confirm_button(self):
        self.click_element(CheckitemConfigurationLocator.add_checkitem_button_confirm_loc)
        time.sleep(0.5)

    # 点击新增巡检项的取消按钮
    def click_add_checkitem_cancel_button(self):
        self.click_element(CheckitemConfigurationLocator.add_checkitem_button_cancel_loc)
        time.sleep(0.5)

    # 点击新增巡检项的关闭按钮
    def click_add_checkitem_close_button(self):
        self.click_element(CheckitemConfigurationLocator.add_checkitem_button_close_loc)


    # 获取信息巡检项 名称必填项提示文本
    def get_add_checkitem_name_required_text(self):
        return self.text(CheckitemConfigurationLocator.add_checkitem_name_required_loc)

    # 获取信息巡检项 类型必填项提示文本
    def get_add_checkitem_type_required_text(self):
        return self.text(CheckitemConfigurationLocator.add_checkitem_type_required_loc)

    # 获取信息巡检项 内容必填项提示文本
    def get_add_checkitem_content_required_text(self):
        return self.text(CheckitemConfigurationLocator.add_checkitem_content_required_loc)

    # 获取信息巡检项 拍照是否必填项提示文本
    def get_add_checkitem_photo_required_text(self):
        return self.text(CheckitemConfigurationLocator.add_checkitem_photo_required_loc)

    # 获取信息巡检项 备注是否必填项提示文本
    def get_add_checkitem_remark_required_text(self):
        return self.text(CheckitemConfigurationLocator.add_checkitem_remark_required_loc)

    # 新增巡检项
    def add_checkitem(self, checkitem_name, checkitem_type, checkitem_content, checkitem_photo, checkitem_remark):
        self.send_keys_by_clear_and_typing(CheckitemConfigurationLocator.add_checkitem_name_input_loc, checkitem_name)
        self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_loc)
        self.random_sleep(0.5)
        if checkitem_type == "空调系统":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_air_loc)
        elif checkitem_type == "电池室或电池仓":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_battery_loc)
        elif checkitem_type == "储能电池及电池管理系统（BMS）":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_bms_loc)
        elif checkitem_type == "EMS系统":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_ems_loc)
        elif checkitem_type == "消防系统":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_fire_loc)
        elif checkitem_type == "汇流柜":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_hui_loc)
        elif checkitem_type == "液冷系统":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_liquid_loc)
        elif checkitem_type == "储能变流器（PCS）":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_pcs_loc)
        else:
            self.logger.error("新增巡检项类型输入错误,默认选择bms")
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_bms_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(CheckitemConfigurationLocator.add_checkitem_content_input_loc,
                                           checkitem_content)
        self.random_sleep(0.5)
        if checkitem_photo == "是":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_photo_yes_loc)
        elif checkitem_photo == "否":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_photo_no_loc)
        else:
            self.logger.error("新增巡检项拍照是否输入错误,默认选择否")
            self.click_element(CheckitemConfigurationLocator.add_checkitem_photo_no_loc)
        self.random_sleep(0.5)
        if checkitem_remark == "是":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_remark_yes_loc)
        elif checkitem_remark == "否":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_remark_no_loc)
        else:
            self.logger.error("新增巡检项备注是否输入错误,默认选择否")
            self.click_element(CheckitemConfigurationLocator.add_checkitem_remark_no_loc)
        self.random_sleep(0.5)

    # 编辑巡检项
    def edit_checkitem(self, checkitem_name="", checkitem_type="", checkitem_content="", checkitem_photo="", checkitem_remark=""):
        if checkitem_name != "":
            self.send_keys_by_clear_and_typing(CheckitemConfigurationLocator.add_checkitem_name_input_loc,
                                               checkitem_name)
        if checkitem_type != "":
            self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_loc)
            self.random_sleep(0.5)
            if checkitem_type == "空调系统":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_air_loc)
            elif checkitem_type == "电池室或电池仓":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_battery_loc)
            elif checkitem_type == "储能电池及电池管理系统（BMS）":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_bms_loc)
            elif checkitem_type == "EMS系统":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_ems_loc)
            elif checkitem_type == "消防系统":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_fire_loc)
            elif checkitem_type == "汇流柜":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_hui_loc)
            elif checkitem_type == "液冷系统":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_liquid_loc)
            elif checkitem_type == "储能变流器（PCS）":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_pcs_loc)
            else:
                self.logger.error("新增巡检项类型输入错误,默认选择bms")
                self.click_element(CheckitemConfigurationLocator.add_checkitem_type_select_option_bms_loc)
            self.random_sleep(0.5)
        if checkitem_content != "":
            self.send_keys_by_clear_and_typing(CheckitemConfigurationLocator.add_checkitem_content_input_loc,
                                               checkitem_content)

            self.random_sleep(0.5)
        if checkitem_photo != "":
            if checkitem_photo == "是":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_photo_yes_loc)
            elif checkitem_photo == "否":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_photo_no_loc)
            else:
                self.logger.error("新增巡检项拍照是否输入错误,默认选择否")
                self.click_element(CheckitemConfigurationLocator.add_checkitem_photo_no_loc)
            self.random_sleep(0.5)
        if checkitem_remark != "":
            if checkitem_remark == "是":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_remark_yes_loc)
            elif checkitem_remark == "否":
                self.click_element(CheckitemConfigurationLocator.add_checkitem_remark_no_loc)
            else:
                self.logger.error("新增巡检项备注是否输入错误,默认选择否")
                self.click_element(CheckitemConfigurationLocator.add_checkitem_remark_no_loc)
            self.random_sleep(0.5)

    # 获取最后一个巡检项名称
    def get_last_checkitem_name(self):
        while True:
            if self.is_next_page_enable() == "false":
                self.click_element(CheckitemConfigurationLocator.next_page_loc)
            else:
                break
        time.sleep(1)
        return self.text(CheckitemConfigurationLocator.current_page_last_checkitem_name_loc)

    # 获取第一个巡检项名称
    def get_first_checkitem_name(self):
        time.sleep(1)
        return self.text(CheckitemConfigurationLocator.current_page_first_checkitem_name_loc)

    # 获取第二个巡检项名称
    def get_second_checkitem_name(self):
        time.sleep(1)
        return self.text(CheckitemConfigurationLocator.second_checkitem_name_loc)

    # 获取巡检项名称列表
    def get_checkitem_name_list(self):
        checkitem_name_list = []
        while True:
            for i in range(2, 12):
                try:
                    checkitem_name_list.append(self.text((By.XPATH, f'//*[@class="ant-table-tbody"]/tr[{i}]/td[2]/div')))
                except Exception as e:
                    # self.logger.error(f'//*[@class="ant-table-tbody"]/tr[{i}]/td[2]/div，时定位不到元素，没有数据了')
                    break

            if self.is_next_page_enable() == "false":
                self.click_element(CheckitemConfigurationLocator.next_page_loc)
            else:
                break

        return checkitem_name_list

    # 勾选符合条件的巡检项复现框
    def check_checkitem_by_name(self, checkitem_name):
        while True:
            for i in range(2, 12):
                try:
                    if self.text((By.XPATH, f'//*[@class="ant-table-tbody"]/tr[{i}]/td[2]/div')) == checkitem_name:
                        self.click_element((By.XPATH,f'//*[@class="ant-table-tbody"]/tr[{i}]/td//span'))
                except:
                    break
            if self.is_next_page_enable() == "false":
                self.click_element(CheckitemConfigurationLocator.next_page_loc)
            else:
                break


    # 点击最后一页的复选框
    def click_last_checkitem_checkbox(self):
        while True:
            if self.is_next_page_enable() == "false":
                self.click_element(CheckitemConfigurationLocator.next_page_loc)
            else:
                break
        self.click_element(CheckitemConfigurationLocator.last_checkitem_checkbox_loc)
        time.sleep(0.5)

    # 判断下一页是否可以点击
    def is_next_page_enable(self):
        return self.get_attribute(CheckitemConfigurationLocator.next_page_loc, "aria-disabled")

    # 获取页面提示文本信息
    def get_page_tip_text(self):
        return self.text(CheckitemConfigurationLocator.page_tip_loc)

    # 巡检项名称查询
    def search_checkitem_by_name(self, checkitem_name):
        self.send_keys_by_clear_and_typing(CheckitemConfigurationLocator.checkitem_name_input_loc, checkitem_name)
        time.sleep(1)

    # 点击查询按钮
    def click_search_button(self):
        self.click_element(CheckitemConfigurationLocator.checkitem_search_button_loc)

    # 点击重置按钮
    def click_reset_button(self):
        self.click_element(CheckitemConfigurationLocator.checkitem_reset_button_loc)


