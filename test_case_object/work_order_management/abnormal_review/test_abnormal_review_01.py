import allure
import pytest

from common.mylogger import Logger
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import AbnormalStatisticPage

logger = Logger()

@allure.title("异常复盘-切换至异常统计界面")
@allure.feature("异常复盘")
@pytest.mark.usefixtures("login_driver")
class TestAbnormalReview01(object):
    """
            切换至异常统计界面
    """
    def test_abnormal_review_01(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_statistic_page  = AbnormalStatisticPage(login_driver)
            abnormal_statistic_page.switch_to_abnormal_statistic_page()
            assert abnormal_statistic_page.get_abnormal_statistic_button_text() == "异常统计"
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            abnormal_statistic_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e