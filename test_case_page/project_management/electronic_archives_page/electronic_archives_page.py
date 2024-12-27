from common.base_method import BasePage
from test_case_locator.project_management.electronic_archives_locator.electronic_archives_locator import \
    ElectronicArchivesLocator
from test_case_locator.project_management.electronic_archives_locator.add_project_locator import \
AddProjectLocator,ProjectBaseInfoLocator,ImplementationMaintenanceInfoLocator,OperationManagementInfoLocator
from common.loggerhandler import logger



class ElectronicArchivesPage(BasePage):

    # 获取项目管理模块class属性
    def get_project_management_module_class(self):

        # ant-menu-submenu ant-menu-submenu-inline
        # ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-open ant-menu-submenu-active

        b = self.get_attribute(ElectronicArchivesLocator.project_management_module_class_attributes_loc, "class")
        logger.debug("项目管理模块class属性为：" + b)
        return b

    # 切换至电子档案界面
    def switch_to_electronic_archives(self):
        # 'ant-menu-submenu ant-menu-submenu-inline'
        if "ant-menu-submenu ant-menu-submenu-inline" == self.get_project_management_module_class():
            self.click_element(ElectronicArchivesLocator.project_management_loc)
            print(self.get_project_management_module_class())
        self.click_element_by_js(ElectronicArchivesLocator.electronic_archives_loc)
        self.logger.info("切换至电子档案界面")
    # 点击保存按钮
    def click_save_button(self):
        self.click_element(ElectronicArchivesLocator.save_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击保存按钮")
    # 点击下一步按钮
    def click_next_button(self):
        self.click_element(ElectronicArchivesLocator.next_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击下一步按钮")
    # 点击上一步按钮
    def click_previous_button(self):
        self.click_element(ElectronicArchivesLocator.previous_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击上一步按钮")
    # 点击提交
    def click_submit_button(self):
        self.click_element(ElectronicArchivesLocator.submit_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击提交按钮")

    # 获取新增项目按钮文本值
    def get_add_project_button_text(self):
        b = self.text(ElectronicArchivesLocator.add_project_button_loc)
        logger.debug("新增项目按钮文本值为：" + b)
        return b

    # 获取供应商维护按钮文本值
    def get_supplier_maintenance_button_text(self):
        b = self.text(ElectronicArchivesLocator.supplier_maintenance_button_loc)
        logger.debug("供应商维护按钮文本值为：" + b)
        return b
    # 获取产品类型的值
    def get_product_type_text(self):
        b = self.text(ProjectBaseInfoLocator.product_type_text_loc)
        logger.debug("产品类型为：" + b)
        return b


    # 获取当前年份 月份
    def get_current_year_month(self):
        year = self.text(ElectronicArchivesLocator.current_year_loc)[0:4]
        month = self.text(ElectronicArchivesLocator.current_month_loc)[0:2]
        logger.debug("当前年份为：" + year + "，当前月份为：" + month)
        return int(year), int(month)
    # 点击新增项目按钮
    def click_add_project_button(self):
        self.click_element(ElectronicArchivesLocator.add_project_button_loc)
        self.logger.info("点击新增项目按钮")

    # 新增项目
    def test_electronic_archives_02(self):
        pass

    # 填写项目基本信息
    def fill_electronic_archives_02_basic_information(self, init_time: str, project_name, project_install_power
                                                      , project_install_capacity,
                                                      project_stage, project_progress, project_type, product_type
                                                      , outdoor_cabinet_type, project_area, is_support_inspection):
        pass

    # 填写项目详情资料-站点详情信息
    def fill_station_detail_info(self, owner_name, project_address, station_name, station_contact,
                                 station_contact_phone,
                                 total_package_unit_name, our_supply_range, warranty_period,
                                 station_internal_storage_unit_grouping,
                                 station_belong_province, station_belong_city, station_belong_area, longitude,
                                 latitude):
        pass
    # 设备配置信息填写
    def fill_device_configuration_info(self,battery_cabinet_number, single_battery_cabinet_capacity, pcs_type, pcs_unit_number,
                                       battery_material, battery_grouping_method, pcs_max_power, battery_cluster_grouping_method,
                                       battery_module_grouping_method,single_cell_capacity,charge_discharge_efficiency,fire_medium,
                                       rated_charge_discharge_rate,associated_station_information):
        pass
    # 厂商信息填写
    def fill_manufacturer_info(self, bms_vendor, bms_vendor_phone,
                               pcs_vendor, pcs_vendor_phone,
                               transformer_vendor, transformer_vendor_phone,
                               liquid_cooling_system_vendor, liquid_cooling_system_vendor_phone,
                               air_conditioner_vendor, air_conditioner_vendor_phone,
                               pack_assembly_vendor, pack_assembly_vendor_phone,
                               cell_vendor, cell_vendor_phone,
                               battery_box_vendor, battery_box_vendor_phone,
                               fire_protection_vendor, fire_protection_vendor_phone,
                               ems_vendor, ems_vendor_phone,
                               busbar_cabinet_vendor, busbar_cabinet_vendor_phone):
        pass

    # 勾选第一个项目，点击编辑。点击下一步
    def click_first_project_edit_next(self):
        self.click_element(ElectronicArchivesLocator.first_project_edit_next_button_loc)
        self.click_element(ElectronicArchivesLocator.next_button_loc)






