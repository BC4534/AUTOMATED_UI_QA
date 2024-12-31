import allure

from test_case_page.project_management.electronic_archives_page.add_operation_maintenance_management_info_page import \
    AddOperationMaintenanceManagementInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_basic_info_page import \
    AddProjectBaseInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_detail_info_page import \
    AddProjectDetailInfoPage
from test_case_page.project_management.electronic_archives_page.electronic_archives_page import ElectronicArchivesPage
from common.loggerhandler import logger

base_info_data = {
    "init_time": "20241226",
    "project_name": "UI自动化测试项目",
    "project_install_power": 100,
    "project_install_capacity": 100,
    "project_stage": "待实施阶段",
    "project_progress": "计划期",
    "project_type": "工商业",
    "product_type": "户外柜",
    "outdoor_cabinet_type": "215户外柜国标2.0",
    "project_area": "东部",
    "is_support_inspection": "否",
}
detail_info_station_station_data = {
    "owner_name": "UI测试业主",
    "project_address": "UI测试地址",
    "station_name": "UI测试电站名",
    "station_contact": "UI测试联系人",
    "station_contact_phone": "UI测试联系人电话",
    "total_package_unit_name": "UI测试总包单位名称",
    "our_supply_range": "UI测试我方供应商范围",
    "project_start_end_time": "UI测试质保期",
    "station_internal_storage_unit_grouping": "UI测试电站内部存储单元分组",
    "station_belong_province": "UI测试电站所属省",
    "station_belong_city": "UI测试电站所属市",
    "station_belong_area": "UI测试电站所属区",
    "longitude": "121.0",
    "latitude": "31.0"
}
datail_info_device_configuration_data = {
    "battery_cabinet_number": 11,  # 电池仓数量
    "single_battery_cabinet_capacity": 100,
    "pcs_type": "集中式",
    "pcs_unit_number": 11,
    "battery_material": "磷酸铁锂",  # 电池材料
    "battery_grouping_method": "8簇成堆",
    "pcs_max_power": 3450,
    "battery_cluster_grouping_method": "25pack成簇",
    "battery_module_grouping_method": "1pack16串电芯",
    "single_cell_capacity": 280,
    "charge_discharge_efficiency": 85,
    "fire_medium": "全氟乙酮",
    "rated_charge_discharge_rate": "0.5",
    "associated_station_information": "UI测试关联电站信息"
}
detail_info_manufacturer_data = {

    "bms_vendor": "bms供应商",
    "bms_vendor_phone": 18700000001,
    "pcs_vendor": "pcs供应商",
    "pcs_vendor_phone": 18700000002,
    "transformer_vendor": "变压器供应商",
    "transformer_vendor_phone": 18700000003,
    "liquid_cooling_system_vendor": "液冷系统供应商",
    "liquid_cooling_system_vendor_phone": 18700000004,
    "air_conditioner_vendor": "空调供应商",
    "air_conditioner_vendor_phone": 18700000005,
    "pack_assembly_vendor": "pack供应商",
    "pack_assembly_vendor_phone": 18700000006,
    "cell_vendor": "电芯供应商",
    "cell_vendor_phone": 18700000007,
    "battery_box_vendor": "电池仓箱体供应商",
    "battery_box_vendor_phone": 18700000008,
    "fire_protection_vendor": "消防供应商",
    "fire_protection_vendor_phone": 18700000009,
    "ems_vendor": "EMS供应商",
    "ems_vendor_phone": 18700000010,
    "busbar_cabinet_vendor": "汇流柜供应商",
    "busbar_cabinet_vendor_phone": 18700000011,
}
"""
                bms_vendor="bms供应商",
                bms_vendor_phone="2",
                pcs_vendor="pcs供应商",
                pcs_vendor_phone="4",
                transformer_vendor="变压器供应商",
                transformer_vendor_phone="6",
                liquid_cooling_system_vendor="液冷系统供应商",
                liquid_cooling_system_vendor_phone="8",
                air_conditioner_vendor="空调供应商",
                air_conditioner_vendor_phone="10",
                pack_assembly_vendor="pack供应商",
                pack_assembly_vendor_phone="12",
                cell_vendor="电芯供应商",
                cell_vendor_phone="14",
                battery_box_vendor="电池仓箱体供应商",
                battery_box_vendor_phone="16",
                fire_protection_vendor="消防供应商",
                fire_protection_vendor_phone="18",
                ems_vendor="EMS供应商",
                ems_vendor_phone="20",
                busbar_cabinet_vendor="汇流柜供应商",
                busbar_cabinet_vendor_phone="22"
                """
maintain_implement_info_data = {
    "maintain_implement_info": "2023-01-01",
    "maintain_implement_person": "系统管理员"
}
operation_maintenance_management_info_data = {
    "first_inspection_time": "2023-01-01",
    "operation_maintenance_person": "系统管理员",
    "inspection_cycle": "1",
    "inspection_group": ""
}


@allure.feature("项目管理模块")
@allure.story("电子档案功能")
@allure.title("查询功能")
class TestElectronicArchives09:

    @allure.description("项目名称查询")
    def test_electronic_archives_09_1(self, login_driver):
        add_election_archives_page = AddOperationMaintenanceManagementInfoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_election_archives_page.switch_to_electronic_archives()
            add_election_archives_page.click_reset_button()
            second_project_name = add_election_archives_page.get_second_project_name()
            add_election_archives_page.search_by_project_name(second_project_name)
            add_election_archives_page.click_search_button()
            first_project_name = add_election_archives_page.get_first_project_name()
            assert second_project_name in first_project_name
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_election_archives_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("立项时间查询")
    def test_electronic_archives_09_2(self, login_driver):
        add_election_archives_page = AddOperationMaintenanceManagementInfoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_election_archives_page.switch_to_electronic_archives()
            add_election_archives_page.click_reset_button()
            t = add_election_archives_page.get_second_project_init_time()
            add_election_archives_page.input_init_time_query_condition(t)
            add_election_archives_page.click_search_button()
            first_project_init_time = add_election_archives_page.get_first_project_init_time()
            assert t ==  first_project_init_time
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_election_archives_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单所属区域查询")
    def test_electronic_archives_09_3(self, login_driver):
        add_election_archives_page = AddOperationMaintenanceManagementInfoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_election_archives_page.switch_to_electronic_archives()
            add_election_archives_page.click_reset_button()
            second_project_area = add_election_archives_page.get_second_project_area()
            add_election_archives_page.select_work_order_area(second_project_area)
            add_election_archives_page.click_search_button()
            first_project_area = add_election_archives_page.get_first_project_area()
            assert second_project_area in first_project_area
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_election_archives_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e



