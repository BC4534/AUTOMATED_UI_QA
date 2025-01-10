from datetime import datetime

import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage


@allure.feature("工单管理")
@allure.story("工单列表")
@allure.title("工单列表-验证搜索功能")
class TestWorkOrderList07(object):

    @allure.story("发布时间搜索")
    def test_work_order_list_07_1(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.test_work_order_list_09_1()
            work_order_list_page.click_search_button()
            work_order_list_page.click_clear_time_button_loc()
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 验证处理状态
    @allure.description("验证处理状态搜索")
    def test_work_order_list_07_2(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            work_order_list_page.test_work_order_list_07_2_unifinished()
            work_order_list_page.click_search_button()
            assert work_order_list_page.get_first_data_handle_status_text() == "未完成"
            work_order_list_page.click_reset_button()
            work_order_list_page.test_work_order_list_07_2_finished()
            work_order_list_page.click_search_button()
            assert work_order_list_page.get_first_data_handle_status_text() == "已完成"
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 工单编号搜索
    @allure.description("验证工单编号搜索")
    def test_work_order_list_07_3(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            second_work_order_number = (
                work_order_list_page.get_second_work_order_number()
            )
            work_order_list_page.test_work_order_list_07_3(second_work_order_number)
            work_order_list_page.click_search_button()
            if second_work_order_number != 1:
                assert (
                    second_work_order_number
                    == work_order_list_page.get_first_work_order_number()
                )
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 工单名称搜索
    @allure.description("验证工单名称搜索")
    def test_work_order_list_07_4(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            second_work_order_name = work_order_list_page.get_second_work_order_name()
            work_order_list_page.test_work_order_list_07_4(second_work_order_name)
            work_order_list_page.click_search_button()
            if second_work_order_name != 1:
                assert (
                    second_work_order_name
                    in work_order_list_page.get_first_work_order_name()
                )
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 关联项目
    @allure.description("验证关联项目搜索")
    def test_work_order_list_07_5(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            association_project = (
                work_order_list_page.get_second_work_order_association_project()
            )
            if association_project != 1:
                _ = work_order_list_page.test_work_order_list_07_5(association_project)
                work_order_list_page.click_search_button()
                if _ != 1:
                    assert (
                        association_project
                        in work_order_list_page.get_first_data_association_project_text()
                    )
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("验证工单类型搜索")
    def test_work_order_list_07_6(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            work_order_list_page.test_work_order_list_07_6("定期标准巡检工单")
            work_order_list_page.click_search_button()
            t1 = work_order_list_page.get_first_data_work_order_type()
            if t1 != 1:
                assert t1 == "定期标准巡检工单"
            work_order_list_page.click_reset_button()
            work_order_list_page.test_work_order_list_07_6("系统异常工单")
            work_order_list_page.click_search_button()
            t2 = work_order_list_page.get_first_data_work_order_type()
            if t2 != 1:
                assert t2 == "系统异常工单"
            work_order_list_page.click_reset_button()
            work_order_list_page.test_work_order_list_07_6("手工其他工单")
            work_order_list_page.click_search_button()
            t3 = work_order_list_page.get_first_data_work_order_type()
            if t3 != 1:
                assert t3 == "手工其他工单"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 计划开始时间
    @allure.description("验证计划开始时间搜索")
    def test_work_order_list_07_7(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.refresh()
            work_order_list_page.click_reset_button()
            time = work_order_list_page.get_second_data_plan_start_time()
            if time != 1:
                work_order_list_page.test_work_order_list_07_7(time)
                work_order_list_page.click_search_button()
                assert (
                    time[0:11]
                    == work_order_list_page.get_first_data_plan_start_time()[0:11]
                )
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("验证计划结束时间搜索")
    def test_work_order_list_07_8(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.refresh()
            work_order_list_page.click_reset_button()
            time = work_order_list_page.get_second_data_plan_end_time()
            if time != 1:
                work_order_list_page.test_work_order_list_07_8(time)
                work_order_list_page.click_search_button()
                assert (
                    time[0:11]
                    == work_order_list_page.get_first_data_plan_end_time()[0:11]
                )
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            # 外层的异常处理，记录错误信息并截图
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            # 可以选择是否向外抛出异常
            raise e

    @allure.description("验证工单所属区域搜索")
    def test_work_order_list_07_9(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            work_order_list_page.test_work_order_list_07_9("东部")
            work_order_list_page.click_search_button()
            _ = work_order_list_page.get_first_work_order_area()
            if _ != 1:
                assert work_order_list_page.get_first_work_order_area() == "东部"
            work_order_list_page.click_reset_button()
            _ = work_order_list_page.test_work_order_list_07_9("大储运维（宁夏）")
            work_order_list_page.click_search_button()

            if _ != 1:
                assert (
                    work_order_list_page.get_first_work_order_area()
                    == "大储运维（宁夏）"
                )
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 工单发起人
    @allure.description("验证工单发起人搜索")
    def test_work_order_list_07_10(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            work_order_list_page.input_work_order_initiator("")
            work_order_list_page.click_search_button()
            initiator = work_order_list_page.get_first_work_order_initiator()
            if initiator != 1:
                assert initiator == "系统管理员"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 工单接受人
    @allure.description("验证工单接收人搜索")
    def test_work_order_list_07_11(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            work_order_list_page.input_work_order_receiver("")
            work_order_list_page.click_search_button()
            receiver = work_order_list_page.get_first_work_order_receiver()
            if receiver != 1:
                assert receiver == "系统管理员"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 当前处理人
    @allure.description("验证当前处理人搜索")
    def test_work_order_list_07_12(self, login_driver):
        work_order_list_page = WorkOrderListPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.click_reset_button()
            work_order_list_page.input_work_order_current_handler("")
            work_order_list_page.click_search_button()
            current_handler = (
                work_order_list_page.get_first_work_order_current_handler()
            )
            if current_handler != 1:
                assert current_handler == "系统管理员"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
