import allure
import pytest
from common.loggerhandler import logger
from test_case_page.work_order_management.abnormal_review.abnormal_details_page import (
    AbnormalDetailsPage,
)
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import (
    AbnormalStatisticPage,
)


@allure.feature("工单管理")
@allure.story("异常复盘")
@allure.title("异常明细")
class TestAbnormalReview07:

    @allure.description("异常明细-附件按钮")
    def test_abnormal_review_07(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_first_work_order_attachment_button()
            abnormal_details_page.click_attachment_dialog_close_button()
            abnormal_details_page.click_first_work_order_attachment_button()
            abnormal_details_page.click_attachment_dialog_cancel_button()
            abnormal_details_page.click_first_work_order_attachment_button()
            abnormal_details_page.click_attachment_dialog_confirm_button()
            assert abnormal_details_page._get_attachment_dialog_is_displayed() == False
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
