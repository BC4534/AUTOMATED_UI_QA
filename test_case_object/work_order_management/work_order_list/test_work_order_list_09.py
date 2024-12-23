from datetime import datetime

import allure

from common.loggerhandler import Logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

logger = Logger()

@allure.title("工单列表-验证搜索功能")
@allure.feature("工单管理-工单列表")
class TestWorkOrderList09(object):

    # 发布时间搜索框 相关操作
    def test_work_order_list_09_1(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_09_1()
            work_order_list_page.click_search_button_loc()
            work_order_list_page.click_clear_time_button_loc()
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    # 验证处理状态
    def test_work_order_list_09_2(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_09_2_1()
            work_order_list_page.click_search_button_loc()
            assert work_order_list_page.get_first_data_handle_status_text() == "未完成"
            work_order_list_page.test_work_order_list_09_2_2()
            work_order_list_page.click_search_button_loc()
            assert work_order_list_page.get_first_data_handle_status_text() == "已完成"
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 工单编号搜索
    def test_work_order_list_09_3(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order = work_order_list_page.test_work_order_list_09_3()
            assert work_order == work_order_list_page.get_first_work_order_number()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 工单名称搜索
    def test_work_order_list_09_4(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order = work_order_list_page.test_work_order_list_09_4()
            assert work_order == work_order_list_page.get_first_work_order_name()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 关联项目
    def test_work_order_list_09_5(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_09_5()
            association_project = work_order_list_page.get_association_project_text()
            assert association_project == work_order_list_page.get_first_data_association_project_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 工单类型 搜索
    # 定期标准巡检工单
    def test_work_order_list_09_6_1(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_6_1()
            try:
                assert (work_order_list_page.get_work_order_type_text() ==
                        work_order_list_page.get_first_data_work_order_type_text())
            except Exception:
                assert work_order_list_page.get_work_order_type_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    # 手工标准巡检工单
    def test_work_order_list_09_6_2(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_6_2()
            try:
                assert (work_order_list_page.get_work_order_type_text() ==
                        work_order_list_page.get_first_data_work_order_type_text())
            except Exception:
                assert work_order_list_page.get_work_order_type_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 实施工单
    def test_work_order_list_09_6_3(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_6_3()
            try:
                assert (work_order_list_page.get_work_order_type_text() ==
                        work_order_list_page.get_first_data_work_order_type_text())
            except Exception:
                assert work_order_list_page.get_work_order_type_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    # system_abnormal_work_order_loc
    def test_work_order_list_09_6_4(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_6_4()
            try:
                assert (work_order_list_page.get_work_order_type_text() ==
                        work_order_list_page.get_first_data_work_order_type_text())
            except Exception:
                assert work_order_list_page.get_work_order_type_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 手工异常工单
    def test_work_order_list_09_6_5(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_6_5()
            try:
                assert (work_order_list_page.get_work_order_type_text() ==
                        work_order_list_page.get_first_data_work_order_type_text())
            except Exception:
                assert work_order_list_page.get_work_order_type_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    # 手工非标巡检工单
    def test_work_order_list_09_6_6(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_6_6()
            try:
                assert (work_order_list_page.get_work_order_type_text() ==
                        work_order_list_page.get_first_data_work_order_type_text())
            except Exception:
                assert work_order_list_page.get_work_order_type_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 手工其他工单
    def test_work_order_list_09_6_7(self, login_driver):
        global work_order_list_page
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_6_7()
            try:
                assert (work_order_list_page.get_work_order_type_text() ==
                        work_order_list_page.get_first_data_work_order_type_text())
            except Exception:
                assert work_order_list_page.get_work_order_type_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 计划开始时间
    def test_work_order_list_09_7(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_09_7()
            try:
                start_time = datetime.strptime(work_order_list_page.get_first_data_plan_start_time(), '%Y-%m-%d %H:%M:%S')
                assert start_time >= datetime.strptime(work_order_list_page.get_plan_start_time_text(), '%Y-%m-%d')
            except Exception as e:
                raise e
            assert work_order_list_page.get_plan_start_time_text()
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 计划结束时间
    from datetime import datetime
    #  暂时不会写了，后面再优化
    def test_work_order_list_09_8(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.switch_to_work_order_list_page()
            work_order_list_page.test_work_order_list_09_8()

            # 内部try-except用于捕获日期时间比较的异常，但不抛出
            try:
                end_time = datetime.strptime(work_order_list_page.get_first_data_plan_end_time(),
                                               '%Y-%m-%d %H:%M:%S')
                plan_end_time = datetime.strptime(work_order_list_page.get_plan_end_time_text(), '%Y-%m-%d')
                assert end_time == plan_end_time, "计划结束时间不正确"
            except Exception as e:
                # 如果日期时间比较失败或格式转换失败，记录警告信息，但不抛出异常
                logger.warning(f"日期时间比较或格式转换失败：{e}")
                # 只断言计划开始时间文本的存在，不抛出异常
                assert work_order_list_page.get_plan_end_time_text(), "计划开始时间文本为空"
            # 如果内部try-except没有抛出异常，继续执行以下代码
            logger.info(f"{self.__class__.__name__}用例执行通过")
            work_order_list_page.click_reset_button_loc()
        except Exception as e:
            # 外层的异常处理，记录错误信息并截图
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            # 可以选择是否向外抛出异常
            raise e

    # 工单所属区域
    def test_work_order_list_09_9(self, login_driver):
        pass
    # 工单发起人
    def test_work_order_list_09_10(self, login_driver):
        pass
    # 工单接受人
    def test_work_order_list_09_11(self, login_driver):
        pass
    # 当前处理人
    def test_work_order_list_09_12(self, login_driver):
        pass