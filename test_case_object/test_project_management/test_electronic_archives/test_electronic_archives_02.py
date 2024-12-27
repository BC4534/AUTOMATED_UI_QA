import allure

from test_case_page.project_management.electronic_archives_page.add_project_basic_info_page import \
    AddProjectBaseInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_detail_info_page import \
    AddProjectDetailInfoPage
from test_case_page.project_management.electronic_archives_page.electronic_archives_page import ElectronicArchivesPage
from common.loggerhandler import logger



@allure.title("电子档案管理模块")
@allure.description("新增项目")
class TestElectronicArchives02:

    def test_electronic_archives_02(self, login_driver):
        add_project_detail_info_page = AddProjectDetailInfoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            add_project_detail_info_page.switch_to_electronic_archives()
            add_project_detail_info_page.click_add_project_button()
            add_project_detail_info_page.fill_electronic_archives_02_basic_information(
                init_time="20241226",
                project_name="测试项目",
                project_install_power="1000",
                project_install_capacity="1000",
                project_stage="待实施阶段11",
                project_progress="待实施",
                project_type="项目",
                product_type="产品",
                project_area="东部",
                is_support_inspection="s",
                outdoor_cabinet_type=" outdoor_cabinet_type"
            )
            add_project_detail_info_page.click_next_button()
            # add_project_detail_info_page.click_first_project_edit_next()
            # owner_name, project_address, station_name, station_contact, station_contact_phone,
            # total_package_unit_name, our_supply_range, warranty_period, station_internal_storage_unit_grouping,
            # station_belong_province, station_belong_city, station_belong_area, longitude, latitude
            add_project_detail_info_page.fill_station_detail_info(
                owner_name="10",
                project_address="11",
                station_name="12",
                station_contact="13",
                station_contact_phone="14",
                total_package_unit_name="15",
                our_supply_range="16",
                project_start_end_time="17",
                station_internal_storage_unit_grouping="18",
                station_belong_province="19",
                station_belong_city="20",
                station_belong_area="21",
                longitude=23,
                latitude=24

            )
            add_project_detail_info_page.fill_device_configuration_info(
                battery_cabinet_number=11,
                single_battery_cabinet_capacity=12,
                pcs_type="13",
                pcs_unit_number=14,
                battery_material="15",
                battery_grouping_method="16",
                pcs_max_power="17",
                battery_cluster_grouping_method="18",
                battery_module_grouping_method="19",
                single_cell_capacity="20",
                charge_discharge_efficiency="21",
                fire_medium="22",
                rated_charge_discharge_rate="23",
                associated_station_information="XZ"
            )
            add_project_detail_info_page.fill_manufacturer_info(
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
            )
            add_project_detail_info_page.click_save_button()



        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            add_project_detail_info_page.get_screenshot_png(f"{self.__class__.__name__}")

