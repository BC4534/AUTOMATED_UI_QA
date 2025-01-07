import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.abnormal_review.abnormal_details_page import AbnormalDetailsPage



@allure.feature("工单管理")
@allure.story("异常复盘")
@allure.title("异常明细")
class TestAbnormalReview05(object):
    """
            异常明细界面跳转
    """
    # 异常明细界面跳转
    @allure.description("异常明细界面跳转")
    def test_abnormal_review_05(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            assert abnormal_details_page._get_abnormal_details_is_active()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e