import allure

from common.loggerhandler import logger
from test_case_page.project_management.alarm_configuration_page.outdoor_cabinet_alarm_configuration_page import (
    OutdoorCabinetAlarmConfigurationPage,
)


@allure.feature("项目管理")
@allure.story("项目告警配置")
@allure.title("翻页")
class TestOutdoorCabinetAlarmConfiguration04:
    """
    现在只能保证批量跟新界面正常弹出，功能不保证
    """

    @allure.description("验证翻页功能")
    def test_outdoor_cabinet_alarm_configuration_04(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(
            login_driver
        )
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            assert outdoor_cabinet_alarm_configuration_page.test_page_turning()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("验证翻页功能")
            raise e
