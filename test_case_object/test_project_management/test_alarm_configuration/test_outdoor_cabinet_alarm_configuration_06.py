import allure

from common.loggerhandler import logger
from test_case_page.project_management.alarm_configuration_page.outdoor_cabinet_alarm_configuration_page import \
    OutdoorCabinetAlarmConfigurationPage
edit_data = {
        "alarm_type": "BMS",
        "alarm_level": "三级",
        "description": "UI测试编辑运维告警描述内容"
}

@allure.feature("项目管理")
@allure.story("项目告警配置")
@allure.title("户外柜告警配置查询功能柜")
class TestOutdoorCabinetAlarmConfiguration06:


    @allure.description("设备名称查询")
    def test_outdoor_cabinet_alarm_configuration_06_01(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            second_device_name = outdoor_cabinet_alarm_configuration_page.get_second_device_name()
            outdoor_cabinet_alarm_configuration_page.input_device_name_search_condition(second_device_name)
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            assert outdoor_cabinet_alarm_configuration_page.get_first_device_name() == second_device_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("设备名称查询")
            raise e

    @allure.description("户外柜规格查询")
    def test_outdoor_cabinet_alarm_configuration_06_02(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.outdoor_cabinet_specification_search(outdoor_cabinet_specification="215户外柜国标1.0")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() == "215户外柜国标1.0"
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.outdoor_cabinet_specification_search(outdoor_cabinet_specification="215户外柜国标2.0")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() == "215户外柜国标2.0"
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.outdoor_cabinet_specification_search(
                outdoor_cabinet_specification="232户外柜")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() == "232户外柜"
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.outdoor_cabinet_specification_search(
                outdoor_cabinet_specification="372户外柜")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_outdoor_cabinet_specification() == "372户外柜"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("户外柜规格查询")
            raise e

    @allure.description("告警名称查询")
    def test_outdoor_cabinet_alarm_configuration_06_03(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            second_alarm_name = outdoor_cabinet_alarm_configuration_page.get_second_alarm_name()
            outdoor_cabinet_alarm_configuration_page.input_alarm_name_search_condition(second_alarm_name)
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_name() == second_alarm_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("告警名称查询")
            raise e

    @allure.description("运维告警描述查询")
    def test_outdoor_cabinet_alarm_configuration_06_04(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            second_alarm_description = outdoor_cabinet_alarm_configuration_page.get_second_alarm_description()
            outdoor_cabinet_alarm_configuration_page.input_alarm_description_search_condition(second_alarm_description)
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_alarm_description() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_description() == second_alarm_description
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("运维告警类型查询")
            raise e

    @allure.description("运维告警类型查询")
    def test_outdoor_cabinet_alarm_configuration_06_05(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.input_alarm_type_search_condition("EMS")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_alarm_type() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_type() == "EMS"
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.input_alarm_type_search_condition("PCS")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_alarm_type() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_type() == "PCS"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("运维告警类型查询")
            raise e

    @allure.description("是否告警查询")
    def test_outdoor_cabinet_alarm_configuration_06_06(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.input_alarm_is_alarm_search_condition("是")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_alarm_level() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_is_alarm() == "是"
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.input_alarm_is_alarm_search_condition("否")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_alarm_level() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_is_alarm() == "否"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("是否告警查询")
            raise e

    @allure.description("是否自动生成工单查询")
    def test_outdoor_cabinet_alarm_configuration_06_07(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.input_alarm_is_auto_create_work_order_search_condition("是")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_alarm_is_auto_create_work_order() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_is_alarm() == "是"
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            outdoor_cabinet_alarm_configuration_page.input_alarm_is_auto_create_work_order_search_condition("否")
            outdoor_cabinet_alarm_configuration_page.click_search_button()
            if outdoor_cabinet_alarm_configuration_page.get_first_alarm_is_auto_create_work_order() != 1:
                assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_is_alarm() == "否"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("是否自动生成工单查询")
            raise e

    @allure.description("最后修改人查询")
    def test_outdoor_cabinet_alarm_configuration_06_08(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_reset_button()
            second_modified = outdoor_cabinet_alarm_configuration_page.get_second_alarm_last_modifier()
            if second_modified != 1:
                outdoor_cabinet_alarm_configuration_page.input_alarm_last_modifier_search_condition(second_modified)
                outdoor_cabinet_alarm_configuration_page.click_search_button()
                if outdoor_cabinet_alarm_configuration_page.get_first_alarm_last_modifier() != 1:
                    assert outdoor_cabinet_alarm_configuration_page.get_first_alarm_last_modifier() == second_modified
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("最后修改人查询")
            raise e




