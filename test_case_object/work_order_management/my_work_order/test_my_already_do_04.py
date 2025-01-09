import allure
from common.loggerhandler import logger
from test_case_page.work_order_management.my_work_order.my_already_do_page import MyAlreadyDoPage



@allure.feature("工单管理")
@allure.story("我的工单")
@allure.title("我的已办")
class TestMyAlreadyDo04:
    @allure.description("工单编号查询")
    def test_my_already_do_04_01(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            number = my_already_do_page.get_second_work_order_number()
            if number != 1:
                my_already_do_page.input_work_order_number(number)
                my_already_do_page.click_search_button()
                assert my_already_do_page.get_first_work_order_number() == number
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单发布时间查询")
    def test_my_already_do_04_02(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单名称查询")
    def test_my_already_do_04_03(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            name = my_already_do_page.get_second_work_order_name()
            if name != 1:
                my_already_do_page.input_work_order_name(name)
                my_already_do_page.click_search_button()
                assert my_already_do_page.get_first_work_order_name() == name
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单类型查询")
    def test_my_already_do_04_04(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            my_already_do_page.input_work_order_type("定期标准巡检工单")
            my_already_do_page.click_search_button()
            type1 = my_already_do_page.get_first_work_order_type()
            if type1 != 1:
                assert "定期标准巡检工单" == type1
            my_already_do_page.click_reset_button()
            my_already_do_page.input_work_order_type("实施工单")
            my_already_do_page.click_search_button()
            type2 = my_already_do_page.get_first_work_order_type()
            if type2 != 1:
                assert "实施工单" == type2
            my_already_do_page.click_reset_button()
            my_already_do_page.input_work_order_type("手工其他工单")
            my_already_do_page.click_search_button()
            type3 = my_already_do_page.get_first_work_order_type()
            if type3 != 1:
                assert "手工其他工单" == type3
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("关联项目查询")
    def test_my_already_do_04_05(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            project = my_already_do_page.get_second_association_project()
            my_already_do_page.input_association_project(project)
            my_already_do_page.click_search_button()
            if project != 1:
                assert my_already_do_page.get_first_association_project() == project
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("计划开始时间查询")
    def test_my_already_do_04_06(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.refresh()
            start_time = my_already_do_page.get_second_plan_start_date()
            if start_time != 1:
                my_already_do_page.input_plan_start_date(start_time)
                my_already_do_page.click_search_button()
                assert my_already_do_page.get_first_plan_end_date() >= start_time
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("计划结束时间查询")
    def test_my_already_do_04_07(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.refresh()
            end_time = my_already_do_page.get_second_plan_end_date()
            if end_time != 1:
                my_already_do_page.input_plan_end_date(end_time)
                my_already_do_page.click_search_button()
                assert my_already_do_page.get_first_plan_end_date() <= end_time
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单所属区域查询")
    def test_my_already_do_04_08(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            my_already_do_page.input_work_order_belong_area("东部")
            my_already_do_page.click_search_button()
            if my_already_do_page.get_first_work_order_belong_area() != 1:
                assert my_already_do_page.get_first_work_order_belong_area() == "东部"
            my_already_do_page.click_reset_button()
            my_already_do_page.input_work_order_belong_area("西北")
            my_already_do_page.click_search_button()
            if my_already_do_page.get_first_work_order_belong_area() != 1:
                assert my_already_do_page.get_first_work_order_belong_area() == "西北"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单发起人查询")
    def test_my_already_do_04_09(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            my_already_do_page.input_work_order_initiator("系统管理员")
            my_already_do_page.click_search_button()
            if my_already_do_page.get_first_work_order_initiator() != 1:
                assert my_already_do_page.get_first_work_order_initiator() == "系统管理员"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("工单接收人查询")
    def test_my_already_do_04_10(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            my_already_do_page.input_work_order_receiver("系统管理员")
            my_already_do_page.click_search_button()
            if my_already_do_page.get_first_work_order_initiator() != 1:
                assert my_already_do_page.get_first_work_order_receiver() == "系统管理员"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("当前处理人查询")
    def test_my_already_do_04_11(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            my_already_do_page.input_current_handler("系统管理员")
            my_already_do_page.click_search_button()
            if my_already_do_page.get_first_work_order_initiator() != 1:
                assert my_already_do_page.get_first_work_order_current_handler() == "系统管理员"
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("处理状态查询,我的已办里面处理状态全是已完成")
    def test_my_already_do_04_12(self, login_driver):
        my_already_do_page = MyAlreadyDoPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            my_already_do_page.switch_to_my_already_do_page()
            my_already_do_page.click_reset_button()
            logger.info(f"{self.__class__.__name__}用例执行通过")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}用例执行失败，错误信息为：{e}")
            my_already_do_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e



