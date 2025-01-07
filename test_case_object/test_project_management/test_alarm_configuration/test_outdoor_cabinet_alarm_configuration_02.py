import allure
import pyautogui

from common.loggerhandler import logger
from test_case_page.project_management.alarm_configuration_page.outdoor_cabinet_alarm_configuration_page import \
    OutdoorCabinetAlarmConfigurationPage


@allure.feature("项目管理")
@allure.story("项目告警配置")
@allure.title("批量更新按钮")
class TestOutdoorCabinetAlarmConfiguration02:

    """
    现用例只能保证按钮能下载文件，不能保证文件内容准确性
    """

    @allure.description("直接点击批量导出按钮")
    def test_outdoor_cabinet_alarm_configuration_02(self, login_driver):
        outdoor_cabinet_alarm_configuration_page = OutdoorCabinetAlarmConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            outdoor_cabinet_alarm_configuration_page.switch_to_outdoor_cabinet_alarm_configuration_page()
            outdoor_cabinet_alarm_configuration_page.click_outdoor_cabinet_alarm_configuration_batch_export_button()
            # x, y = pyautogui.position()
            # print(f"当前鼠标位置: X: {x}, Y: {y}")
            pyautogui.click(x=730, y=558)
            handels = outdoor_cabinet_alarm_configuration_page.get_window_handles()
            logger.info(f"当前窗口句柄数量: {len(handels)}")
            assert len(handels) == 2
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败，失败原因为：{e}")
            outdoor_cabinet_alarm_configuration_page.get_screenshot_png("直接点击批量导出按钮")
            raise e

