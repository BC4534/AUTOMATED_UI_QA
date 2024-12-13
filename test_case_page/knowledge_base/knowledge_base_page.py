import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from common.base_method import BasePage
from test_case_locator.knowledge_base.knowledge_base_locator import KnowledgeBaseLocator


class KnowledgeBasePage(BasePage):

    # 新增知识 问题总结
    def test_knowledge_base_02_1(self, title, content):
        self.switch_to_knowledge_base_page()
        self.click_add_knowledge_button()
        self.fill_add_knowledge_data_type_problem_summary(title, content)
        self.click_submit_button()

    # 规章制度
    def test_knowledge_base_02_2(self, title, content):
        self.switch_to_knowledge_base_page()
        self.click_add_knowledge_button()
        self.fill_add_knowledge_data_type_rule_regulation(title, content)
        self.click_save_button()

    # 行业标准
    def test_knowledge_base_02_3(self, title, content):
        self.switch_to_knowledge_base_page()
        self.click_add_knowledge_button()
        self.fill_add_knowledge_data_type_industry_standard(title, content)

    def test_knowledge_base_02_4(self, title, content):
        self.switch_to_knowledge_base_page()
        self.click_add_knowledge_button()
        self.fill_add_knowledge_data_type_project_material(title, content)
    # 新增知识，提交 必填项效验
    def test_knowledge_base_03_1(self):
        self.switch_to_knowledge_base_page()
        self.click_add_knowledge_button()
        self.click_submit_button()
        time.sleep(3)

    # 新增知识，保存 必填项效验
    def test_knowledge_base_03_2(self):
        self.switch_to_knowledge_base_page()
        self.click_add_knowledge_button()
        self.click_save_button()
        time.sleep(3)

    # 切换至知识库界面
    def switch_to_knowledge_base_page(self):
        self.click_element(KnowledgeBaseLocator.knowledge_base_loc)

    # 点击新增知识按钮
    def click_add_knowledge_button(self):
        self.click_element(KnowledgeBaseLocator.add_knowledge_button_loc)

    # 获取新增知识按钮文本
    def get_add_knowledge_button_text(self):
        return self.text(KnowledgeBaseLocator.add_knowledge_button_loc)

    # 点击删除知识按钮
    def click_delete_knowledge_button(self):
        self.click_element(KnowledgeBaseLocator.delete_knowledge_button_loc)

    # 点击审核按钮
    def click_audit_button(self):
        self.click_element(KnowledgeBaseLocator.audit_button_loc)

    # 点击详情按钮
    def click_detail_button(self):
        self.click_element(KnowledgeBaseLocator.detail_button_loc)

    # ------新增知识页面操作----
    # 填写新增知识数据 问题总结类
    def fill_add_knowledge_data_type_problem_summary(self, title, content):
        self.click_element(KnowledgeBaseLocator.knowledge_type_loc)
        self.click_element(KnowledgeBaseLocator.problem_summary_option_loc)
        time.sleep(0.5)
        self.send_keys(KnowledgeBaseLocator.title_input_loc, title)
        time.sleep(0.5)
        self.click_element(KnowledgeBaseLocator.project_loc)
        self.click_element(KnowledgeBaseLocator.first_project_option_loc)
        time.sleep(0.5)
        self.click_element(KnowledgeBaseLocator.device_type_loc)
        self.click_element(KnowledgeBaseLocator.device_215_option_loc)
        time.sleep(0.5)
        self.click_knowledge_base_page()
        self.click_element(KnowledgeBaseLocator.abnormal_loc)
        self.click_element(KnowledgeBaseLocator.abnormal_bms_option_loc)
        time.sleep(0.5)
        self.click_knowledge_base_page()
        time.sleep(0.5)
        self.click_element(KnowledgeBaseLocator.content_input_loc)
        self.send_keys(KnowledgeBaseLocator.content_input_loc, content)
        self.move_to_element(KnowledgeBaseLocator.content_input_loc)
        # 鼠标移入，页面下滑
        pyautogui.moveTo(1000, 900)
        self.scroll(-200)
        time.sleep(1)

    # 填写新增知识数据 规章制度类
    def fill_add_knowledge_data_type_rule_regulation(self, title, content):
        self.click_element(KnowledgeBaseLocator.knowledge_type_loc)
        self.click_element(KnowledgeBaseLocator.rule_regulation_option_loc)
        time.sleep(0.5)
        self.send_keys(KnowledgeBaseLocator.title_input_loc, title)
        time.sleep(0.5)
        self.click_element(KnowledgeBaseLocator.content_input_loc)
        self.send_keys(KnowledgeBaseLocator.content_input_loc, content)

    # 填写新增知识数据 行业标准类
    def fill_add_knowledge_data_type_industry_standard(self, title, content):
        self.click_element(KnowledgeBaseLocator.knowledge_type_loc)
        self.click_element(KnowledgeBaseLocator.industry_standard_option_loc)
        time.sleep(0.5)
        self.send_keys(KnowledgeBaseLocator.title_input_loc, title)
        time.sleep(0.5)
        self.click_element(KnowledgeBaseLocator.content_input_loc)
        self.send_keys(KnowledgeBaseLocator.content_input_loc, content)

    # # 填写新增知识数据 项目资料类
    def fill_add_knowledge_data_type_project_material(self, title, content):
        self.click_element(KnowledgeBaseLocator.knowledge_type_loc)
        self.click_element(KnowledgeBaseLocator.project_material_option_loc)
        time.sleep(0.5)
        self.send_keys(KnowledgeBaseLocator.title_input_loc, title)
        time.sleep(0.5)
        self.click_element(KnowledgeBaseLocator.content_input_loc)
        self.send_keys(KnowledgeBaseLocator.content_input_loc, content)
        time.sleep(1)

    # 点击 提交按钮
    def click_submit_button(self):
        time.sleep(1)
        # x, y = pyautogui.position()
        # print(f"鼠标当前位置: x={x}, y={y}")
        element = self.visibility_of_element_located(KnowledgeBaseLocator.submit_button_loc)
        # self.execute_script("arguments[0].click();", element)
        self.click_element(KnowledgeBaseLocator.submit_button_loc)
        self.action_chains_click(KnowledgeBaseLocator.submit_button_loc)


    # 点击保存按钮
    def click_save_button(self):
        element = self.visibility_of_element_located(KnowledgeBaseLocator.save_button_loc)
        self.execute_script("arguments[0].click();", element)
        self.click_element(KnowledgeBaseLocator.save_button_loc)

    # 点击 返回按钮
    def click_back_button(self):
        element = self.visibility_of_element_located(KnowledgeBaseLocator.back_button_loc)
        self.execute_script("arguments[0].click();", element)
        self.click_element(KnowledgeBaseLocator.back_button_loc)

    # 点击知识库界面
    def click_knowledge_base_page(self):
        self.click_element(KnowledgeBaseLocator.knowledge_base_page_loc)
