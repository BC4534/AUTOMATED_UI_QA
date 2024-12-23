import allure
import pytest

from common.loggerhandler import Logger
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import AbnormalStatisticPage

logger = Logger()

@allure.title("异常复盘-显示数据条件切换")
@allure.feature("异常复盘")
@pytest.mark.usefixtures("login_driver")
class TestAbnormalReview02(object):
    """
            显示数据条件切换
    """
    # 产品类型切换
    def test_abnormal_review_02(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_statistic_page  = AbnormalStatisticPage(login_driver)
            abnormal_statistic_page.switch_to_abnormal_statistic_page()
            abnormal_statistic_page.test_abnormal_statistic_02_1()
            assert abnormal_statistic_page.get_product_type_input_text() == "集装箱"
            abnormal_statistic_page.test_abnormal_statistic_02_2()
            assert abnormal_statistic_page.get_product_type_input_text() == "户外柜"
            abnormal_statistic_page.test_abnormal_statistic_02_3()
            assert abnormal_statistic_page.get_product_type_input_text() == "非系统"
            abnormal_statistic_page.test_abnormal_statistic_02_4()
            assert abnormal_statistic_page.get_product_type_no_input_text() == "请选择产品类型"
            logger.info(f"{self.__class__.__name__}执行用例通过")
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            abnormal_statistic_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e