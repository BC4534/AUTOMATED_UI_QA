import allure
from common.loggerhandler import logger
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage

@allure.feature("知识库")
@allure.story("知识库")
@allure.title("编辑知识")
class TestKnowledgeBase05():

    @allure.description("草稿状态,编辑后点取消")
    def test_knowledge_base_05(self,login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            title = knowledge_base_page.get_first_knowledge_name()
            knowledge_base_page.click_first_knowledge_edit_button()
            knowledge_base_page.edit_operation(new_knowledge_title="草稿知识编辑title",
                                               new_knowledge_content="草稿知识编辑内容")
            knowledge_base_page.click_back_button()
            assert knowledge_base_page.get_first_knowledge_name() == title
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("草稿状态,编辑后点取消")
    def test_knowledge_base_05(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            title = knowledge_base_page.get_first_knowledge_name()
            knowledge_base_page.click_first_knowledge_edit_button()
            knowledge_base_page.edit_operation(new_knowledge_title="草稿知识编辑title",
                                               new_knowledge_content="草稿知识编辑内容")
            knowledge_base_page.click_save_button()
            assert knowledge_base_page.get_first_knowledge_name() == "草稿知识编辑title"
            knowledge_base_page.click_first_knowledge_edit_button()
            knowledge_base_page.edit_operation(new_knowledge_title=title,
                                               new_knowledge_content="草稿知识编辑内容")
            knowledge_base_page.click_save_button()
            assert knowledge_base_page.get_first_knowledge_name() == title
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

