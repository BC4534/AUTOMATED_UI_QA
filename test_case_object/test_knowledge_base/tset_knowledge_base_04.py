import allure
from common.loggerhandler import logger
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage


@allure.feature("知识库")
@allure.story("知识库")
@allure.title("删除知识")
class TestKnowledgeBase04:

    @allure.description("详情界面")
    def test_knowledge_base_04(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_first_knowledge_detail_button()
            assert knowledge_base_page.get_detail_page_title() == "详情"
            knowledge_base_page.click_detail_page_back_button()
            knowledge_base_page.click_first_knowledge_detail_button()
            assert knowledge_base_page.get_detail_page_title() == "详情"
            knowledge_base_page.click_detail_page_close_button()
            knowledge_base_page.click_first_knowledge_detail_button()
            assert knowledge_base_page.get_detail_page_title() == "详情"
            knowledge_base_page.click_detail_page_confirm_button()
            assert knowledge_base_page.is_detail_page_closed()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
