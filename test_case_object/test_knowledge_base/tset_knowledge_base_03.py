import allure

from common.loggerhandler import Logger
from test_case_object.conftest import login_driver
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage

logger = Logger()
data = {
    "title": "问题总结title",
    "content": "问题总结知识"
}
data2 = {
    "title": "规章制度title",
    "content": "规章制度知识"
}
data3 = {
    "title": "行业标准title",
    "content": "新增行业标准内容"
}
data4 = {
    "title": "项目资料title",
    "content": "项目资料内容"
}
@allure.title("新增知识")
@allure.feature("知识库")
class TestKnowledgeBase03():
    '''
     新增知识.必填项效验
    '''
    # 新增问题总结类知识
    def test_knowledge_base_03(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page = KnowledgeBasePage(login_driver)
            knowledge_base_page.test_knowledge_base_03_1()
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    # 规章制度类知识
    def test_knowledge_base_03_2(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page = KnowledgeBasePage(login_driver)
            knowledge_base_page.test_knowledge_base_03_2()
            # assert knowledge_base_page.get_add_knowledge_button_text() == "新增知识"
        except Exception as e:
            logger.error(e)
    # 行业标准   pass
    def test_knowledge_base_02_3(self,login_driver):
        pass

    # 项目资料
    def test_knowledge_base_02_4(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page = KnowledgeBasePage(login_driver)
            knowledge_base_page.test_knowledge_base_02_4(data4["title"], data["content"])
            knowledge_base_page.click_save_button()
        except Exception as e:
            logger.error(e)
            logger.error(f"{self.__class__.__name__}执行用例失败")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e