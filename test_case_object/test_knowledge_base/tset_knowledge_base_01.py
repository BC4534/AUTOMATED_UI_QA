from common.mylogger import Logger
from test_case_object.conftest import login_driver
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage

logger = Logger()


class TestKnowledgeBase01:
    '''
     切换至知识库界面
    '''

    def test_knowledge_base_01(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page = KnowledgeBasePage(login_driver)
            knowledge_base_page.switch_to_knowledge_base_page()
            assert knowledge_base_page.get_add_knowledge_button_text() == "新增知识"
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
