import time
import allure
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.knowledge_base.knowledge_base_locator import KnowledgeBaseLocator


class KnowledgeBasePage(BasePage):

    @allure.step("切换到知识库页面")
    def switch_to_knowledge_base_page(self):
        self.click_element(KnowledgeBaseLocator.knowledge_base_loc)

    @allure.step("点击新增知识按钮")
    def click_add_knowledge_button(self):
        self.click_element(KnowledgeBaseLocator.add_knowledge_button_loc)
        self.random_sleep(0.5)

    @allure.step("获取新增知识按钮文本")
    def get_add_knowledge_button_text(self):
        return self.text(KnowledgeBaseLocator.add_knowledge_button_loc)

    @allure.step("点击删除知识按钮")
    def click_delete_knowledge_button(self):
        self.click_element(KnowledgeBaseLocator.delete_knowledge_button_loc)

    @allure.step("点击取消删除按钮")
    def click_cancel_delete_button(self):
        self.click_element(KnowledgeBaseLocator.cancel_button_loc)

    @allure.step("点击确定删除按钮")
    def click_confirm_delete_button(self):
        self.click_element(KnowledgeBaseLocator.confirm_button_loc)

    @allure.step("点击审核按钮")
    def click_audit_button(self):
        self.click_element(KnowledgeBaseLocator.audit_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击详情按钮")
    def click_detail_button(self):
        self.click_element(KnowledgeBaseLocator.detail_button_loc)
        self.random_sleep(0.5)

    # ------新增知识页面操作----
    @allure.step("新增知识")
    def fill_add_knowledge_data(
        self,
        knowledge_type="",
        knowledge_title="",
        associated_project="",
        associated_device_type="",
        abnormal="",
        knowledge_content="",
    ):
        self.click_element(KnowledgeBaseLocator.knowledge_type_select_loc)
        if knowledge_type == "问题总结":
            self._fill_add_knowledge_data_type_problem_summary(
                knowledge_title,
                associated_project,
                associated_device_type,
                abnormal,
                knowledge_content,
            )
        elif knowledge_type == "规章制度":
            self._fill_add_knowledge_data_type_rule_regulation(
                knowledge_title, knowledge_content
            )
        elif knowledge_type == "行业标准":
            self._fill_add_knowledge_data_type_industry_standard(
                knowledge_title, knowledge_content
            )
        elif knowledge_type == "项目资料":
            self._fill_add_knowledge_data_type_project_info(
                knowledge_title, associated_project, knowledge_content
            )
        else:
            logger.warning("没有找到对应的知识类型")

    @allure.step("输入新增知识内容")
    def __fill_add_knowledge_content(self, knowledge_content):
        self.click_element(KnowledgeBaseLocator.content_input_loc)
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.content_input_loc, knowledge_content
        )

    # 填写新增知识数据 问题总结类
    def _fill_add_knowledge_data_type_problem_summary(
        self,
        knowledge_title,
        associated_project,
        associated_device_type,
        abnormal,
        knowledge_content,
    ):
        self.click_element(KnowledgeBaseLocator.problem_summary_option_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.title_input_loc, knowledge_title
        )
        self.random_sleep(0.5)
        self.click_element(KnowledgeBaseLocator.project_select_loc)
        self.random_sleep(0.5)
        try:
            self.click_element((By.XPATH, f"//*[@title='{associated_project}']"))
        except:
            logger.warning(f"没有找到项目{associated_project},选择默认第一个项目")
            self.click_element(KnowledgeBaseLocator.first_project_option_loc)
        self.random_sleep(0.5)
        self.click_element(KnowledgeBaseLocator.device_type_select_loc)
        try:
            self.click_element((By.XPATH, f"//*[@title='{associated_device_type}']"))
        except:
            logger.warning(
                f"没有找到设备类型{associated_device_type},选择默认第一个设备类型"
            )
            self.click_element(KnowledgeBaseLocator.device_215_option_loc)
        self.random_sleep(0.5)
        self.__click_knowledge_base_page__()
        self.click_element(KnowledgeBaseLocator.abnormal_select_loc)
        try:
            self.click_element((By.XPATH, f"//*[@title='{abnormal}']"))
        except:
            self.click_element(KnowledgeBaseLocator.abnormal_bms_option_loc)
            logger.warning(f"没有找到异常{abnormal},选择默认第一个异常")

        self.random_sleep(0.5)
        self.__click_knowledge_base_page__()
        self.__fill_add_knowledge_content(knowledge_content)

    # 填写新增知识数据 规章制度类
    def _fill_add_knowledge_data_type_rule_regulation(
        self, knowledge_title, knowledge_content
    ):
        self.click_element(KnowledgeBaseLocator.rule_regulation_option_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.title_input_loc, knowledge_title
        )
        self.random_sleep(0.5)
        self.__fill_add_knowledge_content(knowledge_content)

    # 填写新增知识数据 行业标准类
    def _fill_add_knowledge_data_type_industry_standard(
        self, knowledge_title, knowledge_content
    ):
        self.click_element(KnowledgeBaseLocator.industry_standard_option_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.title_input_loc, knowledge_title
        )
        self.random_sleep(0.5)
        self.__fill_add_knowledge_content(knowledge_content)

    # # 填写新增知识数据 项目资料类
    def _fill_add_knowledge_data_type_project_info(
        self, knowledge_title, associated_project, knowledge_content
    ):
        self.click_element(KnowledgeBaseLocator.project_info_option_loc)
        self.random_sleep(0.5)
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.title_input_loc, knowledge_title
        )
        self.random_sleep(0.5)
        self.click_element(KnowledgeBaseLocator.project_select_loc)
        self.random_sleep(0.5)
        try:
            self.click_element((By.XPATH, f"//*[@title='{associated_project}']"))
        except:
            logger.warning(f"没有找到项目{associated_project},选择默认第一个项目")
            self.click_element(KnowledgeBaseLocator.first_project_option_loc)
        self.random_sleep(0.5)
        self.__fill_add_knowledge_content(knowledge_content)

    @allure.step("点击提交按钮")
    def click_submit_button(self):
        self.click_element(KnowledgeBaseLocator.submit_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击保存按钮")
    def click_save_button(self):
        self.click_element(KnowledgeBaseLocator.save_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击返回按钮")
    def click_back_button(self):
        self.click_element(KnowledgeBaseLocator.back_button_loc)
        self.random_sleep(0.5)

    # 点击知识库界面
    def __click_knowledge_base_page__(self):
        self.click_element(KnowledgeBaseLocator.knowledge_base_page_loc)

    @allure.step("获取第一条知识名称")
    def get_first_knowledge_name(self):
        time.sleep(0.5)
        try:
            return self.text(KnowledgeBaseLocator.first_knowledge_name_loc)
        except:
            logger.warning("没有找到第一条知识名称")
            return 1

    @allure.step("获取第二条知识名称")
    def get_second_knowledge_name(self):
        try:
            return self.text(KnowledgeBaseLocator.second_knowledge_name_loc)
        except:
            logger.warning("没有找到第二条知识名称")
            return 1

    @allure.step("获取第一条知识状态")
    def get_first_knowledge_status(self):
        return self.text(KnowledgeBaseLocator.first_knowledge_status_loc)

    @allure.step("获取标题必填项提示信息")
    def get_title_required_text(self):
        return self.text(KnowledgeBaseLocator.title_required_text_loc)

    @allure.step("勾选第一条知识的复选框")
    def check_first_knowledge_checkbox(self):
        self.click_element(KnowledgeBaseLocator.first_knowledge_checkbox_loc)

    @allure.step("勾选前三条知识的复选框")
    def check_three_knowledge_checkbox(self):
        self.click_element(KnowledgeBaseLocator.first_knowledge_checkbox_loc)
        self.random_sleep(0.5)
        self.click_element(KnowledgeBaseLocator.second_knowledge_checkbox_loc)
        self.random_sleep(0.5)
        self.click_element(KnowledgeBaseLocator.third_knowledge_checkbox_loc)
        self.random_sleep(0.5)

    @allure.step("点击第一条知识的详情按钮")
    def click_first_knowledge_detail_button(self):
        self.click_element(KnowledgeBaseLocator.first_knowledge_detail_button_loc)
        self.random_sleep(0.5)

    @allure.step("获取详情界面title")
    def get_detail_page_title(self):
        return self.text(KnowledgeBaseLocator.detail_page_title_loc)

    @allure.step("点击详情界面返回按钮")
    def click_detail_page_back_button(self):
        self.click_element(KnowledgeBaseLocator.cancel_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击详情界面关闭按钮")
    def click_detail_page_close_button(self):
        self.click_element(KnowledgeBaseLocator.close_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击详情界面确定按钮")
    def click_detail_page_confirm_button(self):
        self.click_element(KnowledgeBaseLocator.confirm_button_loc)
        self.random_sleep(0.5)

    @allure.step("判断详情界面是否关闭")
    def is_detail_page_closed(self):
        try:
            self.visibility_of_element_located(KnowledgeBaseLocator.detail_page_loc)
            return False
        except:
            return True

    """
        查询相关
    """

    @allure.step("点击搜索按钮")
    def click_search_button(self):
        self.click_element(KnowledgeBaseLocator.search_button_loc)
        self.random_sleep(0.5)

    @allure.step("点击重置按钮")
    def click_reset_button(self):
        self.click_element(KnowledgeBaseLocator.reset_button_loc)
        self.random_sleep(0.5)

    @allure.step("获取第一条知识名称")
    def get_first_knowledge_name(self):
        time.sleep(0.5)
        try:
            return self.text(KnowledgeBaseLocator.first_knowledge_name_loc)
        except:
            logger.warning("没有找到第一条知识名称")
            return 1

    @allure.step("获取第二条知识名称")
    def get_second_knowledge_name(self):
        try:
            return self.text(KnowledgeBaseLocator.second_knowledge_name_loc)
        except:
            logger.warning("没有找到第二条知识名称")
            return 2

    @allure.step("输入知识名称查询条件")
    def input_knowledge_name_query_condition(self, knowledge_name):
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.knowledge_name_input_loc, knowledge_name
        )
        self.random_sleep(0.5)

    @allure.step("选择知识类型查询条件")
    def select_knowledge_type_query_condition(self, knowledge_type):
        self.click_element(KnowledgeBaseLocator.query_knowledge_type_select_loc)
        self.random_sleep(0.5)
        if knowledge_type == "问题总结":
            self.click_element(KnowledgeBaseLocator.problem_summary_option_loc)
        elif knowledge_type == "行业标准":
            self.click_element(KnowledgeBaseLocator.industry_standard_option_loc)
        elif knowledge_type == "规章制度":
            self.click_element(KnowledgeBaseLocator.rule_regulation_option_loc)
        elif knowledge_type == "项目资料":
            self.click_element(KnowledgeBaseLocator.project_info_option_loc)

    @allure.step("获取第一条知识类型")
    def get_first_knowledge_type(self):
        try:
            return self.text(KnowledgeBaseLocator.first_knowledge_type_loc)
        except:
            logger.warning("没有找到第一条知识类型")
            return 1

    @allure.step("选择撰写人查询条件")
    def input_writer_query_condition(self, writer):
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.writer_select_loc, writer
        )

    @allure.step("获取第一个知识的撰写人")
    def get_first_writer(self):
        try:
            return self.text(KnowledgeBaseLocator.first_knowledge_writer_loc)
        except:
            logger.warning("没有找到第一条知识撰写人")
            return 1

    @allure.step("选择关联设备类型条件")
    def select_device_type_query_condition(self, device_type):
        self.click_element(KnowledgeBaseLocator.device_type_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f"//*[@title='{device_type}']"))
        self.random_sleep(0.5)

    @allure.step("获取第一个知识的关联设备类型")
    def get_first_device_type(self):
        try:
            return self.text(KnowledgeBaseLocator.first_knowledge_device_type_loc)
        except:
            logger.warning("没有找到第一条知识关联设备类型")
            return 1

    @allure.step("选择异常环节查询条件")
    def select_abnormal_link_query_condition(self, abnormal_link):
        self.click_element(KnowledgeBaseLocator.query_abnormal_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f"//*[@title='{abnormal_link}']"))
        self.random_sleep(0.5)

    @allure.step("获取第一个知识异常环节")
    def get_first_no_abnormal_link(self):
        try:
            for i in range(2, 12):  # //*[@class="ant-table-tbody"]/tr[2]/td[9]
                if (
                    self.text(
                        (By.XPATH, f"//*[@class='ant-table-tbody']/tr[{i}]/td[9]")
                    )
                    != ""
                ):
                    return self.text(
                        (By.XPATH, f"//*[@class='ant-table-tbody']/tr[{i}]/td[9]")
                    )
        except:
            logger.warning("没有找到第一条知识异常环节")
            return 1

    @allure.step("获取第一个知识异常环节")
    def get_first_abnormal_link(self):
        return self.text(KnowledgeBaseLocator.first_knowledge_abnormal_loc)

    @allure.step("获取第一条知识状态")
    def get_first_knowledge_status(self):
        try:
            return self.text(KnowledgeBaseLocator.first_knowledge_status_loc)
        except:
            logger.warning("没有找到第一条知识状态")
            return 1

    @allure.step("输入知识状态查询条件")
    def input_knowledge_status_query_condition(self, knowledge_status):
        self.click_element(KnowledgeBaseLocator.query_knowledge_status_select_loc)
        self.random_sleep(0.5)
        if knowledge_status == "草稿":
            self.click_element(KnowledgeBaseLocator.draft_option_loc)
        elif knowledge_status == "待修改":
            self.click_element(KnowledgeBaseLocator.to_be_modified_option_loc)
        elif knowledge_status == "审核中":
            self.click_element(KnowledgeBaseLocator.under_review_option_loc)
        elif knowledge_status == "审核成功":
            self.click_element(KnowledgeBaseLocator.audit_success_option_loc)
        else:
            logger.warning("知识状态输入错误")

    # 编辑相关
    @allure.step("点击第一个知识的编辑按钮")
    def click_first_knowledge_edit_button(self):
        self.click_element(KnowledgeBaseLocator.first_knowledge_edit_button_loc)
        self.random_sleep(0.5)

    @allure.step("编辑操作")
    # def edit_operation(self,knowledge_type,knowledge_name,device_type,abnormal_link,new_knowledge_content):
    #     self.fill_add_knowledge_data(knowledge_type=knowledge_type,
    #                                  knowledge_title=knowledge_name,
    #                                  associated_device_type=device_type,
    #                                  abnormal=abnormal_link,
    #                                  knowledge_content=new_knowledge_content)
    def edit_operation(self, new_knowledge_title, new_knowledge_content):
        self.random_sleep(0.5)
        title = self.get_attribute(KnowledgeBaseLocator.title_input_loc, "value")
        # content = self.get_attribute(KnowledgeBaseLocator.content_input_loc, "value")
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.title_input_loc, new_knowledge_title
        )
        # self.__fill_add_knowledge_content(new_knowledge_content)
        return title

    @allure.step("根据输入的知识名称返回知识状态")
    def get_knowledge_status_by_title(self, knowledge_title):
        try:
            for i in range(2, 12):
                if (
                    self.text(
                        (By.XPATH, f"//*[@class='ant-table-tbody']/tr[{i}]/td[3]")
                    )
                    == knowledge_title
                ):
                    return self.text(
                        (By.XPATH, f"//*[@class='ant-table-tbody']/tr[{i}]/td[2]")
                    )
        except:
            logger.warning("没有找到第一条知识状态")
            return 1

    @allure.step("根据输入的知识名称点击对应的编辑按钮")
    def click_edit_button_by_title(self, knowledge_title):
        for i in range(2, 12):
            try:
                if (
                    self.text(
                        (By.XPATH, f"//*[@class='ant-table-tbody']/tr[{i}]/td[3]")
                    )
                    == knowledge_title
                ):
                    # //*[@class='ant-table-tbody']/tr[2]/td[last()]//button/span[text()="编辑"]/..
                    # self.click_element((By.XPATH, f'(//*[text()="编辑"])[{i-1}]'))
                    self.click_element(
                        (
                            By.XPATH,
                            f'//*[@class="ant-table-tbody"]/tr[{i}]/td[last()]//button/span[text()="编辑"]/..',
                        )
                    )
                    self.random_sleep(0.5)
                    break
            except:
                logger.warning("没有找到第一条知识状态")

    @allure.step("根据输入的知识名称点击对应的审核按钮")
    def click_audit_button_by_title(self, knowledge_title):
        for i in range(2, 12):
            try:
                if (
                    self.text(
                        (By.XPATH, f"//*[@class='ant-table-tbody']/tr[{i}]/td[3]")
                    )
                    == knowledge_title
                ):
                    self.click_element((By.XPATH, f'(//*[text()="审核"])[{i-1}]'))
                    self.random_sleep(0.5)
                    break
            except:
                logger.warning("根据输入的知识名称点击对应的审核按钮")

    # 审核相关
    @allure.step("点击第一个审核按钮")
    def click_first_audit_button(self):
        self.click_element(KnowledgeBaseLocator.first_audit_button_loc)
        self.random_sleep(0.5)

    # @ 点击审核界面的审核 按钮
    def click_audit_page_audit_button(self):
        self.click_element(KnowledgeBaseLocator.audit_page_audit_button_loc)
        self.random_sleep(0.5)

    @allure.step("审核操作")
    def audit_operation(self, audit_option, audit_remark):
        if audit_option == "审核通过":
            self.click_element(KnowledgeBaseLocator.audit_pass_option_loc)
        elif audit_option == "审核拒绝":
            self.click_element(KnowledgeBaseLocator.audit_reject_option_loc)
        self.send_keys_by_clear_and_typing(
            KnowledgeBaseLocator.audit_remark_input_loc, audit_remark
        )
