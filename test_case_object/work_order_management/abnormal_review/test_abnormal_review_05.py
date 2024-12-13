import allure
import pytest

from common.mylogger import Logger
from test_case_page.work_order_management.abnormal_review.abnormal_details_page import AbnormalDetailsPage
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import AbnormalStatisticPage

logger = Logger()

@allure.title("异常复盘-异常明细界面跳转")
@allure.feature("异常复盘")
@pytest.mark.usefixtures("login_driver")
class TestAbnormalReview04(object):
    """
            异常明细界面跳转
    """
    # 异常明细界面跳转
    def test_abnormal_review_05(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page  = AbnormalDetailsPage(login_driver)
            abnormal_details_page.switch_to_abnormal_details_page()
            assert abnormal_details_page.get_abnormal_details_title() == "异常明细"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e