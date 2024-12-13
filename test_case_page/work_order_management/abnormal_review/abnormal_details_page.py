import time

from common.base_method import BasePage
from test_case_locator.work_order_management.abnormal_review.abnormal_details_locator import AbnormalDetailsLocator


class AbnormalDetailsPage(BasePage):
    """异常详情界面"""

    # 切换至异常明细界面
    def switch_to_abnormal_details_page(self):
        self.click_element(AbnormalDetailsLocator.work_order_management_loc)
        self.click_element(AbnormalDetailsLocator.abnormal_review_loc)
        self.click_element(AbnormalDetailsLocator.abnormal_detail_loc)
        time.sleep(0.5)


    # 获取异常明细界面标题
    def get_abnormal_details_title(self):
        return self.text(AbnormalDetailsLocator.abnormal_detail_loc)