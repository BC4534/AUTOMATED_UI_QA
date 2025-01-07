# 户外柜告警配置界面
import allure
from selenium.webdriver.common.by import By

from common.base_method import BasePage
from test_case_locator.project_management.alarm_configuration_locator.outdoor_cabinet_alarm_configuration_locator import \
    OutdoorCabinetAlarmConfigurationLocator
from test_case_object.work_order_management.work_order_list.test_work_order_list_09 import logger


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
        return (By.XPATH, f'(//*[text()="编辑"]/..)[{row_index}]')

    @allure.step("获取运维告警类型必填提示信息")
    def get_operation_alarm_type_required_message(self):
        return self.text(OutdoorCabinetAlarmConfigurationLocator.edit_operation_alarm_type_required_message_loc)

    @allure.step("编辑操作流程")
    def edit_operation_alarm(self, alarm_type="", alarm_level="", description=""):
        if alarm_type != "":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.edit_operation_alarm_type_select_loc)
            self.random_sleep(0.5)
            self.click_element((By.XPATH, f'//*[@title="{alarm_type}"]'))
            self.random_sleep(0.5)
        if alarm_level != "":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.edit_operation_alarm_level_select_loc)
            self.random_sleep(0.5)
            self.click_element((By.XPATH, f'//*[@title="{alarm_level}"]'))
            self.random_sleep(0.5)
        if description != "":
            self.send_keys_by_clear_and_typing(OutdoorCabinetAlarmConfigurationLocator.edit_operation_alarm_description_input_loc, description)
            self.random_sleep(0.5)


    @allure.step("获取户外柜告警编辑界面的运维告警描述内容")
    def get_edit_operation_alarm_description_content(self):
        return self.get_attribute(OutdoorCabinetAlarmConfigurationLocator.edit_operation_alarm_description_input_loc,"value")

    # 查询相关
    @allure.step("点击搜索按钮")
    def click_search_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击重置按钮")
    def click_reset_button(self):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.reset_button_loc)
        self.random_sleep(0.5)

    @allure.step("获取第二个设备名称")
    def get_second_device_name(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.second_alarm_device_name_loc)
        except:
            return 1

    @allure.step("获取第一个设备名称")
    def get_first_device_name(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_device_name_loc)
        except:
            return 1

    @allure.step("输入设备名称查询条件")
    def input_device_name_search_condition(self, device_name):
        self.send_keys_by_clear_and_typing(OutdoorCabinetAlarmConfigurationLocator.search_device_name_input_loc, device_name)
        self.random_sleep(0.5)

    @allure.step("获取第一个户外柜规格")
    def get_first_outdoor_cabinet_specification(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_outdoor_cabinet_specification_loc)
        except:
            return 1

    @allure.step("户外柜规格查询")
    def outdoor_cabinet_specification_search(self, outdoor_cabinet_specification):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_outdoor_cabinet_specification_select_loc)
        self.random_sleep(0.5)
        if outdoor_cabinet_specification == "215户外柜国标1.0":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_outdoor_cabinet_specification_215_1_loc)
        elif outdoor_cabinet_specification == "215户外柜国标2.0":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_outdoor_cabinet_specification_215_2_loc)
        elif outdoor_cabinet_specification == "232户外柜":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_outdoor_cabinet_specification_232_loc)
        elif outdoor_cabinet_specification == "372户外柜":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_outdoor_cabinet_specification_372_loc)
        else:
            logger.info(" outdoor_cabinet_specification 参数错误")

    @allure.step("获取第一个告警名称")
    def get_first_alarm_name(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_alarm_name_loc)
        except:
            return 1
    @allure.step("获取第二个告警名称")
    def get_second_alarm_name(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.second_alarm_alarm_name_loc)
        except:
            return 1

    @allure.step("输入告警名称查询条件")
    def input_alarm_name_search_condition(self, alarm_name):
        self.send_keys_by_clear_and_typing(OutdoorCabinetAlarmConfigurationLocator.search_alarm_name_input_loc, alarm_name)
        self.random_sleep(0.5)


    @allure.step("获取第一个告警描述")
    def get_first_alarm_description(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_alarm_description_loc)
        except:
            return 1
    @allure.step("获取第二个告警描述")
    def get_second_alarm_description(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.second_alarm_alarm_description_loc)
        except:
            return 1
    @allure.step("输入告警描述查询条件")
    def input_alarm_description_search_condition(self, alarm_description):
        self.send_keys_by_clear_and_typing(OutdoorCabinetAlarmConfigurationLocator.search_alarm_description_input_loc, alarm_description)
        self.random_sleep(0.5)


    @allure.step("获取第一个告警类型")
    def get_first_alarm_type(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_alarm_type_loc)
        except:
            return 1
    @allure.step("获取第二个告警类型")
    def get_second_alarm_type(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.second_alarm_alarm_type_loc)
        except:
            return 1
    @allure.step("输入告警类型查询条件")
    def input_alarm_type_search_condition(self, alarm_type):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_type_select_loc)
        self.random_sleep(0.5)
        if alarm_type == "EMS":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_type_ems_loc)
        elif alarm_type == "PCS":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_type_pcs_loc)
        elif alarm_type == "BMS":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_type_bms_loc)
        elif alarm_type == "液冷系统":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_type_liquid_cooling_system_loc)
        elif alarm_type == "消防系统":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_type_fire_system_loc)
        elif alarm_type == "集装箱类":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_type_container_loc)
        else:
            logger.info(" alarm_type 参数错误")

    @allure.step("获取第一个告警等级")
    def get_first_alarm_level(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_alarm_level_loc)
        except:
            return 1
    @allure.step("输入告警等级查询条件")
    def input_alarm_level_search_condition(self, alarm_level):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_level_select_loc)
        self.random_sleep(0.5)
        if alarm_level == "一级":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_level_first_loc)
        elif alarm_level == "二级":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_level_second_loc)
        elif alarm_level == "三级":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_level_third_loc)
        elif alarm_level == "四级":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_alarm_level_fourth_loc)
        else:
            logger.info(" alarm_level 参数错误")

    @allure.step("获取第一个是否告警")
    def get_first_alarm_is_alarm(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_is_alarm_loc)
        except:
            return 1

    @allure.step("输入是否告警查询条件")
    def input_alarm_is_alarm_search_condition(self, alarm_is_alarm):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_is_alarm_select_loc)
        self.random_sleep(0.5)
        if alarm_is_alarm == "是":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_is_alarm_yes_loc)
        elif alarm_is_alarm == "否":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_is_alarm_no_loc)
        else:
            logger.info(" alarm_is_alarm 参数错误")

    @allure.step("获取第一个是否自动生成工单")
    def get_first_alarm_is_auto_create_work_order(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_is_auto_create_work_order_loc)
        except:
            return 1
    @allure.step("输入是否自动生成工单查询条件")
    def input_alarm_is_auto_create_work_order_search_condition(self, alarm_is_auto_create_work_order):
        self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_is_auto_create_work_order_select_loc)
        self.random_sleep(0.5)
        if alarm_is_auto_create_work_order == "是":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_is_auto_create_work_order_yes_loc)
        elif alarm_is_auto_create_work_order == "否":
            self.click_element(OutdoorCabinetAlarmConfigurationLocator.search_is_auto_create_work_order_no_loc)
        else:
            logger.info(" alarm_is_auto_create_work_order 参数错误")

    @allure.step("获取第一个最后修改人")
    def get_first_alarm_last_modifier(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.first_alarm_last_modifier_loc)
        except:
            return 1
    @allure.step("获取第二个最后修改人")
    def get_second_alarm_last_modifier(self):
        try:
            return self.text(OutdoorCabinetAlarmConfigurationLocator.second_alarm_last_modifier_loc)
        except:
            return 1
    @allure.step("输入最后修改人查询条件")
    def input_alarm_last_modifier_search_condition(self, alarm_last_modifier):
        self.send_keys_by_clear_and_typing(OutdoorCabinetAlarmConfigurationLocator.search_last_modifier_input_loc, alarm_last_modifier)
        self.random_sleep(0.5)

        








