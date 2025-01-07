import allure
import pytest

from common.loggerhandler import logger
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import AbnormalStatisticPage



@allure.feature("工单管理")
@allure.story("异常复盘")
@allure.title("异常统计")
@pytest.mark.usefixtures("login_driver")
class TestAbnormalReview04(object):
    """
            时间维度切换
    """
    # 时间维度切换
    @allure.description("时间维度切换")
    def test_abnormal_review_04(self, login_driver):
        abnormal_statistic_page = AbnormalStatisticPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_statistic_page.switch_to_abnormal_statistic_page()
            abnormal_statistic_page.test_abnormal_statistic_04_1()
            assert abnormal_statistic_page.get_time_dimension_input_text() == "月"
            abnormal_statistic_page.test_abnormal_statistic_04_2()
            assert abnormal_statistic_page.get_time_dimension_input_text() == "年"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_statistic_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e