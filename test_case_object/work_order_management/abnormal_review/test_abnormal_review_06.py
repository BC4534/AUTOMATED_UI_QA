import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.abnormal_review.abnormal_details_page import (
    AbnormalDetailsPage,
)


@allure.feature("工单管理")
@allure.story("异常复盘")
@allure.title("异常明细")
class TestAbnormalReview06:

    @allure.description("异常明细-异常统计部分展开合并")
    def test_abnormal_review_06(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_abnormal_statistic_expand_button()
            assert abnormal_details_page._get_abnormal_statistic_is_expand() == False
            abnormal_details_page.click_abnormal_statistic_expand_button()
            assert abnormal_details_page._get_abnormal_statistic_is_expand() == True
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
