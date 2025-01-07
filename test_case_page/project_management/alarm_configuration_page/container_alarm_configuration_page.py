# 大储告警配置页面
import time

from common.base_method import BasePage
from test_case_locator.project_management.alarm_configuration_locator.container_alarm_configuration_locator import \
    ContainerAlarmConfigurationLocator


class ContainerAlarmConfigurationPage(BasePage):
    # 获取项目管理模块是否展开 如果展开则返回False
    def _get_project_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            ContainerAlarmConfigurationLocator.project_management_is_expand_loc, "class")

    # 判断是否在大储告警配置界面
    # class ="ant-tabs-tab ant-tabs-tab-active"
    def is_container_alarm_configuration_page(self):
        return self.get_attribute(ContainerAlarmConfigurationLocator.container_alarm_configuration_loc, "class") == "ant-tabs-tab ant-tabs-tab-active"

    # 切换至大储告警配置界面
    def switch_to_container_alarm_configuration_page(self):
        if self._get_project_management_is_expand():
            self.click_element(ContainerAlarmConfigurationLocator.project_management_loc)
        self.click_element(ContainerAlarmConfigurationLocator.project_alarm_configuration_loc)
        if self.is_container_alarm_configuration_page() == False:
            self.click_element(ContainerAlarmConfigurationLocator.container_alarm_configuration_loc)


