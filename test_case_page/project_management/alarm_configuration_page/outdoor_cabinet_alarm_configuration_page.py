# 户外柜告警配置界面
import allure
from selenium.webdriver.common.by import By

from common.base_method import BasePage
from test_case_locator.project_management.alarm_configuration_locator.outdoor_cabinet_alarm_configuration_locator import \
    OutdoorCabinetAlarmConfigurationLocator


class OutdoorCabinetAlarmConfigurationPage(BasePage):
    # 获取项目管理模块是否展开 如果展开则返回False
    def _get_project_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            OutdoorCabinetAlarmConfigurationLocator.project_management_is_expand_loc, "class")

    # 判断是否在户外柜告警配置界面
    # class ="ant-tabs-tab ant-tabs-tab-active"
    def is_outdoor_cabinet_alarm_configuration_page(self):
        return self.get_attribute(OutdoorCabinetAlarmConfigurationLocator.outdoor_cabinet_alarm_configuration_loc, "class") == "ant-tabs-tab ant-tabs-tab-active"

    # 切换至户外柜告警配置界面
    def switch_to_outdoor_cabinet_alarm_configuration_page(self):
        if self._get_project_management_is_expand():
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.project_management_loc)
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.project_alarm_configuration_loc)
        if self.is_outdoor_cabinet_alarm_configuration_page() == False:
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.outdoor_cabinet_alarm_configuration_loc)
            self.random_sleep(0.5)

    # 点击户外柜告警配置界面批量导出按钮
    def click_outdoor_cabinet_alarm_configuration_batch_export_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.batch_export_button_loc)

    # 点击批量更新按钮
    def click_batch_update_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.batch_update_button_loc)

    # 点击批量更新取消按钮
    def click_batch_update_cancel_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.batch_update_cancel_button_loc)

    # 点击批量更新关闭按钮
    def click_batch_update_close_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.batch_update_close_button_loc)
    # 点击批量更新确定按钮
    def click_batch_update_confirm_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.batch_update_confirm_button_loc)

    # 翻页功能
    def test_page_turning(self):
        if self.visibility_of_element_located(OutdoorCabinetAlarmConfigurationLocator.second_page_loc):
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.next_page_loc)
            self.random_sleep(0.5)
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.first_page_loc)
            self.random_sleep(0.5)
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.second_page_loc)
            self.random_sleep(0.5)
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.previous_page_loc)
            a = self.get_attribute(OutdoorCabinetAlarmConfigurationLocator.first_page_loc, "class")
            return "ant-pagination-item-active" in a
        else:
            return True

    # 编辑功能
    # 点击第一个告警的 编辑按钮
    @allure.step("点击第一个告警的 编辑按钮")
    def click_first_alarm_edit_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.first_alarm_edit_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击编辑界面确认按钮")
    def click_edit_confirm_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.edit_confirm_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击编辑界面取消按钮")
    def click_edit_cancel_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.edit_cancel_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击编辑界面关闭按钮")
    def click_edit_close_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.edit_close_button_loc)
        self.random_sleep(0.5)

    # 查看告警类型是否有值
    def check_alarm_type_value(self):
        return self.text(OutdoorCabinetAlarmConfigurationLocator.edit_operation_alarm_type_content_loc)

    @allure.step("判断下一页是否可以被点击")
    # class="ant-pagination-next ant-pagination-disabled"
    def check_next_page_clickable(self):
        return self.get_attribute(OutdoorCabinetAlarmConfigurationLocator.next_page_loc, "class") == "ant-pagination-next ant-pagination-disabled"

    @allure.step("找到第一个没有运维告警类的高级")
    def find_first_no_alarm_type_advanced(self):
        while True:  # 开始一个无限循环
            found_empty_cell = False  # 标记是否找到空单元格
            for i in range(2, 12):  # 遍历从2到11的整数
                # 获取当前行第6列单元格的文本内容
                cell_text = self.text((By.XPATH, f'//*[@class="ant-table-tbody"]/tr[{i}]/td[6]'))

                if cell_text == "":  # 如果单元格文本为空字符串
                    return i - 1  # 返回当前行索引减一的值，并结束函数执行
                else:
                    found_empty_cell = True  # 找到非空单元格，更新标记

            if not found_empty_cell:  # 如果for循环结束且没有找到空单元格
                if self.check_next_page_clickable():  # 检查是否存在下一页可以点击
                    self.click_element(OutdoorCabinetAlarmConfigurationLocator.next_page_loc)  # 点击下一页按钮
                else:
                    break  # 如果没有下一页可点击，退出循环
            self.random_sleep(0.5)  # 随机等待一段时间

    @allure.step("点击没有运维告警类的编辑按钮")
    def click_no_alarm_type_edit_button(self): #//*[text()="编辑"]/..
        row_index = self.find_first_no_alarm_type_advanced()
        self.click_element((By.XPATH, f'(//*[text()="编辑"]/..)[{row_index}]'))
        self.random_sleep(0.5)

    @allure.step("获取运维告警类型必填提示信息")
    def get_operation_alarm_type_required_message(self):
        return self.text(OutdoorCabinetAlarmConfigurationLocator.edit_operation_alarm_type_required_message_loc)








