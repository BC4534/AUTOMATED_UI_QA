import allure
import pytest

from common.loggerhandler import logger
from test_case_object.conftest import login_driver
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage


problem_summary_data = {
    "knowledge_type" :"问题总结",
    "knowledge_title" : "UI测试问题总结类知识标题",
    "associated_project": "填写具体的关联项目",
    "associated_device_type": "集装箱",
    "abnormal": "EMS系统",
    "knowledge_content" : "UI测试问题总结类知识内容\n下一行内容"
}
rule_regulation_data = {
    "knowledge_type" :"规章制度",
    "knowledge_title" : "UI测试规章制度类知识标题",
    "knowledge_content" : "UI测试规章制度类知识内容\n下一行内容",
    "associated_project": "数据格式要求",
    "associated_device_type": "数据格式要求",
    "abnormal": "数据格式要求",
}
industry_standard_data = {
    "knowledge_type" :"行业标准",
    "knowledge_title" : "UI测试行业标准类知识标题",
    "knowledge_content" : "UI测试行业标准类知识内容\n下一行内容",
    "associated_project": "数据格式要求",
    "associated_device_type": "数据格式要求",
    "abnormal": "数据格式要求",
}
project_info_data = {
    "knowledge_type" :"项目资料",
    "knowledge_title" : "UI测试项目资料类知识标题",
    "knowledge_content" : "UI测试项目资料类知识内容\n下一行内容",
    "associated_project": "输入关联项目名称",
    "associated_device_type": "数据格式要求",
    "abnormal": "数据格式要求",
}

@allure.feature("知识库")
@allure.story("知识库")
@allure.title("新增知识")
class TestKnowledgeBase02():

    @allure.title("新增知识必填项验证")
    def test_knowledge_base_02_1(self,login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_add_knowledge_button()
            knowledge_base_page.click_submit_button()
            assert knowledge_base_page.get_title_required_text() == "请输入必填字段"
            knowledge_base_page.click_back_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,失败信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.title("新增知识 取消")
    def test_knowledge_base_02_2(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            knowledge_base_page.switch_to_knowledge_base_page()
            name = knowledge_base_page.get_first_knowledge_name()
            knowledge_base_page.click_add_knowledge_button()
            knowledge_base_page.fill_add_knowledge_data(
                knowledge_type=problem_summary_data["knowledge_type"],
                knowledge_title=problem_summary_data["knowledge_title"],
                associated_project=problem_summary_data["associated_project"],
                associated_device_type=problem_summary_data["associated_device_type"],
                abnormal=problem_summary_data["abnormal"],
                knowledge_content=problem_summary_data["knowledge_content"]
            )
            knowledge_base_page.click_back_button()
            assert knowledge_base_page.get_first_knowledge_name() == name
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,失败信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.title("新增知识-确定")
    @pytest.mark.parametrize("data", [problem_summary_data,rule_regulation_data,industry_standard_data,project_info_data])
    # @pytest.mark.parametrize("data", [problem_summary_data])
    def test_knowledge_base_02_3(self,login_driver,data):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_add_knowledge_button()
            knowledge_base_page.fill_add_knowledge_data(
                knowledge_type=data["knowledge_type"],
                knowledge_title=data["knowledge_title"],
                associated_project=data["associated_project"],
                associated_device_type=data["associated_device_type"],
                abnormal=data["abnormal"],
                knowledge_content=data["knowledge_content"]
            )
            knowledge_base_page.click_save_button()
            assert knowledge_base_page.get_first_knowledge_name() == data["knowledge_title"]
            assert knowledge_base_page.get_first_knowledge_status() == "草稿"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,失败信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e