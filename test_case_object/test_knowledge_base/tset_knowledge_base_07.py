import allure
from common.loggerhandler import logger
from test_case_page.knowledge_base.knowledge_base_page import KnowledgeBasePage

problem_summary_data = {
    "knowledge_type": "问题总结",
    "knowledge_title": "UI测试新增提交问题总结知识标题",
    "associated_project": "填写具体的关联项目",
    "associated_device_type": "集装箱",
    "abnormal": "EMS系统",
    "knowledge_content": "UI测试问题总结类知识内容\n下一行内容",
}
rule_regulation_data = {
    "knowledge_type": "规章制度",
    "knowledge_title": "UI测试新增保存再提交规章制度知识标题",
    "knowledge_content": "UI测试规章制度类知识内容\n下一行内容",
    "associated_project": "数据格式要求",
    "associated_device_type": "数据格式要求",
    "abnormal": "数据格式要求",
}
industry_standard_data = {
    "knowledge_type": "行业标准",
    "knowledge_title": "UI测试行业标准类知识标题",
    "knowledge_content": "UI测试行业标准类知识内容\n下一行内容",
    "associated_project": "数据格式要求",
    "associated_device_type": "数据格式要求",
    "abnormal": "数据格式要求",
}
project_info_data = {
    "knowledge_type": "项目资料",
    "knowledge_title": "UI测试项目资料类知识标题",
    "knowledge_content": "UI测试项目资料类知识内容\n下一行内容",
    "associated_project": "输入关联项目名称",
    "associated_device_type": "数据格式要求",
    "abnormal": "数据格式要求",
}


@allure.feature("知识库")
@allure.story("知识库")
@allure.title("提交知识")
class TestKnowledgeBase07:

    @allure.description("新增提交")
    def test_knowledge_base_07_1(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_add_knowledge_button()
            knowledge_base_page.fill_add_knowledge_data(
                knowledge_type=problem_summary_data["knowledge_type"],
                knowledge_title=problem_summary_data["knowledge_title"],
                associated_project=problem_summary_data["associated_project"],
                associated_device_type=problem_summary_data["associated_device_type"],
                abnormal=problem_summary_data["abnormal"],
                knowledge_content=problem_summary_data["knowledge_content"],
            )
            knowledge_base_page.click_submit_button()
            status = knowledge_base_page.get_knowledge_status_by_title(
                problem_summary_data["knowledge_title"]
            )
            if status != 1:
                assert status == "审核中"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("新增保存再提交")
    def test_knowledge_base_07_2(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_add_knowledge_button()
            knowledge_base_page.fill_add_knowledge_data(
                knowledge_type=rule_regulation_data["knowledge_type"],
                knowledge_title=rule_regulation_data["knowledge_title"],
                associated_project=rule_regulation_data["associated_project"],
                associated_device_type=rule_regulation_data["associated_device_type"],
                abnormal=rule_regulation_data["abnormal"],
                knowledge_content=rule_regulation_data["knowledge_content"],
            )
            knowledge_base_page.click_save_button()
            knowledge_base_page.click_edit_button_by_title(
                rule_regulation_data["knowledge_title"]
            )
            knowledge_base_page.click_submit_button()
            status = knowledge_base_page.get_knowledge_status_by_title(
                rule_regulation_data["knowledge_title"]
            )
            if status != 1:
                assert status == "审核中"
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("审核拒绝")
    def test_knowledge_base_07_3(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_audit_button_by_title(
                rule_regulation_data["knowledge_title"]
            )
            knowledge_base_page.click_back_button()
            knowledge_base_page.click_audit_button_by_title(
                rule_regulation_data["knowledge_title"]
            )
            knowledge_base_page.click_audit_page_audit_button()
            knowledge_base_page.audit_operation("审核拒绝", "拒绝原因")
            knowledge_base_page.click_confirm_delete_button()
            assert (
                knowledge_base_page.get_knowledge_status_by_title(
                    rule_regulation_data["knowledge_title"]
                )
                == "待修改"
            )
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("审核成功")
    def test_knowledge_base_07_4(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_audit_button_by_title(
                problem_summary_data["knowledge_title"]
            )
            knowledge_base_page.click_back_button()
            knowledge_base_page.click_audit_button_by_title(
                problem_summary_data["knowledge_title"]
            )
            knowledge_base_page.click_audit_page_audit_button()
            knowledge_base_page.audit_operation("审核通过", "通过原因")
            knowledge_base_page.click_confirm_delete_button()
            assert (
                knowledge_base_page.get_knowledge_status_by_title(
                    problem_summary_data["knowledge_title"]
                )
                == "审核成功"
            )
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("待修改 -- 审核中")
    def test_knowledge_base_07_5(self, login_driver):
        knowledge_base_page = KnowledgeBasePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            knowledge_base_page.switch_to_knowledge_base_page()
            knowledge_base_page.click_edit_button_by_title(
                rule_regulation_data["knowledge_title"]
            )
            knowledge_base_page.click_submit_button()
            assert (
                knowledge_base_page.get_knowledge_status_by_title(
                    rule_regulation_data["knowledge_title"]
                )
                == "审核中"
            )
        except Exception as e:
            logger.error(f"{self.__class__.__name__}执行用例失败,错误信息为:{e}")
            knowledge_base_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
