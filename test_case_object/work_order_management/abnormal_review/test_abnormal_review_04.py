import allure
import pytest

from common.loggerhandler import Logger
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import AbnormalStatisticPage

logger = Logger()

@allure.title("异常复盘-显示数据条件切换")
@allure.feature("异常复盘")
@pytest.mark.usefixtures("login_driver")
class TestAbnormalReview04(object):
    """
            时间维度切换
    """
    # 时间维度切换
    def test_abnormal_review_04(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_statistic_page  = AbnormalStatisticPage(login_driver)
            abnormal_statistic_page.switch_to_abnormal_statistic_page()
            abnormal_statistic_page.test_abnormal_statistic_04_1()
            assert abnormal_statistic_page.get_time_dimension_input_text() == "月"
            abnormal_statistic_page.test_abnormal_statistic_04_2()
            assert abnormal_statistic_page.get_time_dimension_input_text() == "年"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            abnormal_statistic_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e