import allure

from common.loggerhandler import Logger
from test_case_page.work_order_management.work_order_list_page import WorkOrderListPage

logger = Logger()

@allure.title("工单列表-新增必填项效验")
@allure.feature("工单管理-工单列表")
class TestWorkOrderList03(object):
    """
    新增必填项 效验
    """

    def test_work_order_list_03(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            work_order_list_page = WorkOrderListPage(login_driver)
            work_order_list_page.test_work_order_list_03()
            assert work_order_list_page.get_work_order_type_required_text() == "请选择工单类型"
            assert work_order_list_page.get_work_order_name_required_text() == "请输入工单名称"
            assert work_order_list_page.get_work_order_description_required_text() == "请输入工单描述"
            assert work_order_list_page.get_association_project_required_text() == "请选择关联项目"
            assert work_order_list_page.get_responsible_person_required_text() == "请选择负责人"
            assert work_order_list_page.get_plan_start_time_required_text() == "请选择计划开始时间"
            assert work_order_list_page.get_plan_end_time_required_text() == "请选择计划结束时间"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            work_order_list_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

