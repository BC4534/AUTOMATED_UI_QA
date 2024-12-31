from selenium.webdriver.common.by import By
from test_case_locator.project_management.electronic_archives_locator.add_project_locator import \
    ProjectDetailInfoLocator
from test_case_page.project_management.electronic_archives_page.add_project_basic_info_page import \
    AddProjectBaseInfoPage
from common.loggerhandler import logger

class AddProjectDetailInfoPage(AddProjectBaseInfoPage):

    # 切换至详细资料维护界面
    def switch_to_project_detail_info(self):
        self.click_element(ProjectDetailInfoLocator.project_detail_info_page_loc)


    # 电站详细信息部分填写
    def fill_station_detail_info(self, owner_name, project_address, station_name, station_contact, station_contact_phone,
                                 total_package_unit_name, our_supply_range, project_start_end_time, station_internal_storage_unit_grouping,
                                 station_belong_province, station_belong_city, station_belong_area, longitude, latitude):
        # 业主姓名
        self.send_keys_by_clear(ProjectDetailInfoLocator.owner_name_input_loc,owner_name)
        # 项目地址
        self.send_keys_by_clear(ProjectDetailInfoLocator.project_address_input_loc,project_address)
        # 电站名称
        self.send_keys_by_clear(ProjectDetailInfoLocator.station_name_input_loc,station_name)
        # 电站联系人
        self.send_keys_by_clear(ProjectDetailInfoLocator.station_contact_input_loc,station_contact)
        # 电站联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.station_contact_phone_input_loc,station_contact_phone)
        # 总包单位名称
        self.send_keys_by_clear(ProjectDetailInfoLocator.total_package_unit_name_input_loc,total_package_unit_name)
        # 我方供货范围
        self.send_keys_by_clear(ProjectDetailInfoLocator.our_supply_range_input_loc,our_supply_range)
        # 质保期起止时间
        # self.send_keys_by_clear(ProjectDetailInfoLocator.warranty_period_input_loc,project_start_end_time)
        self.click_element(ProjectDetailInfoLocator.warranty_period_start_time_loc)
        # 时间这个还可以优化，先暂时选近两个月的1号
        self.click_element(ProjectDetailInfoLocator.current_month_1_loc)
        self.random_sleep(0.5)
        self.click_element(ProjectDetailInfoLocator.next_month_1_loc)
        # 电站内储能单位分组情况
        self.send_keys_by_clear(ProjectDetailInfoLocator.station_internal_storage_unit_grouping_input_loc,station_internal_storage_unit_grouping)
        # 电站所属省
        self.send_keys_by_clear(ProjectDetailInfoLocator.station_belong_province_input_loc,station_belong_province)
        # 电站所属市
        self.send_keys_by_clear(ProjectDetailInfoLocator.station_belong_city_input_loc,station_belong_city)
        # 电站所属区/镇
        self.send_keys_by_clear(ProjectDetailInfoLocator.station_belong_area_input_loc,station_belong_area)
        # 经度
        self.send_keys(ProjectDetailInfoLocator.longitude_input_loc,longitude)
        # 纬度
        self.send_keys(ProjectDetailInfoLocator.latitude_input_loc,latitude)

    # 设备配置信息填写
    def fill_device_configuration_info(self,battery_cabinet_number, single_battery_cabinet_capacity, pcs_type, pcs_unit_number,
                                       battery_material, battery_grouping_method, pcs_max_power, battery_cluster_grouping_method,
                                       battery_module_grouping_method,single_cell_capacity,charge_discharge_efficiency,fire_medium,
                                       rated_charge_discharge_rate,associated_station_information):

        # 电池仓数量(个)输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.battery_cabinet_number_input_loc, battery_cabinet_number)
        # 单台电池仓容量(kWh)输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.battery_cabinet_capacity_input_loc,
                                single_battery_cabinet_capacity)
        # PCS类型
        self.click_element(ProjectDetailInfoLocator.pcs_type_select_loc)
        if pcs_type != " ":
            if pcs_type == "组串式":
                self.click_element(ProjectDetailInfoLocator.pcs_type_group_string_loc)
            elif pcs_type == "集中式":
                self.click_element(ProjectDetailInfoLocator.pcs_type_centralized_loc)
            elif pcs_type == "构网式":
                self.click_element(ProjectDetailInfoLocator.pcs_type_grid_loc)
            else:
                logger.info("输入的PCS类型不正确，默认选择组串式")
                self.click_element(ProjectDetailInfoLocator.pcs_type_group_string_loc)
        else:
            logger.info("输入的PCS类型不正确，默认选择组串式")
            self.click_element(ProjectDetailInfoLocator.pcs_type_group_string_loc)
        # PCS一体机数量(个)输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.pcs_unit_number_input_loc, pcs_unit_number)
        # 电芯材料选择框
        self.click_element(ProjectDetailInfoLocator.battery_material_select_loc)
        if battery_material != "":
            if battery_material == "磷酸铁锂":
                self.click_element(ProjectDetailInfoLocator.battery_material_phosphor_iron_battery_loc)
            else:
                logger.info("输入的电芯材料不正确，默认选择磷酸铁锂")
                self.click_element(ProjectDetailInfoLocator.battery_material_phosphor_iron_battery_loc)
        else:
            logger.info("输入的电芯材料不正确，默认选择磷酸铁锂")
            self.click_element(ProjectDetailInfoLocator.battery_material_phosphor_iron_battery_loc)

        # 电池堆成组方式输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.battery_grouping_method_input_loc, battery_grouping_method)
        # 单台PCS最大功率(kW)输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.pcs_max_power_input_loc, pcs_max_power)
        # 电池簇组成组方式输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.battery_cluster_grouping_method_input_loc,
                                battery_cluster_grouping_method)
        # 电池模组成组方式输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.battery_module_grouping_method_input_loc,
                                battery_module_grouping_method)
        # 单电芯额定容量(Ah)输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.single_cell_capacity_input_loc, single_cell_capacity)
        # 充放电转换效率(%)输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.charge_discharge_efficiency_input_loc,
                                charge_discharge_efficiency)
        # 消防介质输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.fire_medium_input_loc, fire_medium)
        # 额定充放电倍率(C)输入框
        self.send_keys_by_clear(ProjectDetailInfoLocator.rated_charge_discharge_rate_input_loc,
                                rated_charge_discharge_rate)
        # 关联电站信息
        if associated_station_information != "":
            self.click_element(ProjectDetailInfoLocator.associated_station_information_select_loc)
            # //*[@title="XZ"]
            try:
                self.click_element((By.XPATH, f'//*[@title="{associated_station_information}"]'))
            except:
                logger.info("输入的关联电站信息不正确，默认不选择关联电站信息")
            self.click_element(ProjectDetailInfoLocator.associated_station_information_text_loc)
            self.random_sleep(0.5)


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
        # BMS厂商
        self.click_element(ProjectDetailInfoLocator.bms_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{bms_vendor}"]'))
        self.random_sleep(0.5)
        # BMS厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.bms_vendor_contact_phone_input_loc, bms_vendor_phone)
        self.random_sleep(0.5)

        # PCS厂商
        self.click_element(ProjectDetailInfoLocator.pcs_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{pcs_vendor}"]'))
        self.random_sleep(0.5)
        # PCS厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.pcs_vendor_contact_phone_input_loc, pcs_vendor_phone)
        self.random_sleep(0.5)

        # 变压器厂商
        self.click_element(ProjectDetailInfoLocator.transformer_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{transformer_vendor}"]'))
        self.random_sleep(0.5)
        # 变压器厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.transformer_vendor_contact_phone_input_loc,
                                transformer_vendor_phone)
        self.random_sleep(0.5)

        # 液冷系统厂商
        self.click_element(ProjectDetailInfoLocator.liquid_cooling_system_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{liquid_cooling_system_vendor}"]'))
        self.random_sleep(0.5)
        # 液冷系统厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.liquid_cooling_system_vendor_contact_phone_input_loc,
                                liquid_cooling_system_vendor_phone)
        self.random_sleep(0.5)

        # 空调厂商
        self.click_element(ProjectDetailInfoLocator.air_conditioner_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{air_conditioner_vendor}"]'))
        self.random_sleep(0.5)
        # 空调厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.air_conditioner_vendor_contact_phone_input_loc,
                                air_conditioner_vendor_phone)
        self.random_sleep(0.5)

        # PACK组装厂厂商
        self.click_element(ProjectDetailInfoLocator.pack_assembly_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{pack_assembly_vendor}"]'))
        self.random_sleep(0.5)
        # PACK组装厂厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.pack_assembly_vendor_contact_phone_input_loc,
                                pack_assembly_vendor_phone)
        self.random_sleep(0.5)

        # 电芯厂商
        self.click_element(ProjectDetailInfoLocator.cell_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{cell_vendor}"]'))
        self.random_sleep(0.5)
        # 电芯厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.cell_vendor_contact_phone_input_loc, cell_vendor_phone)
        self.random_sleep(0.5)

        # 电池仓箱体厂商
        self.click_element(ProjectDetailInfoLocator.battery_box_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{battery_box_vendor}"]'))
        self.random_sleep(0.5)
        # 电池仓箱体厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.battery_box_vendor_contact_phone_input_loc,
                                battery_box_vendor_phone)
        self.random_sleep(0.5)

        # 消防厂商
        self.click_element(ProjectDetailInfoLocator.fire_protection_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{fire_protection_vendor}"]'))
        self.random_sleep(0.5)
        # 消防厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.fire_protection_vendor_contact_phone_input_loc,
                                fire_protection_vendor_phone)
        self.random_sleep(0.5)

        # EMS厂商
        self.click_element(ProjectDetailInfoLocator.ems_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{ems_vendor}"]'))
        self.random_sleep(0.5)
        # EMS厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.ems_vendor_contact_phone_input_loc, ems_vendor_phone)
        self.random_sleep(0.5)

        # 汇流柜厂商
        self.click_element(ProjectDetailInfoLocator.busbar_cabinet_vendor_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{busbar_cabinet_vendor}"]'))
        self.random_sleep(0.5)
        # 汇流柜厂商联系方式
        self.send_keys_by_clear(ProjectDetailInfoLocator.busbar_cabinet_vendor_contact_phone_input_loc,
                                busbar_cabinet_vendor_phone)
        self.random_sleep(0.5)

    # ===必填项断言===
    # 业主名称必填项
    def get_owner_required_text(self):
        return self.text(ProjectDetailInfoLocator.owner_required_loc)

    # 电池仓个数必填项
    def get_battery_box_number_required_text(self):
        return self.text(ProjectDetailInfoLocator.battery_box_number_required_loc)
    # bms厂商必填项
    def get_bms_vendor_required_text(self):
        return self.text(ProjectDetailInfoLocator.bms_vendor_required_loc)
















