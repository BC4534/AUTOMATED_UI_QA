import allure
import pytest

from common.loggerhandler import logger
from test_case_page.project_management.alarm_configuration_page.outdoor_cabinet_alarm_configuration_page import (
    OutdoorCabinetAlarmConfigurationPage,
)


@allure.feature("项目管理")
@allure.story("项目告警配置")
@allure.title("点击批量更新")
@pytest.mark.skip(reason="暂时不能关闭win系统下载文件弹框,先跳过")
class TestOutdoorCabinetAlarmConfiguration03:
    """
    现在只能保证批量跟新界面正常弹出，功能不保证
    """

    @allure.description("点击批量更新")
    def test_outdoor_cabinet_alarm_configuration_03(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(
            login_driver
        )
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            # outdoor_cabinet_alarm_configuration_page.click_batch_update_button()
            # outdoor_cabinet_alarm_configuration_page.click_batch_update_cancel_button()
            # outdoor_cabinet_alarm_configuration_page.click_batch_update_button()
            # outdoor_cabinet_alarm_configuration_page.click_batch_update_close_button()
            # outdoor_cabinet_alarm_configuration_page.click_batch_update_button()
            # outdoor_cabinet_alarm_configuration_page.click_batch_update_confirm_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")

        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("点击批量更新")
            raise e
