# 大储告警配置页面
import time

import allure

from common.base_method import BasePage
from test_case_locator.project_management.alarm_configuration_locator.container_alarm_configuration_locator import (
    ContainerAlarmConfigurationLocator,
)


class ContainerAlarmConfigurationPage(BasePage):
    # 获取项目管理模块是否展开 如果展开则返回False
    def _get_project_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            ContainerAlarmConfigurationLocator.project_management_is_expand_loc, "class"
        )

    # 判断是否在大储告警配置界面
    # class ="ant-tabs-tab ant-tabs-tab-active"
    def is_container_alarm_configuration_page(self):
        return (
            self.get_attribute(
                ContainerAlarmConfigurationLocator.container_alarm_configuration_loc,
                "class",
            )
            == "ant-tabs-tab ant-tabs-tab-active"
        )

    # 切换至大储告警配置界面
    def switch_to_container_alarm_configuration_page(self):
        if self._get_project_management_is_expand():
            self.click_element(
                ContainerAlarmConfigurationLocator.project_management_loc
            )
        self.click_element(
            ContainerAlarmConfigurationLocator.project_alarm_configuration_loc
        )
        if self.is_container_alarm_configuration_page() == False:
            self.click_element(
                ContainerAlarmConfigurationLocator.container_alarm_configuration_loc
            )

    # 点击批量更新按钮
    @allure.step("点击批量更新按钮")
    def click_batch_update_button(self):
        self.click_element(ContainerAlarmConfigurationLocator.batch_update_button_loc)
        self.random_sleep(0.5)

    # 点击批量导出按钮
    @allure.step("点击批量导出按钮")
    def click_batch_export_button(self):
        self.click_element(ContainerAlarmConfigurationLocator.batch_export_button_loc)
        self.random_sleep(0.5)

    # 点击批量更新取消按钮
    @allure.step("点击批量更新取消按钮")
    def click_batch_update_cancel_button(self):
        self.click_element(
            ContainerAlarmConfigurationLocator.batch_update_cancel_button_loc
        )
        self.random_sleep(0.5)

    # 点击批量更新关闭按钮
    def click_batch_update_close_button(self):
        self.click_element(
            ContainerAlarmConfigurationLocator.batch_update_close_button_loc
        )
        self.random_sleep(0.5)

    # 点击批量更新确定按钮
    def click_batch_update_confirm_button(self):
        self.click_element(
            ContainerAlarmConfigurationLocator.batch_update_confirm_button_loc
        )
        self.random_sleep(0.5)

    # 翻页功能
    def test_page_turning(self):
        if self.visibility_of_element_located(
            ContainerAlarmConfigurationLocator.second_page_loc
        ):
            self.click_element(ContainerAlarmConfigurationLocator.next_page_loc)
            self.random_sleep(0.5)
            self.click_element(ContainerAlarmConfigurationLocator.first_page_loc)
            self.random_sleep(0.5)
            self.click_element(ContainerAlarmConfigurationLocator.second_page_loc)
            self.random_sleep(0.5)
            self.click_element(ContainerAlarmConfigurationLocator.previous_page_loc)
            a = self.get_attribute(
                ContainerAlarmConfigurationLocator.first_page_loc, "class"
            )
            return "ant-pagination-item-active" in a
        else:
            return True

    @allure.step("判断批量更新弹框页面是否关闭")
    def check_batch_update_close(self):
        try:
            self.visibility_of_element_located(
                ContainerAlarmConfigurationLocator.batch_update_file_format_loc
            )
            return False
        except:
            return True

    @allure.step("获取页面提示信息")
    def get_page_tip_text(self):
        return self.text(ContainerAlarmConfigurationLocator.page_tip_loc)
