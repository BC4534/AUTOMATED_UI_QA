import allure
from selenium.webdriver.common.by import By

from common.base_method import BasePage
from test_case_locator.maintenance_tools.project_operation_overview_locator import ProjectOperationOverviewLocator


class ProjectOperationOverviewPage(BasePage):


    # 判断运维工具模块是否展开
    def __get_maintenance_tools_is_expand(self):
        return "ant-menu-submenu-open" in self.get_attribute(
            ProjectOperationOverviewLocator.maintenance_tools_page_expand_loc, "class"
        )
    # 判断是否在项目运行总览界面
    def _get_project_operation_overview_is_current_page(self):
        return self.get_attribute(ProjectOperationOverviewLocator.project_operation_overview_loc, "aria-selected")

    @allure.step("切换至项目运行报告界面")
    def __switch_to_project_running_report_page(self) :
        if self.__get_maintenance_tools_is_expand() is False:
            self.click_element(ProjectOperationOverviewLocator.maintenance_tools_module_loc)
        self.click_element(ProjectOperationOverviewLocator.project_operation_report_loc)
        self.random_sleep(0.5)

    @allure.step("切换至项目运行总览界面")
    def switch_to_project_operation_overview_page(self) :
        self.__switch_to_project_running_report_page()
        if self._get_project_operation_overview_is_current_page() == "false":
            self.click_element(ProjectOperationOverviewLocator.project_operation_overview_loc)
        self.random_sleep(0.5)

    @allure.step("点击导出查询数据")
    def click_export_query_data(self) :
        self.click_element(ProjectOperationOverviewLocator.export_query_data_button_loc)
        self.random_sleep(0.5)

    @allure.step("获取第一个项目名称")
    def get_first_project_name(self):
        return self.text(ProjectOperationOverviewLocator.first_data_project_name_loc)

    @allure.step("获取第一个站点名称")
    def get_first_station_name(self):
        return self.text(ProjectOperationOverviewLocator.first_data_station_name_loc)

    @allure.step("获取第二个项目名称")
    def get_second_project_name(self):
        return self.text(ProjectOperationOverviewLocator.second_data_project_name_loc)

    @allure.step("获取第二个站点名称")
    def get_second_station_name(self):
        return self.text(ProjectOperationOverviewLocator.second_data_station_name_loc)

    @allure.step("项目名称 输入")
    def input_project_name(self, project_name):
        self.click_element(ProjectOperationOverviewLocator.project_name_input_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(ProjectOperationOverviewLocator.project_name_input_loc, project_name)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[contains(@title,"{project_name}")]'))
        self.random_sleep(0.5)

    @allure.step("输入电站名称查询条件")
    def input_station_name(self, station_name):
        self.click_element(ProjectOperationOverviewLocator.station_name_input_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(ProjectOperationOverviewLocator.station_name_input_loc, station_name)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[contains(@title,"{station_name}")]'))
        self.random_sleep(0.5)

