import allure
import pytest
from common.loggerhandler import logger
from test_case_page.work_order_management.abnormal_review.abnormal_details_page import (
    AbnormalDetailsPage,
)
from test_case_page.work_order_management.abnormal_review.abnormal_statistic_page import (
    AbnormalStatisticPage,
)
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage


@allure.feature("工单管理")
@allure.story("异常复盘")
@allure.title("异常明细-查询")
class TestAbnormalReview09:
    """
    异常开始时间 和异常完结时间未写
    """

    @allure.description("工单编号查询")
    def test_abnormal_review_09_01(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            second_work_order_number = (
                abnormal_details_page.get_second_work_order_number()
            )
            abnormal_details_page.input_work_order_number(second_work_order_number)
            abnormal_details_page.click_search_button()
            if second_work_order_number != 1:
                assert (
                    abnormal_details_page.get_first_work_order_number()
                    == second_work_order_number
                )
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单名称查询")
    def test_abnormal_review_09_02(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            abnormal_name = abnormal_details_page.get_second_work_order_abnormal_name()
            abnormal_details_page.input_abnormal_name(abnormal_name)
            abnormal_details_page.click_search_button()
            if abnormal_name != 1:
                assert (
                    abnormal_name
                    in abnormal_details_page.get_first_work_order_abnormal_name()
                )
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("关联项目名称查询")  # 当项目过多时, 需要优化
    def test_abnormal_review_09_03(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            project = abnormal_details_page.get_second_work_order_relation_project()
            abnormal_details_page.select_relation_project(project)
            abnormal_details_page.click_search_button()
            if project != 1:
                assert (
                    project
                    in abnormal_details_page.get_first_work_order_relation_project()
                )
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("关联工单类型查询")  # 当项目过多时, 需要优化
    def test_abnormal_review_09_04(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            abnormal_details_page.select_relation_work_order_type("手工异常工单")
            abnormal_details_page.click_search_button()
            type1 = (
                abnormal_details_page.get_first_work_order_relation_work_order_type()
            )
            if type1 != 1:
                assert type1 == "手工异常工单"
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            abnormal_details_page.select_relation_work_order_type("系统异常工单")
            abnormal_details_page.click_search_button()
            type2 = (
                abnormal_details_page.get_first_work_order_relation_work_order_type()
            )
            if type2 != 1:
                assert type2 == "系统异常工单"
            abnormal_details_page.switch_to_abnormal_details_page()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("异常部件查询")  #  需要优化
    def test_abnormal_review_09_05(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            abnormal_part = abnormal_details_page.get_second_work_order_abnormal_part()
            abnormal_details_page.select_abnormal_part(abnormal_part)
            abnormal_details_page.click_search_button()
            if abnormal_part != 1:
                assert (
                    abnormal_part
                    == abnormal_details_page.get_first_work_order_abnormal_part()
                )
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("责任厂商查询")  # 需要优化
    def test_abnormal_review_09_06(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            vendor = abnormal_details_page.get_second_work_order_responsible_vendor()
            abnormal_details_page.select_responsible_vendor(vendor)
            abnormal_details_page.click_search_button()
            if vendor != 1:
                assert (
                    vendor
                    == abnormal_details_page.get_first_work_order_responsible_vendor()
                )
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("是否领用/采购备件或耗材查询")  # 需要优化
    def test_abnormal_review_09_07(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            abnormal_details_page.select_is_purchase("是")
            abnormal_details_page.click_search_button()
            _ = abnormal_details_page.get_first_work_order_is_purchase()
            if _ != 1:
                assert _ == "是"
            abnormal_details_page.close_details_page()
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            abnormal_details_page.select_is_purchase("否")
            abnormal_details_page.click_search_button()
            _ = abnormal_details_page.get_first_work_order_is_purchase()
            if _ != 1:
                assert _ == "否"
            logger.info(f"{self.__class__.__name__}执行用例成功")

        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("异常处理人查询")  # 需要优化
    def test_abnormal_review_09_07(self, login_driver):
        abnormal_details_page = AbnormalDetailsPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            abnormal_details_page.switch_to_abnormal_details_page()
            abnormal_details_page.click_reset_button()
            person = (
                abnormal_details_page.get_second_work_order_abnormal_processing_person()
            )
            abnormal_details_page.select_abnormal_processing_person(person)
            abnormal_details_page.click_search_button()
            if person != 1:
                assert (
                    person
                    == abnormal_details_page.get_first_work_order_abnormal_processing_person()
                )
            logger.info(f"{self.__class__.__name__}执行用例成功")

        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            abnormal_details_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
