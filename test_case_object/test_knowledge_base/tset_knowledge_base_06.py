import allure
from common.loggerhandler import logger
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage


@allure.feature("知识库")
@allure.story("知识库")
@allure.title("查询")
class TestKnowledgeBase06:

    @allure.description("发布时间查询")
    def test_knowledge_base_06_1(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("知识名称查询")
    def test_knowledge_base_06_2(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_reset_button()
            second_knowledge_name = knowledge_base_page.get_second_knowledge_name()
            knowledge_base_page.input_knowledge_name_query_condition(
                second_knowledge_name
            )
            knowledge_base_page.click_search_button()
            _ = knowledge_base_page.get_first_knowledge_name()
            if _ != 1:
                assert _ == second_knowledge_name
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("知识类型查询")
    def test_knowledge_base_06_3(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_knowledge_type_query_condition("规章制度")
            knowledge_base_page.click_search_button()
            type1 = knowledge_base_page.get_first_knowledge_type()
            if type1 != 1:
                assert type1 == "规章制度"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_knowledge_type_query_condition("行业标准")
            knowledge_base_page.click_search_button()
            type2 = knowledge_base_page.get_first_knowledge_type()
            if type2 != 1:
                assert type2 == "行业标准"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_knowledge_type_query_condition("问题总结")
            knowledge_base_page.click_search_button()
            type3 = knowledge_base_page.get_first_knowledge_type()
            if type3 != 1:
                assert type3 == "问题总结"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_knowledge_type_query_condition("项目资料")
            knowledge_base_page.click_search_button()
            type4 = knowledge_base_page.get_first_knowledge_type()
            if type4 != 1:
                assert type4 == "项目资料"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("关联项目查询")
    def test_knowledge_base_06_4(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_reset_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("撰写人查询")
    def test_knowledge_base_06_5(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_reset_button()
            first_writer = knowledge_base_page.get_first_writer()
            if first_writer != 1:
                knowledge_base_page.input_writer_query_condition(first_writer)
                knowledge_base_page.click_search_button()
                assert first_writer == knowledge_base_page.get_first_writer()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("关联设备类型查询")
    def test_knowledge_base_06_6(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_device_type_query_condition("215")
            knowledge_base_page.click_search_button()
            type1 = knowledge_base_page.get_first_device_type()
            if type1 != 1:
                assert type1 == "215"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_device_type_query_condition("232")
            knowledge_base_page.click_search_button()
            type2 = knowledge_base_page.get_first_device_type()
            if type2 != 1:
                assert type1 == "232"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_device_type_query_condition("372")
            knowledge_base_page.click_search_button()
            type3 = knowledge_base_page.get_first_device_type()
            if type3 != 1:
                assert type3 == "372"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.select_device_type_query_condition("集装箱")
            knowledge_base_page.click_search_button()
            type4 = knowledge_base_page.get_first_device_type()
            if type4 != 1:
                assert type4 == "集装箱"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("异常环节查询")
    def test_knowledge_base_06_7(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_reset_button()
            abnormal = knowledge_base_page.get_first_no_abnormal_link()
            if abnormal != 1:
                knowledge_base_page.select_abnormal_link_query_condition(abnormal)
                knowledge_base_page.click_search_button()
                assert knowledge_base_page.get_first_abnormal_link() == abnormal
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("知识状态查询")
    def test_knowledge_base_06_8(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_reset_button()
            knowledge_base_page.input_knowledge_status_query_condition("草稿")
            knowledge_base_page.click_search_button()
            status1 = knowledge_base_page.get_first_knowledge_status()
            if status1 != 1:
                assert status1 == "草稿"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.input_knowledge_status_query_condition("待修改")
            knowledge_base_page.click_search_button()
            status2 = knowledge_base_page.get_first_knowledge_status()
            if status2 != 1:
                assert status2 == "待修改"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.input_knowledge_status_query_condition("审核中")
            knowledge_base_page.click_search_button()
            status3 = knowledge_base_page.get_first_knowledge_status()
            if status3 != 1:
                assert status3 == "审核中"
            knowledge_base_page.click_reset_button()
            knowledge_base_page.input_knowledge_status_query_condition("审核成功")
            knowledge_base_page.click_search_button()
            status4 = knowledge_base_page.get_first_knowledge_status()
            if status4 != 1:
                assert status4 == "审核成功"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
