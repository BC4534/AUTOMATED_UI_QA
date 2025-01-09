import allure
from common.loggerhandler import logger
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage

@allure.feature("知识库")
@allure.story("知识库")
@allure.title("删除知识")
class TestKnowledgeBase03():

    @allure.description("单条删除-取消")
    def test_knowledge_base_99_01(self,login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            first_knowledge_name = knowledge_base_page.get_first_knowledge_name()
            knowledge_base_page.check_first_knowledge_checkbox()
            knowledge_base_page.click_delete_knowledge_button()
            knowledge_base_page.click_cancel_delete_button()
            assert knowledge_base_page.get_first_knowledge_name() == first_knowledge_name
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("单条删除-确认")
    def test_knowledge_base_99_02(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            second_knowledge_name = knowledge_base_page.get_second_knowledge_name()
            knowledge_base_page.check_first_knowledge_checkbox()
            knowledge_base_page.click_delete_knowledge_button()
            knowledge_base_page.click_confirm_delete_button()
            assert knowledge_base_page.get_first_knowledge_name() == second_knowledge_name
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("多条同时删除")
    def test_knowledge_base_99_03(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            old_name = knowledge_base_page.get_first_knowledge_name()
            knowledge_base_page.check_three_knowledge_checkbox()
            knowledge_base_page.click_delete_knowledge_button()
            knowledge_base_page.click_confirm_delete_button()
            new_name = knowledge_base_page.get_first_knowledge_name()
            if old_name !=1 and new_name !=1:
                assert knowledge_base_page.get_first_knowledge_name() != old_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e


