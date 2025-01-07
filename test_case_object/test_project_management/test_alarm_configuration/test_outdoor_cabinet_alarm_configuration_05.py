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
@allure.title("编辑")
class TestOutdoorCabinetAlarmConfiguration05:


    @allure.description("编辑-必填项效验")
    def test_outdoor_cabinet_alarm_configuration_05_01(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_no_alarm_type_edit_button()
            outdoor_cabinet_alarm_configuration_page.click_edit_confirm_button()
            assert outdoor_cabinet_alarm_configuration_page.get_operation_alarm_type_required_message() == "请输入必填字段"
            outdoor_cabinet_alarm_configuration_page.click_edit_cancel_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("编辑-必填项效验")
            raise e

    @allure.description("编辑-后点取消")
    def test_outdoor_cabinet_alarm_configuration_05_02(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            loc = outdoor_cabinet_alarm_configuration_page.click_no_alarm_type_edit_button()
            des = outdoor_cabinet_alarm_configuration_page.get_edit_operation_alarm_description_content()
            outdoor_cabinet_alarm_configuration_page.edit_operation_alarm(
                description=edit_data["description"]
            )
            outdoor_cabinet_alarm_configuration_page.click_edit_cancel_button()
            outdoor_cabinet_alarm_configuration_page.click_element(loc)
            assert outdoor_cabinet_alarm_configuration_page.get_edit_operation_alarm_description_content() == des
            outdoor_cabinet_alarm_configuration_page.click_edit_cancel_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("编辑-后点取消")
            raise e

    @allure.description("编辑-后点关闭")
    def test_outdoor_cabinet_alarm_configuration_05_03(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            loc = outdoor_cabinet_alarm_configuration_page.click_no_alarm_type_edit_button()
            des = outdoor_cabinet_alarm_configuration_page.get_edit_operation_alarm_description_content()
            outdoor_cabinet_alarm_configuration_page.edit_operation_alarm(
                alarm_type=edit_data["alarm_type"],
                alarm_level=edit_data["alarm_level"],
                description=edit_data["description"]
            )
            outdoor_cabinet_alarm_configuration_page.click_edit_close_button()
            outdoor_cabinet_alarm_configuration_page.click_element(loc)
            assert outdoor_cabinet_alarm_configuration_page.get_edit_operation_alarm_description_content() == des
            outdoor_cabinet_alarm_configuration_page.click_edit_cancel_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("编辑-后点取消")
            raise e

    @allure.description("编辑-后点确认")
    def test_outdoor_cabinet_alarm_configuration_05_04(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            loc = outdoor_cabinet_alarm_configuration_page.click_no_alarm_type_edit_button()
            des = outdoor_cabinet_alarm_configuration_page.get_edit_operation_alarm_description_content()
            outdoor_cabinet_alarm_configuration_page.edit_operation_alarm(
                alarm_type=edit_data["alarm_type"],
                alarm_level=edit_data["alarm_level"],
                description=edit_data["description"]
            )
            outdoor_cabinet_alarm_configuration_page.click_edit_confirm_button()
            outdoor_cabinet_alarm_configuration_page.click_element(loc)
            assert outdoor_cabinet_alarm_configuration_page.get_edit_operation_alarm_description_content() == edit_data["description"]
            outdoor_cabinet_alarm_configuration_page.edit_operation_alarm(
                description = des
            )
            outdoor_cabinet_alarm_configuration_page.click_edit_confirm_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("编辑-后点取消")
            raise e



