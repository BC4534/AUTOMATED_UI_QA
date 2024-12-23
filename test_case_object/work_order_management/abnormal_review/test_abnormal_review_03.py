import allure
import pytest

from common.loggerhandler import Logger
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import AbnormalStatisticPage

logger = Logger()

@allure.title("异常复盘-显示数据条件切换")
@allure.feature("异常复盘")
@pytest.mark.usefixtures("login_driver")
class TestAbnormalReview03(object):
    """
            场景类型切换
    """
    # 产品类型切换
    def test_abnormal_review_03(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_statistic_page  = AbnormalStatisticPage(login_driver)
            abnormal_statistic_page.switch_to_abnormal_statistic_page()
            abnormal_statistic_page.test_abnormal_statistic_03_1()
            assert abnormal_statistic_page.get_scene_type_input_text() == "部件"
            abnormal_statistic_page.test_abnormal_statistic_03_2()
            assert abnormal_statistic_page.get_scene_type_input_text() == "厂商"
            abnormal_statistic_page.test_abnormal_statistic_03_3()
            logger.info(f"{self.__class__.__name__}执行用例成功")

        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            abnormal_statistic_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e