import allure
from selenium.webdriver.common.by import By

from common.base_method import BasePage
from test_case_locator.maintenance_tools.project_operation_report_locator import ProjectOperationReportLocator


class ProjectOperationReportPage(BasePage):


    # 判断运维工具模块是否展开
    def __get_maintenance_tools_is_expand(self):
        return "ant-menu-submenu-open" in self.get_attribute(
            ProjectOperationReportLocator.maintenance_tools_page_expand_loc, "class"
        )
    # 判断是否在项目运行日报tab页
    def _get_project_operation_report_is_active(self):
        return  self.get_attribute(
            ProjectOperationReportLocator.project_operation_report_daily_tab_loc, "aria-selected"
        )

    @allure.step("切换至项目运行报告界面")
    def __switch_to_project_running_report_page(self) :
        if self.__get_maintenance_tools_is_expand() is False:
            self.click_element(ProjectOperationReportLocator.maintenance_tools_module_loc)
        self.click_element(ProjectOperationReportLocator.project_operation_report_loc)
        self.random_sleep(0.5)

    @allure.step("切换至项目运行日报界面")
    def switch_to_project_operation_report_daily_tab(self) :
        self.__switch_to_project_running_report_page()
        if self._get_project_operation_report_is_active() == "false":
            self.click_element(ProjectOperationReportLocator.project_operation_report_daily_tab_loc)
        self.random_sleep(0.5)

    @allure.step("点击导出查询数据按钮")
    def click_export_query_data_button(self) :
        self.click_element(ProjectOperationReportLocator.export_query_data_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击批量导出云平台巡检数据按钮")
    def click_batch_export_cloud_platform_inspection_data_button(self) :
        self.click_element(ProjectOperationReportLocator.batch_export_cloud_platform_inspection_data_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击第一个导出云平台巡检记录按钮")
    def click_export_cloud_platform_inspection_data_button(self) :
        self.click_element(ProjectOperationReportLocator.export_cloud_platform_inspection_record_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击巡检记录界面关闭按钮")
    def click_inspection_record_close_button(self) :
        self.click_element(ProjectOperationReportLocator.inspection_record_close_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击巡检记录第一个导出按钮")
    def click_inspection_record_export_button(self) :
        self.click_element(ProjectOperationReportLocator.inspection_record_export_button_loc)
        self.random_sleep(0.5)
    @allure.step("点击巡检记录导出全部文件按钮")
    def click_inspection_record_export_all_file_button(self) :
        self.click_element(ProjectOperationReportLocator.inspection_record_export_all_file_button_loc)
        self.random_sleep(0.5)

    @allure.step("判断弹窗界面是否还在")
    def _get_content_page(self) :
        try:
            self.visibility_of_element_located(ProjectOperationReportLocator.content_page_loc)
            return True
        except:
            return False

    @allure.step("点击第一个导出当日充放原数据按钮")
    def click_export_daily_charge_and_discharge_data_button(self) :
        self.click_element(ProjectOperationReportLocator.export_daily_charge_and_discharge_original_data_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击全选复选框")
    def click_select_all_checkbox(self) :
        self.click_element(ProjectOperationReportLocator.select_all_checkbox_loc)
        self.random_sleep(0.5)
    @allure.step("获取第一个项目名称")
    def get_first_project_name(self) :
        return self.text(ProjectOperationReportLocator.first_data_project_name_loc)

    @allure.step("获取第一个站点名称")
    def get_first_station_name(self) :
        return self.text(ProjectOperationReportLocator.first_data_station_name_loc)
    @allure.step("获取第一个检查时间")
    def get_first_check_time(self) :
        return self.text(ProjectOperationReportLocator.first_data_check_time_loc)

    @allure.step("获取第二个项目名称")
    def get_second_project_name(self) :
        try:
            return self.text(ProjectOperationReportLocator.second_data_project_name_loc)
        except:
            return 1
    @allure.step("获取第二个站点名称")
    def get_second_station_name(self) :
        return self.text(ProjectOperationReportLocator.second_data_station_name_loc)
    @allure.step("获取第二个检查时间")
    def get_second_check_time(self) :
        return self.text(ProjectOperationReportLocator.second_data_check_time_loc)
    @allure.step("获取第一个下载任务名称")
    def get_first_download_task_name(self) :
        return self.text(ProjectOperationReportLocator.download_task_list_button_first_task_name_loc)
    @allure.step("获取第一个下载任务状态")
    def get_first_download_task_status(self) :
        try:
            return self.text(ProjectOperationReportLocator.download_task_list_button_first_task_status_loc)
        except:
            return 1
    @allure.step("获取第一个下载任务创建时间")
    def get_first_download_task_create_time(self) :
        return self.text(ProjectOperationReportLocator.download_task_list_button_first_task_create_time_loc)
    @allure.step("获取第二个下载任务名称")
    def get_second_download_task_name(self) :
        try:
            return self.text(ProjectOperationReportLocator.download_task_list_button_second_task_name_loc)
        except:
            return 1
    @allure.step("获取第二个下载任务状态")
    def get_second_download_task_status(self) :
        try:
            return self.text(ProjectOperationReportLocator.download_task_list_button_second_task_status_loc)
        except:
            return 1
    @allure.step("获取第二个下载任务创建时间")
    def get_second_download_task_create_time(self) :
        try:
            return self.text(ProjectOperationReportLocator.download_task_list_button_second_task_create_time_loc)
        except:
            return 1
    @allure.step("点击任务列表按钮")
    def click_download_task_list_button(self) :
        self.click_element(ProjectOperationReportLocator.download_task_list_button_loc)
        self.random_sleep(0.5)

    @allure.step("项目名称 输入")
    def input_project_name(self, project_name) :
        self.click_element(ProjectOperationReportLocator.project_name_input_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(ProjectOperationReportLocator.project_name_input_loc, project_name)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[contains(@title,"{project_name}")]'))
        self.random_sleep(0.5)
    @allure.step("输入电站名称查询条件")
    def input_station_name(self, station_name) :
        self.click_element(ProjectOperationReportLocator.station_name_input_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(ProjectOperationReportLocator.station_name_input_loc, station_name)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[contains(@title,"{station_name}")]'))
        self.random_sleep(0.5)

    @allure.step("输入日报生成时间查询条件")
    def input_daily_report_generation_time(self, start_time, end_time) :
        self.input_time(ProjectOperationReportLocator.daily_report_generation_time_input_loc, start_time, end_time)
        self.random_sleep(0.5)

    @allure.step("输入任务列表的任务名称查询条件")
    def input_download_task_list_task_name(self, task_name) :
        self.click_element(ProjectOperationReportLocator.download_task_list_task_name_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(ProjectOperationReportLocator.download_task_list_task_name_loc, task_name)
        self.random_sleep(0.5)

    @allure.step("输入任务列表的任务状态查询条件")
    def input_download_task_list_task_status(self, task_status) :
        self.click_element(ProjectOperationReportLocator.download_task_list_task_status_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[contains(@title,"{task_status}")]'))

    @allure.step("输入任务列表的任务创建时间查询条件")
    def input_download_task_list_create_time(self, create_time) :
        self.input_time(ProjectOperationReportLocator.download_task_list_create_time_loc, create_time)
        self.random_sleep(0.5)

    @allure.step("获取任务列表第二个创建时间")
    def get_download_task_list_second_create_time(self) :
        try:
            return self.text(ProjectOperationReportLocator.download_task_list_button_second_task_create_time_loc)
        except:
            return 1
    @allure.step("获取任务列表第一个创建时间")
    def get_download_task_list_first_create_time(self) :
        try:
            return self.text(ProjectOperationReportLocator.download_task_list_button_first_task_create_time_loc)
        except:
            return 1

