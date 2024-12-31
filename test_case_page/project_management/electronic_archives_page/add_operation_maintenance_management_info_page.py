from selenium.webdriver.common.by import By
from common.loggerhandler import logger
from test_case_locator.project_management.electronic_archives_locator.add_project_locator import \
    OperationManagementInfoLocator
from test_case_locator.project_management.electronic_archives_locator.electronic_archives_locator import \
    ElectronicArchivesLocator
from test_case_page.project_management.electronic_archives_page.add_maintain_implement_info_management_page import \
    AddMaintainImplementInfoManagementPage


class AddOperationMaintenanceManagementInfoPage(AddMaintainImplementInfoManagementPage):

    # 切换至运维管理信息界面
    def switch_to_operation_maintenance_management_info_page(self):
        logger.info("切换至运维管理信息界面")
        self.click_element(OperationManagementInfoLocator.operation_management_info_page_loc)
        self.random_sleep(0.5)
        self.switch_to_electronic_archives()

    # 选择运维负责人
    def _select_operation_maintenance_person(self, operation_maintenance_person):
        self.click_element(OperationManagementInfoLocator.operation_responsible_select_loc)
        self.random_sleep(0.5)
        if operation_maintenance_person == "":
            logger.info("未填写运维负责人，选择运维负责人为系统管理员")
            self.click_element(OperationManagementInfoLocator.operation_responsible_system_administrator_loc)
        else:
            try:
                logger.info(f"选择运维负责人为{operation_maintenance_person}")
                self.click_element((By.XPATH,
                                    f'//*[@class="rc-virtual-list-holder-inner"]/div[@title="{operation_maintenance_person}"]'))
            except:
                logger.warning("未找到运维负责人，选择运维负责人为系统管理员")
                self.click_element(OperationManagementInfoLocator.operation_responsible_system_administrator_loc)

    # 获取运维负责人提示文本
    def _get_operation_maintenance_person_tip_text(self):
        logger.info("获取运维负责人提示文本")
        self.click_element(OperationManagementInfoLocator.operation_responsible_tip_loc)
        self.random_sleep(0.5)
        return self.text(OperationManagementInfoLocator.operation_responsible_tip_text_loc)

    # 填写首次巡检时间
    def _fill_first_inspection_time(self, first_inspection_time):
        # 默认填写后三个月的1号
        logger.info(f"填写首次巡检时间为{first_inspection_time}")
        self.click_element(OperationManagementInfoLocator.first_inspection_time_select_loc)
        self.random_sleep(0.5)
        self.click_element(OperationManagementInfoLocator.next_month_button_loc)
        self.random_sleep(0.5)
        self.click_element(OperationManagementInfoLocator.next_month_button_loc)
        self.random_sleep(0.5)
        self.click_element(OperationManagementInfoLocator.first_day_loc)
        self.random_sleep(0.5)
        # if first_inspection_time == "":
        #     logger.info("未填写首次巡检时间，选择今天")
        #     self.click_element(OperationManagementInfoLocator.first_inspection_time_today_loc)
        #
        # else:
        #     logger.info(f"填写首次巡检时间为{first_inspection_time}")
        #     self.click_element(OperationManagementInfoLocator.first_inspection_time_today_loc)
        #     self.random_sleep(0.5)

    # 选择巡检周期
    def _select_inspection_cycle(self, inspection_cycle):
        logger.info(f"选择巡检周期为{inspection_cycle}")
        self.click_element(OperationManagementInfoLocator.inspection_cycle_select_loc)
        self.random_sleep(0.5)
        if inspection_cycle == "":
            logger.info("未填写巡检周期，选择默认值：一月一次")
            self.click_element(OperationManagementInfoLocator.inspection_cycle_one_month_loc)
        else:
            try:
                logger.info(f"选择巡检周期为{inspection_cycle}")
                self.click_element((By.XPATH, f'//*[@title="{inspection_cycle}"]'))
            except:
                logger.warning("未找到巡检周期，选择默认值：一月一次")
                self.click_element(OperationManagementInfoLocator.inspection_cycle_one_month_loc)

    # 添加巡检组
    def _add_inspection_group(self, inspection_group):
        logger.info(f"添加巡检组为{inspection_group}")
        self.click_element(OperationManagementInfoLocator.add_inspection_group_button_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear(OperationManagementInfoLocator.inspection_group_name_input_loc, inspection_group)
        self.random_sleep(0.5)
        self.click_element(OperationManagementInfoLocator.add_inspection_item_button_loc)
        self.random_sleep(0.5)
        self.click_element(OperationManagementInfoLocator.inspection_item_select_loc)
        self.random_sleep(0.5)
        self.click_element(OperationManagementInfoLocator.inspection_item_one_loc)

    # 点击批量下载巡检码按钮
    def _click_batch_download_inspection_code_button(self):
        logger.info("点击批量下载巡检码按钮")
        self.click_element(OperationManagementInfoLocator.batch_download_inspection_code_button_loc)

    # 填写运维管理信息界面数据
    def fill_operation_maintenance_management_info(self, operation_maintenance_person, first_inspection_time,
                                                   inspection_cycle, inspection_group):
        self._select_operation_maintenance_person(operation_maintenance_person)  # 选择运维负责人
        self._fill_first_inspection_time(first_inspection_time)  # 填写首次巡检时间
        self._select_inspection_cycle(inspection_cycle)  # 选择巡检周期
        if inspection_group != "":
            self._add_inspection_group(inspection_group)  # 添加巡检组


    # 必填项 =========================================
    # 请选择运维负责人
    def get_operation_maintenance_person_required_text(self):
        return self.text(OperationManagementInfoLocator.operation_responsible_required_text_loc)

    # 请选择首次巡检时间
    def get_first_inspection_time_required_text(self):
        return self.text(OperationManagementInfoLocator.first_inspection_time_required_text_loc)

    # 请选择巡检周期
    def get_inspection_cycle_required_text(self):
        return self.text(OperationManagementInfoLocator.inspection_cycle_required_text_loc)

    # 点击查询
    def click_search_button(self):
        logger.debug("点击查询按钮")
        self.click_element(ElectronicArchivesLocator.search_button_loc)
    # 点击重置
    def click_reset_button(self):
        logger.debug("点击重置按钮")
        self.click_element(ElectronicArchivesLocator.reset_button_loc)
    # 项目名称查询
    def search_by_project_name(self, project_name):
        logger.info(f"输入项目名称为{project_name}")
        self.send_keys_by_clear(ElectronicArchivesLocator.project_name_input_loc, project_name)