import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.work_order_management.abnormal_review.abnormal_details_locator import (
    AbnormalDetailsLocator,
)
from test_case_locator.work_order_management.abnormal_review.abnormal_statistic_locator import (
    AbnormalStatisticLocator,
)


class AbnormalDetailsPage(BasePage):
    """异常详情界面"""

    """异常统计页面"""

    # 判断工单管理是否展开
    def _get_work_order_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            AbnormalStatisticLocator.work_order_management_expand_loc, "class"
        )

    # 切换至 异常明细界面
    def switch_to_abnormal_details_page(self):
        if self._get_work_order_management_is_expand():
            self.click_element(AbnormalStatisticLocator.work_order_management_loc)
        self.click_element(AbnormalStatisticLocator.abnormal_review_loc)
        if not self._get_abnormal_details_is_active():
            self.click_element(AbnormalDetailsLocator.abnormal_detail_loc)

    # 获取异常明细界面标题
    def get_abnormal_details_title(self):
        return self.text(AbnormalDetailsLocator.abnormal_detail_loc)

    # 判断是否在异常明细界面 class="ant-tabs-tab ant-tabs-tab-active"
    @allure.step("判断是否在异常明细界面")
    def _get_abnormal_details_is_active(self):
        return (
            self.get_attribute(
                AbnormalDetailsLocator.abnormal_detail_class_loc, "class"
            )
            == "ant-tabs-tab ant-tabs-tab-active"
        )

    @allure.step("判断异常明细界面的异常统计部分是否展开")
    def _get_abnormal_statistic_is_expand(self):
        try:
            if self.visibility_of_element_located(
                AbnormalDetailsLocator.abnormal_statistic_expand_button_judge_loc
            ):
                return True
        except Exception as e:
            return False

    @allure.step("点击异常统计部分展开关闭按钮")
    def click_abnormal_statistic_expand_button(self):
        self.click_element(AbnormalDetailsLocator.abnormal_statistic_expand_button_loc)

    @allure.step("关闭异常统计部分")
    def close_abnormal_statistic(self):
        if self._get_abnormal_statistic_is_expand():
            self.click_abnormal_statistic_expand_button()

    @allure.step("点击第一个工单附件按钮.如有")
    def click_first_work_order_attachment_button(self):
        try:
            self.click_element(
                AbnormalDetailsLocator.first_work_order_attachment_button_loc
            )
        except Exception as e:
            logger.warning("没有找到第一个工单附件按钮", e)

    # 点击附件弹窗的关闭按钮
    @allure.step("点击附件弹窗的关闭按钮")
    def click_attachment_dialog_close_button(self):
        self.click_element(AbnormalDetailsLocator.attachment_dialog_close_button_loc)

    @allure.step("点击附件弹窗的取消按钮")
    def click_attachment_dialog_cancel_button(self):
        self.click_element(AbnormalDetailsLocator.attachment_dialog_cancel_button_loc)

    @allure.step("点击附件弹窗的确认按钮")
    def click_attachment_dialog_confirm_button(self):
        self.click_element(AbnormalDetailsLocator.attachment_dialog_confirm_button_loc)

    @allure.step("判断是否有附件弹窗")
    def _get_attachment_dialog_is_displayed(self):
        try:
            self.visibility_of_element_located(
                AbnormalDetailsLocator.attachment_dialog_title_loc
            )
            return True
        except Exception as e:
            return False

    @allure.step("点击第一个工单的详情按钮,如有")
    def click_first_work_order_detail_button(self):
        try:
            self.click_element(
                AbnormalDetailsLocator.first_work_order_details_button_loc
            )
            return self.text(AbnormalDetailsLocator.first_work_order_number_loc)
        except Exception as e:
            logger.warning("没有找到第一个工单详情按钮", e)

    # 查询相关
    @allure.step("点击重置按钮")
    def click_reset_button(self):
        self.click_element(AbnormalDetailsLocator.reset_button_loc)
        time.sleep(0.5)

    @allure.step("点击搜索按钮")
    def click_search_button(self):
        self.click_element(AbnormalDetailsLocator.search_button_loc)
        time.sleep(0.5)

    @allure.step("输入工单编号")
    def input_work_order_number(self, work_order_number):
        self.send_keys_by_clear_and_typing(
            AbnormalDetailsLocator.work_order_number_input_loc, work_order_number
        )

    @allure.step("获取第一个工单编号")
    def get_first_work_order_number(self):
        try:
            return self.text(AbnormalDetailsLocator.first_work_order_number_loc)
        except Exception as e:
            logger.warning("没有找到第一个工单编号", e)
            return 1

    @allure.step("获取第二个工单编号")
    def get_second_work_order_number(self):
        try:
            return self.text(AbnormalDetailsLocator.second_work_order_number_loc)
        except Exception as e:
            logger.warning("没有找到第二个工单编号", e)
            return 1

    @allure.step("输入异常名称")
    def input_abnormal_name(self, abnormal_name):
        self.send_keys_by_clear_and_typing(
            AbnormalDetailsLocator.abnormal_name_input_loc, abnormal_name
        )

    @allure.step("获取第一个工单的异常名称")
    def get_first_work_order_abnormal_name(self):
        try:
            return self.text(AbnormalDetailsLocator.first_work_order_abnormal_name_loc)
        except Exception as e:
            logger.warning("没有找到第一个工单的异常名称", e)
            return 1

    @allure.step("获取第二个工单的异常名称")
    def get_second_work_order_abnormal_name(self):
        try:
            return self.text(AbnormalDetailsLocator.second_work_order_abnormal_name_loc)
        except Exception as e:
            logger.warning("没有找到第二个工单的异常名称", e)
            return 1

    @allure.step("选择关联项目名称")
    def select_relation_project(self, relation_project):
        self.click_element(AbnormalDetailsLocator.relation_project_select_loc)
        # //*[@title="测试/1112"]
        self.click_element((By.XPATH, f'//*[@title="{relation_project}"]'))

    @allure.step("获取第一个工单的关联项目名称")
    def get_first_work_order_relation_project(self):
        try:
            return self.text(
                AbnormalDetailsLocator.first_work_order_relation_project_loc
            )
        except Exception as e:
            logger.warning("没有找到第一个工单的关联项目名称", e)
            return 1

    @allure.step("获取第二个工单的关联项目名称")
    def get_second_work_order_relation_project(self):
        try:
            return self.text(
                AbnormalDetailsLocator.second_work_order_relation_project_loc
            )
        except Exception as e:
            logger.warning("没有找到第二个工单的关联项目名称", e)
            return 1

    @allure.step("选择关联工单类型")
    def select_relation_work_order_type(self, relation_work_order_type):
        self.click_element(AbnormalDetailsLocator.relation_work_order_type_select_loc)
        self.click_element((By.XPATH, f'//*[@title="{relation_work_order_type}"]'))

    @allure.step("获取第一个工单的关联工单类型")
    def get_first_work_order_relation_work_order_type(self):
        try:
            self.click_element(
                AbnormalDetailsLocator.first_work_order_details_button_loc
            )
            return self.text(
                AbnormalDetailsLocator.first_work_order_relation_work_order_type_loc
            )
        except Exception as e:
            logger.warning(f"没有找到第一个工单的关联工单类型,错误信息:{e}")
            return 1

    @allure.step("选择异常部件")
    def select_abnormal_part(self, abnormal_part):
        self.click_element(AbnormalDetailsLocator.abnormal_part_select_loc)
        self.click_element((By.XPATH, f'//*[@title="{abnormal_part}"]'))

    @allure.step("获取第一个工单的异常部件")
    def get_first_work_order_abnormal_part(self):
        try:
            return self.text(AbnormalDetailsLocator.first_work_order_abnormal_part_loc)
        except Exception as e:
            logger.warning(f"没有找到第一个工单的异常部件,错误信息:{e}")
            return 1

    @allure.step("获取第二个工单的异常部件")
    def get_second_work_order_abnormal_part(self):
        try:
            return self.text(AbnormalDetailsLocator.second_work_order_abnormal_part_loc)
        except Exception as e:
            logger.warning(f"没有找到第二个工单的异常部件,错误信息:{e}")
            return 1

    @allure.step("选择责任厂商")
    def select_responsible_vendor(self, responsible_vendor):
        self.click_element(AbnormalDetailsLocator.responsible_vendor_select_loc)
        self.click_element((By.XPATH, f'//*[@title="{responsible_vendor}"]'))

    @allure.step("获取第一个工单的责任厂商")
    def get_first_work_order_responsible_vendor(self):
        try:
            return self.text(
                AbnormalDetailsLocator.first_work_order_responsible_vendor_loc
            )
        except Exception as e:
            logger.warning(f"没有找到第一个工单的责任厂商,错误信息:{e}")
            return 1

    @allure.step("获取第二个工单的责任厂商")
    def get_second_work_order_responsible_vendor(self):
        try:
            return self.text(
                AbnormalDetailsLocator.second_work_order_responsible_vendor_loc
            )
        except Exception as e:
            logger.warning(f"没有找到第二个工单的责任厂商,错误信息:{e}")
            return 1

    @allure.step("是否领用/采购备件或耗材查询")
    def select_is_purchase(self, is_purchase):
        self.click_element(AbnormalDetailsLocator.is_purchase_select_loc)
        self.click_element((By.XPATH, f'//*[@title="{is_purchase}"]'))

    @allure.step("获取第一个工单的领用/采购备件或耗材")
    def get_first_work_order_is_purchase(self):
        try:
            self.click_element(
                AbnormalDetailsLocator.first_work_order_details_button_loc
            )
            self.random_sleep(1)
            self.click_element(
                AbnormalDetailsLocator.work_order_list_details_button_loc
            )
            self.random_sleep(1)
            return self.text(AbnormalDetailsLocator.is_purchase_loc)
        except Exception as e:
            logger.warning(f"没有找到第一个工单的领用/采购备件或耗材,错误信息:{e}")
            return 1

    @allure.step("关闭详情页面")
    def close_details_page(self):
        self.click_element(AbnormalDetailsLocator.detail_close_button_loc)

    @allure.step("选择异常处理人")
    def select_abnormal_processing_person(self, abnormal_processing_person):
        self.click_element(AbnormalDetailsLocator.abnormal_processing_person_select_loc)
        self.click_element((By.XPATH, f'//*[@title="{abnormal_processing_person}"]'))

    @allure.step("获取第一个工单的异常处理人")
    def get_first_work_order_abnormal_processing_person(self):
        try:
            return self.text(
                AbnormalDetailsLocator.first_work_order_abnormal_processing_person_loc
            )
        except Exception as e:
            logger.warning(f"没有找到第一个工单的异常处理人,错误信息:{e}")

    @allure.step("获取第二个工单的异常处理人")
    def get_second_work_order_abnormal_processing_person(self):
        try:
            return self.text(
                AbnormalDetailsLocator.second_work_order_abnormal_processing_person_loc
            )
        except Exception as e:

            logger.warning(f"没有找到第二个工单的异常处理人,错误信息:{e}")
