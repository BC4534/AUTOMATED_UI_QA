import time

from common.base_method import BasePage
from test_case_locator.work_order_management.abnormal_review.abnormal_statistic_locator import (
    AbnormalStatisticLocator,
)


class AbnormalStatisticPage(BasePage):
    """异常统计页面"""

    # 判断工单管理是否展开
    def _get_work_order_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            AbnormalStatisticLocator.work_order_management_expand_loc, "class"
        )

    # 切换至 异常统计界面
    def switch_to_abnormal_statistic_page(self):
        if self._get_work_order_management_is_expand():
            self.click_element(AbnormalStatisticLocator.work_order_management_loc)
        self.click_element(AbnormalStatisticLocator.abnormal_review_loc)

    # 产品类型切换
    def test_abnormal_statistic_02_1(self):  # 集装箱
        self.click_element(AbnormalStatisticLocator.product_type_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.product_type_container_loc)
        time.sleep(0.5)

    def test_abnormal_statistic_02_2(self):  # 户外柜
        self.click_element(AbnormalStatisticLocator.product_type_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.product_type_outdoor_loc)
        time.sleep(0.5)

    def test_abnormal_statistic_02_3(self):  # 非系统
        self.click_element(AbnormalStatisticLocator.product_type_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.product_type_non_system_loc)
        time.sleep(0.5)

    def test_abnormal_statistic_02_4(self):  # 清除
        self.move_to_element(AbnormalStatisticLocator.product_type_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.product_type_clear_loc)
        time.sleep(0.5)

    # 场景类型切换
    def test_abnormal_statistic_03_1(self):  # 部件
        self.click_element(AbnormalStatisticLocator.scene_type_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.scene_type_part_loc)
        time.sleep(0.5)

    def test_abnormal_statistic_03_2(self):  # 厂商
        self.click_element(AbnormalStatisticLocator.scene_type_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.scene_type_vendor_loc)
        time.sleep(0.5)

    def test_abnormal_statistic_03_3(self):  # 清除
        self.move_to_element(AbnormalStatisticLocator.scene_type_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.scene_type_clear_loc)
        time.sleep(0.5)

    # 时间维度切换
    def test_abnormal_statistic_04_1(self):  # 月
        self.click_element(AbnormalStatisticLocator.time_dimension_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.time_dimension_month_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.year_month_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.year_month_next_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.year_month_previous_loc)
        time.sleep(0.5)

    def test_abnormal_statistic_04_2(self):  # 年
        self.click_element(AbnormalStatisticLocator.time_dimension_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.time_dimension_year_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.year_month_select_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.year_month_next_loc)
        time.sleep(0.5)
        self.click_element(AbnormalStatisticLocator.year_month_previous_loc)
        time.sleep(0.5)

    # 获取异常统计按钮文本
    def get_abnormal_statistic_button_text(self):
        return self.text(AbnormalStatisticLocator.abnormal_statistic_loc)

    # 获取产品类型 未输入时的1提示文本
    def get_product_type_no_input_text(self):
        return self.text(AbnormalStatisticLocator.scene_type_select_unselected_loc)

    # 获取产品类型输入框文本
    def get_product_type_input_text(self):
        return self.text(AbnormalStatisticLocator.product_type_text_loc)
        # return self.get_attribute(AbnormalStatisticLocator.product_type_select_loc, 'value')

    # 获取场景类型输入框文本
    def get_scene_type_input_text(self):
        return self.text(AbnormalStatisticLocator.scene_type_text_loc)

    # 获取时间维度输入框文本
    def get_time_dimension_input_text(self):
        return self.text(AbnormalStatisticLocator.time_dimension_text_loc)
