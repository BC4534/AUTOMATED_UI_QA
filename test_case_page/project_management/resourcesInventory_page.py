import logging
import time

from selenium.webdriver.common.by import By

from common.base_method import BasePage
from test_case_locator.project_management.resources_inventory_locator.resources_inventory_locator import (
    ResourcesInventoryLocator,
)


class ResourcesInventoryPage(BasePage):

    # 获取项目管理模块是否展开
    def get_project_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            ResourcesInventoryLocator.project_management_is_expand_loc, "class"
        )

    # 切换至人力资源复盘界面
    def switch_to_resources_inventory_page(self):
        if self.get_project_management_is_expand():
            self.click_element(ResourcesInventoryLocator.project_management_loc)
        self.click_element(ResourcesInventoryLocator.resources_inventory_loc)
        time.sleep(0.5)

    # 获取人员名称输入框文本 placeholder属性值
    def get_resources_inventory_name_input_placeholder(self):
        return self.get_attribute(
            ResourcesInventoryLocator.resources_inventory_name_input_loc, "placeholder"
        )

    # 点击确定按钮
    def click_confirm_button(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_confirm_button_loc
        )
        self.random_sleep(0.5)

    # 点击取消按钮
    def click_cancel_button(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_cancel_button_loc
        )
        self.random_sleep(0.5)

    # 点击取消按钮
    def click_close_button(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_close_button_loc
        )
        self.random_sleep(0.5)

    # 点击第一个项目总数
    def click_project_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_project_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个实施项目数 非0
    def click_implementation_project_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_implementation_project_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个售后质保项目数
    def click_after_sales_warranty_project_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_after_sales_warranty_project_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个售后过保项目数
    def click_after_sales_expired_project_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_after_sales_expired_project_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个处理任务总数
    def click_task_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_task_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个处理实施工单数
    def click_implementation_work_order_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_implementation_work_order_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个处理巡检工单数
    def click_inspection_work_order_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_inspection_work_order_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个处理异常工单数
    def click_abnormal_work_order_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_abnormal_work_order_count_loc
        )
        self.random_sleep(0.5)

    # 点击第一个待办工单数
    def click_pending_work_order_count(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_first_pending_work_order_count_loc
        )
        self.random_sleep(0.5)

    # 获取项目名称
    def get_project_name_loc_text(self):
        return self.text(ResourcesInventoryLocator.resources_inventory_project_name_loc)

    # 获取工单名称
    def get_work_order_name_loc_text(self):
        return self.text(
            ResourcesInventoryLocator.resources_inventory_work_order_name_loc
        )

    # 获取第一个人员名称
    def get_first_name_loc_text(self):
        return self.text(ResourcesInventoryLocator.resources_inventory_first_name_loc)

    # 获取第二个人员名称
    def get_second_name_loc_text(self):
        return self.text(ResourcesInventoryLocator.resources_inventory_second_name_loc)

    # 获取第一个区域名称
    def get_first_area_loc_text(self):
        return self.text(ResourcesInventoryLocator.resources_inventory_first_area_loc)

    # 获取第二个区域名称
    def get_second_area_loc_text(self):
        return self.text(ResourcesInventoryLocator.resources_inventory_second_area_loc)

    # 人员名称查询
    def resources_inventory_search_by_name(self, name):
        self.send_keys_by_clear_and_typing(
            ResourcesInventoryLocator.resources_inventory_name_input_loc, name
        )
        self.random_sleep(0.5)

    # 选择所属区域查询
    def resources_inventory_search_by_area(self, area):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_area_select_loc
        )
        self.random_sleep(0.5)
        if area == "东部":
            self.click_element(
                ResourcesInventoryLocator.resources_inventory_area_option_east_loc
            )
        elif area == "西北":
            self.click_element(
                ResourcesInventoryLocator.resources_inventory_area_option_northwest_loc
            )
        elif area == "大储运维（宁夏）":
            self.click_element(
                ResourcesInventoryLocator.resources_inventory_area_option_northwest_nx_loc
            )
        elif area == "南方":
            self.click_element(
                ResourcesInventoryLocator.resources_inventory_area_option_south_loc
            )
        elif area == "海外":
            self.click_element(
                ResourcesInventoryLocator.resources_inventory_area_option_west_loc
            )
        else:
            logging.info("未找到区域选项")
            self.click_element(
                ResourcesInventoryLocator.resources_inventory_area_option_east_loc
            )
            return 1
        self.random_sleep(0.5)

    # 点击查询按钮
    def click_search_button(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_search_button_loc
        )
        self.random_sleep(0.5)

    # 点击重置按钮
    def click_reset_button(self):
        self.click_element(
            ResourcesInventoryLocator.resources_inventory_reset_button_loc
        )
        self.random_sleep(0.5)
