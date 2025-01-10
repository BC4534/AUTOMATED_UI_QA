import allure
from test_case_page.project_management.electronic_archives_page.add_operation_maintenance_management_info_page import (
    AddOperationMaintenanceManagementInfoPage,
)

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
    "latitude": "31.0",
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
    "associated_station_information": "UI测试关联电站信息",
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
    "maintain_implement_person": "系统管理员",
}
operation_maintenance_management_info_data = {
    "first_inspection_time": "2023-01-01",
    "operation_maintenance_person": "系统管理员",
    "inspection_cycle": "1",
    "inspection_group": "",
}


@allure.title("电子档案管理模块-新增项目")
@allure.feature("项目管理模块")
@allure.story("电子档案功能")
class TestElectronicArchives02:

    @allure.description("新增项目")
    def test_electronic_archives_02_1(self, login_driver):
        add_election_archives_page = AddOperationMaintenanceManagementInfoPage(
            login_driver
        )
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_election_archives_page.switch_to_electronic_archives()
            add_election_archives_page.click_add_project_button()
            add_election_archives_page.fill_basic_information(
                init_time=base_info_data["init_time"],
                project_name=base_info_data["project_name"],
                project_install_power=base_info_data["project_install_power"],
                project_install_capacity=base_info_data["project_install_capacity"],
                project_stage=base_info_data["project_stage"],
                project_progress=base_info_data["project_progress"],
                project_type=base_info_data["project_type"],
                product_type=base_info_data["product_type"],
                outdoor_cabinet_type=base_info_data["outdoor_cabinet_type"],
                project_area=base_info_data["project_area"],
                is_support_inspection=base_info_data["is_support_inspection"],
            )
            logger.debug("填写基本信息成功")
            add_election_archives_page.click_next_button()  # 填写完基础数据，前往详细数据
            add_election_archives_page.fill_station_detail_info(
                owner_name=detail_info_station_station_data["owner_name"],
                project_address=detail_info_station_station_data["project_address"],
                station_name=detail_info_station_station_data["station_name"],
                station_contact=detail_info_station_station_data["station_contact"],
                station_contact_phone=detail_info_station_station_data[
                    "station_contact_phone"
                ],
                total_package_unit_name=detail_info_station_station_data[
                    "total_package_unit_name"
                ],
                our_supply_range=detail_info_station_station_data["our_supply_range"],
                project_start_end_time=detail_info_station_station_data[
                    "project_start_end_time"
                ],
                station_internal_storage_unit_grouping=detail_info_station_station_data[
                    "station_internal_storage_unit_grouping"
                ],
                station_belong_province=detail_info_station_station_data[
                    "station_belong_province"
                ],
                station_belong_city=detail_info_station_station_data[
                    "station_belong_city"
                ],
                station_belong_area=detail_info_station_station_data[
                    "station_belong_area"
                ],
                longitude=detail_info_station_station_data["longitude"],
                latitude=detail_info_station_station_data["latitude"],
            )
            logger.debug("填写详细信息-电站信息成功")
            add_election_archives_page.fill_device_configuration_info(
                battery_cabinet_number=datail_info_device_configuration_data[
                    "battery_cabinet_number"
                ],
                single_battery_cabinet_capacity=datail_info_device_configuration_data[
                    "single_battery_cabinet_capacity"
                ],
                pcs_type=datail_info_device_configuration_data["pcs_type"],
                pcs_unit_number=datail_info_device_configuration_data[
                    "pcs_unit_number"
                ],
                battery_material=datail_info_device_configuration_data[
                    "battery_material"
                ],
                battery_grouping_method=datail_info_device_configuration_data[
                    "battery_grouping_method"
                ],
                pcs_max_power=datail_info_device_configuration_data["pcs_max_power"],
                battery_cluster_grouping_method=datail_info_device_configuration_data[
                    "battery_cluster_grouping_method"
                ],
                battery_module_grouping_method=datail_info_device_configuration_data[
                    "battery_module_grouping_method"
                ],
                single_cell_capacity=datail_info_device_configuration_data[
                    "single_cell_capacity"
                ],
                charge_discharge_efficiency=datail_info_device_configuration_data[
                    "charge_discharge_efficiency"
                ],
                fire_medium=datail_info_device_configuration_data["fire_medium"],
                rated_charge_discharge_rate=datail_info_device_configuration_data[
                    "rated_charge_discharge_rate"
                ],
                associated_station_information=datail_info_device_configuration_data[
                    "associated_station_information"
                ],
            )
            logger.debug("填写详细信息-设备配置信息成功")
            add_election_archives_page.fill_manufacturer_info(
                bms_vendor=detail_info_manufacturer_data["bms_vendor"],
                bms_vendor_phone=detail_info_manufacturer_data["bms_vendor_phone"],
                pcs_vendor=detail_info_manufacturer_data["pcs_vendor"],
                pcs_vendor_phone=detail_info_manufacturer_data["pcs_vendor_phone"],
                transformer_vendor=detail_info_manufacturer_data["transformer_vendor"],
                transformer_vendor_phone=detail_info_manufacturer_data[
                    "transformer_vendor_phone"
                ],
                liquid_cooling_system_vendor=detail_info_manufacturer_data[
                    "liquid_cooling_system_vendor"
                ],
                liquid_cooling_system_vendor_phone=detail_info_manufacturer_data[
                    "liquid_cooling_system_vendor_phone"
                ],
                air_conditioner_vendor=detail_info_manufacturer_data[
                    "air_conditioner_vendor"
                ],
                air_conditioner_vendor_phone=detail_info_manufacturer_data[
                    "air_conditioner_vendor_phone"
                ],
                pack_assembly_vendor=detail_info_manufacturer_data[
                    "pack_assembly_vendor"
                ],
                pack_assembly_vendor_phone=detail_info_manufacturer_data[
                    "pack_assembly_vendor_phone"
                ],
                cell_vendor=detail_info_manufacturer_data["cell_vendor"],
                cell_vendor_phone=detail_info_manufacturer_data["cell_vendor_phone"],
                battery_box_vendor=detail_info_manufacturer_data["battery_box_vendor"],
                battery_box_vendor_phone=detail_info_manufacturer_data[
                    "battery_box_vendor_phone"
                ],
                fire_protection_vendor=detail_info_manufacturer_data[
                    "fire_protection_vendor"
                ],
                fire_protection_vendor_phone=detail_info_manufacturer_data[
                    "fire_protection_vendor_phone"
                ],
                ems_vendor=detail_info_manufacturer_data["ems_vendor"],
                ems_vendor_phone=detail_info_manufacturer_data["ems_vendor_phone"],
                busbar_cabinet_vendor=detail_info_manufacturer_data[
                    "busbar_cabinet_vendor"
                ],
                busbar_cabinet_vendor_phone=detail_info_manufacturer_data[
                    "busbar_cabinet_vendor_phone"
                ],
            )
            add_election_archives_page.click_next_button()  # 前往维护实施管理界面

            add_election_archives_page.fill_maintain_implement_info(
                maintain_implement_info=maintain_implement_info_data[
                    "maintain_implement_info"
                ],
                maintain_implement_person=maintain_implement_info_data[
                    "maintain_implement_person"
                ],
            )
            logger.debug("填写维护实施管理信息成功")
            add_election_archives_page.click_next_button()  # 前往运维管理界面
            add_election_archives_page.fill_operation_maintenance_management_info(
                operation_maintenance_person=operation_maintenance_management_info_data[
                    "operation_maintenance_person"
                ],
                first_inspection_time=operation_maintenance_management_info_data[
                    "first_inspection_time"
                ],
                inspection_cycle=operation_maintenance_management_info_data[
                    "inspection_cycle"
                ],
                inspection_group=operation_maintenance_management_info_data[
                    "inspection_group"
                ],
            )
            logger.debug("填写运维管理信息成功")
            add_election_archives_page.click_submit_button()
            assert (
                add_election_archives_page.get_first_project_name()
                == base_info_data["project_name"]
            )
            add_election_archives_page.delete_first_project()

        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_election_archives_page.get_screenshot_png(f"{self.__class__.__name__}")
            if (
                add_election_archives_page.get_first_project_name()
                == base_info_data["project_name"]
            ):
                add_election_archives_page.delete_first_project()
            raise e

    @allure.description("验证新增项目弹框文本")
    def test_electronic_archives_02_2(self, login_driver):
        add_election_archives_page = AddOperationMaintenanceManagementInfoPage(
            login_driver
        )
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_election_archives_page.switch_to_electronic_archives()
            add_election_archives_page.click_add_project_button()
            assert add_election_archives_page.get_add_edit_project_title() == "新增项目"
            add_election_archives_page.click_close_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_election_archives_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
