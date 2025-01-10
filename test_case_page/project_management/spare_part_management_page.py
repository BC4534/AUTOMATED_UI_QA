import time

import allure
from selenium.webdriver.common.by import By
from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.project_management.spare_parts_management_locator.spare_part_management_locator import (
    SparePartManagementLocator,
)


class SparePartManagementPage(BasePage):

    # 获取项目管理模块是否展开
    def get_project_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(
            SparePartManagementLocator.project_management_is_expand_loc, "class"
        )

    # 切换至备件管理界面
    def switch_to_spare_part_management_page(self):
        if self.get_project_management_is_expand():
            self.click_element(SparePartManagementLocator.project_management_loc)
        self.click_element(SparePartManagementLocator.spare_part_management_loc)
        time.sleep(0.5)

    # 获取备件入库按钮文本
    def get_spare_part_inbound_button_text(self):
        return self.text(SparePartManagementLocator.spare_part_inbound_button_loc)

    # 点击备件入库按钮
    def click_spare_part_inbound_button(self):
        self.click_element(SparePartManagementLocator.spare_part_inbound_button_loc)

    # 点击备件入库确定 按钮
    def click_spare_part_inbound_confirm_button(self):
        time.sleep(1)
        self.click_element(SparePartManagementLocator.fill_data_confirm_button_loc)
        time.sleep(1)

    @allure.step("点击备件领用确定按钮")
    def click_spare_part_receive_confirm_button(self):
        time.sleep(1)
        self.click_element(SparePartManagementLocator.spare_part_receive_confirm_button_loc)


    # 点击备件入库 取消按钮
    def click_spare_part_inbound_cancel_button(self):
        self.click_element(SparePartManagementLocator.fill_data_cancel_button_loc)

    # 点击备件入库 X按钮
    def click_spare_part_inbound_close_button(self):
        self.click_element(SparePartManagementLocator.fill_data_close_button_loc)

    # 新增备件入库
    def add_spare_part_inbound(
        self,
        part_attribute,
        part_name,
        part_number,
        part_remark,
        part_type,
        part_vendor,
        part_warehouse,
        part_inbound_remark,
    ):

        # 检查入库方式 ant-radio-checked
        if "ant-radio-checked" not in self.get_attribute(
            SparePartManagementLocator.add_spare_part_button_loc, "class"
        ):
            self.click_element(SparePartManagementLocator.add_spare_part_button_loc)
        # 备件属性 选择框
        self.click_element(
            SparePartManagementLocator.fill_data_spare_part_attribute_select_loc
        )
        if part_attribute not in ["供应商预存备件", "采日自研备件", "采日自采备件"]:
            self.click_element(
                SparePartManagementLocator.self_developed_by_spare_part_option_loc
            )
            logger.info("备件属性选择有误，默认选择采日自研备件")
        else:
            self.click_element(
                (By.XPATH, f'//*[@title="{part_attribute}" and @aria-selected]')
            )
        self.random_sleep(0.5)
        # 备件类型
        self.click_element(
            SparePartManagementLocator.fill_data_spare_part_type_select_loc
        )
        if part_type not in [
            "EMS类附件",
            "PCS类附件",
            "变压器",
            "汇集交换机",
            "BMU",
            "高压箱",
            "显示屏",
            "高压箱内附件",
            "汇流柜内附件",
            "电芯",
            "电池模组内附件",
            "液冷系统",
            "消防系统",
            "动力线束",
            "通信线束",
            "空调",
            "集装箱附件",
            "熔断器",
            "采样线束",
            "UPS",
            "接触器",
        ]:
            self.click_element(SparePartManagementLocator.type_of_ems_option_loc)
        else:
            try:
                self.click_element(
                    (By.XPATH, f'//*[@title="{part_type}" and @aria-selected]')
                )
            except:
                # self.scroll_with_mouse_wheel(SparePartManagementLocator.type_list_option_loc,1000)
                # self.scroll_with_mouse_wheel(SparePartManagementLocator.type_list_option_loc,-100)
                # self.click_element((By.XPATH, f'//*[@title="{part_type}" and @aria-selected]'))
                self.click_element(SparePartManagementLocator.type_of_ems_option_loc)
                logger.info("备件类型选择有误，默认选择EMS类附件")

        self.random_sleep(0.5)
        # 所属供应商
        if part_attribute != "采日自研备件":
            self.click_element(SparePartManagementLocator.fill_data_vendor_select_loc)
            try:
                self.click_element(
                    (By.XPATH, f'//*[@title="{part_vendor}" and @aria-selected]')
                )
            except:
                self.click_element(SparePartManagementLocator.first_vendor_option_loc)

        # 所属仓库
        self.click_element(SparePartManagementLocator.fill_data_warehouse_select_loc)
        if part_warehouse not in ["上海备品仓", "宁夏备品仓"]:
            self.click_element(
                SparePartManagementLocator.warehouse_of_shanghai_option_loc
            )
            logger.info("备件仓库选择有误，默认选择上海备品仓")
        else:
            self.click_element(
                (By.XPATH, f'//*[@title="{part_warehouse}" and @aria-selected]')
            )
        self.random_sleep(0.5)
        # 备件名称
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.fill_data_spare_part_name_input_loc, part_name
        )
        # 备件数量
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.fill_data_spare_part_number_input_loc,
            part_number,
        )
        #  备件备注
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.fill_data_spare_part_remark_input_loc,
            part_remark,
        )
        # 入库备注
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.fill_data_spare_part_inbound_remark_input_loc,
            part_inbound_remark,
        )

    # 维护已有备件
    def maintain_spare_part(self, part_name, part_number, part_inbound_remark):
        # 检查入库方式 ant-radio-checked
        if "ant-radio-checked" not in self.get_attribute(
            SparePartManagementLocator.maintain_spare_part_button_loc, "class"
        ):
            self.click_element(
                SparePartManagementLocator.maintain_spare_part_button_loc
            )
        # 备件名称选择
        self.click_element(
            SparePartManagementLocator.maintain_spare_part_name_select_loc
        )
        try:
            self.click_element(
                (By.XPATH, f'//*[@title="{part_name}" and @aria-selected]')
            )
        except:
            self.click_element(
                SparePartManagementLocator.first_spare_part_name_option_loc
            )
            logger.info("备件名称选择有误，默认选择第一个备件名称")
        # 备件数量
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.fill_data_spare_part_number_input_loc,
            part_number,
        )
        # 入库备注
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.fill_data_spare_part_inbound_remark_input_loc,
            part_inbound_remark,
        )

    def get_page_tip_text(self):
        b = self.text(SparePartManagementLocator.page_tip_loc)
        logger.debug("页面保存成功提示信息为：" + b)
        return b

    # 判断是否在别急入库信息填写界面
    def is_in_spare_part_inbound_page(self):
        try:
            self.visibility_of_element_located(
                SparePartManagementLocator.spare_part_inbound_title_loc, 1, 1
            )
            return True
        except:
            return False

    # 点击第一个备件的查看出入库记录按钮
    def click_first_spare_part_view_inbound_record_button(self):
        self.click_element(
            SparePartManagementLocator.first_spare_part_view_inbound_record_button_loc
        )

    # 获取入库记录弹窗标题
    def get_spare_part_inbound_record_title(self):
        return self.text(SparePartManagementLocator.spare_part_inbound_record_title_loc)

    # 点击出入记录X按钮
    def click_spare_part_inbound_record_close_button(self):
        self.click_element(
            SparePartManagementLocator.spare_part_inbound_record_close_button_loc
        )

    # 点击第一条数据的备件领用按钮
    def click_first_spare_part_receive_button(self):
        self.click_element(
            SparePartManagementLocator.first_spare_part_receive_button_loc
        )

    # 获取备件领用弹窗标题
    def get_spare_part_receive_title(self):
        return self.text(SparePartManagementLocator.spare_part_receive_title_loc)

    # 备件领用流程
    def spare_part_receive(self, part_number, part_project, part_remark):
        # 备件领用数量
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.spare_part_receive_number_input_loc, part_number
        )
        # 备件领用项目
        self.click_element(
            SparePartManagementLocator.spare_part_receive_project_select_loc
        )
        try:
            # //*[@title="南翔待实施项目" and @aria-selected]
            self.click_element(
                (By.XPATH, f'//*[@title="{part_project}" and @aria-selected]')
            )
        except:
            self.click_element(
                SparePartManagementLocator.spare_part_receive_project_first_option_loc
            )
            logger.info("备件领用项目选择有误，默认选择第一个项目")
            self.random_sleep(0.5)
        # 输入备件领用备注
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.spare_part_receive_remark_input_loc, part_remark
        )

    # 获取备件领用 库存备件数量
    def get_spare_part_receive_stock_number(self):
        return self.get_attribute(
            SparePartManagementLocator.spare_part_receive_stock_number_loc, "value"
        )

    # 翻页功能
    def page_turning(self):
        try:
            # 判断第二页是否存在
            if self.visibility_of_element_located(SparePartManagementLocator.second_page_loc):
                self.click_element(SparePartManagementLocator.second_page_loc)
                self.random_sleep(0.5)
                self.click_element(SparePartManagementLocator.previous_page_loc)
                self.random_sleep(0.5)
                self.click_element(SparePartManagementLocator.next_page_loc)
                self.random_sleep(0.5)
                self.click_element(SparePartManagementLocator.first_page_loc)
                self.random_sleep(0.5)
        except:
            logger.info("第二页不存在")
            return 1

    # 判断当前所在页 class="ant-pagination-item ant-pagination-item-1 ant-pagination-item-active"
    def is_current_page(self, loc=SparePartManagementLocator.first_page_loc):
        if "ant-pagination-item-active" in self.get_attribute(loc, "class"):
            return True
        else:
            return False

    # 查询相关
    # 点击搜索按钮
    def click_search_button(self):
        self.click_element(SparePartManagementLocator.search_button_loc)

    # 点击重置按钮
    def click_reset_button(self):
        self.click_element(SparePartManagementLocator.reset_button_loc)

    # 通过备件名称查询
    def search_by_spare_part_name(self, part_name):
        self.send_keys_by_clear_and_typing(
            SparePartManagementLocator.search_spare_part_name_input_loc, part_name
        )
        self.random_sleep(0.5)

    # 获取第二个备件名称
    def get_second_spare_part_name(self):
        return self.text(SparePartManagementLocator.second_spare_part_name_loc)

    # 获取第一个备件名称
    def get_first_spare_part_name(self):
        return self.text(SparePartManagementLocator.first_spare_part_name_loc)

    # 通过备件类型查询
    def search_by_spare_part_type(self, part_type):
        self.click_element(SparePartManagementLocator.search_spare_part_type_select_loc)
        try:
            # //*[@class="ant-select-item-option-content" and text()="EMS类附件"]
            self.click_element(
                (
                    By.XPATH,
                    f'//*[@class="ant-select-item-option-content" and text()="{part_type}"]',
                )
            )
            return 0
        except:
            self.click_element(
                SparePartManagementLocator.search_spare_part_type_first_option_loc
            )
            logger.info("备件类型选择有误，默认选择第一个备件类型")
            return 1

    # 获取第一个备件 类型
    def get_first_spare_part_type(self):
        return self.text(SparePartManagementLocator.fitst_spare_part_type_text_loc)

    # 获取第二个备件 类型
    def get_second_spare_part_type(self):
        return self.text(SparePartManagementLocator.second_spare_part_type_text_loc)

    # 通过所属仓库查询
    def search_by_spare_part_warehouse(self, part_warehouse):
        self.click_element(
            SparePartManagementLocator.search_spare_part_warehouse_select_loc
        )
        if part_warehouse == "上海备品仓":
            self.click_element(
                SparePartManagementLocator.search_spare_part_warehouse_shanghai_loc
            )
        elif part_warehouse == "宁夏备品仓":
            self.click_element(
                SparePartManagementLocator.search_spare_part_warehouse_ningxia_loc
            )
        else:
            self.click_element(
                SparePartManagementLocator.search_spare_part_warehouse_shanghai_loc
            )
            logger.info("备件所属仓库选择有误，默认选择上海备品仓")

    # 获取第一个备件 所属仓库
    def get_first_spare_part_warehouse(self):
        return self.text(SparePartManagementLocator.first_spare_part_warehouse_text_loc)

    # 通过备件属性查询
    def search_by_spare_part_attribute(self, part_attribute):
        self.click_element(
            SparePartManagementLocator.search_spare_part_attribute_select_loc
        )
        if part_attribute == "供应商预存备件":
            self.click_element(
                SparePartManagementLocator.search_spare_part_attribute_supplier_pre_spare_part_loc
            )
        elif part_attribute == "采日自研备件":
            self.click_element(
                SparePartManagementLocator.search_spare_part_attribute_self_develop_spare_part_loc
            )
        elif part_attribute == "采日自采备件":
            self.click_element(
                SparePartManagementLocator.search_spare_part_attribute_self_purchase_spare_part_loc
            )
        else:
            self.click_element(
                SparePartManagementLocator.search_spare_part_attribute_supplier_pre_spare_part_loc
            )
            logger.info("备件属性选择有误，默认选择供应商预存备件")

    # 获取第一个备件 属性
    def get_first_spare_part_attribute(self):
        self.random_sleep(0.5)
        return self.text(SparePartManagementLocator.first_spare_part_attribute_text_loc)

    # 第二个备件 属性
    def get_second_spare_part_attribute(self):
        return self.text(
            SparePartManagementLocator.second_spare_part_attribute_text_loc
        )

    # 通过所属供应商查询
    def search_by_spare_part_supplier(self, part_supplier):
        self.click_element(
            SparePartManagementLocator.search_spare_part_supplier_select_loc
        )
        try:
            self.click_element(
                (
                    By.XPATH,
                    f'//*[@class="ant-select-item-option-content" and text()="{part_supplier}"]/..',
                )
            )
        except:
            self.click_element(
                SparePartManagementLocator.search_spare_part_supplier_first_option_loc
            )
            logger.info("备件所属供应商选择有误，默认选择第一个备件供应商")
            return self.text(
                SparePartManagementLocator.first_spare_part_supplier_text_loc
            )

    # 获取第一个备件 供应商
    def get_first_spare_part_supplier(self):
        self.random_sleep(0.5)
        return self.text(SparePartManagementLocator.first_spare_part_supplier_text_loc)

    # 获取第二个备件 供应商
    def get_second_spare_part_supplier(self):
        return self.text(SparePartManagementLocator.second_spare_part_supplier_text_loc)

    # 删除相关
    # 判断第一个项目名称是否包含：UI测试
    def is_first_spare_part_name_contain_ui_test(self):
        if "UI测试" in self.get_first_spare_part_name():
            return True
        else:
            return False

    # 读取第一个备件数量
    def get_first_spare_part_number(self):
        return self.text(SparePartManagementLocator.first_spare_part_number_text_loc)

    # 读取第二个备件数量
    def get_second_spare_part_number(self):
        return self.text(SparePartManagementLocator.second_spare_part_number_text_loc)

    # 读取第三个备件数量
    def get_third_spare_part_number(self):
        return self.text(SparePartManagementLocator.third_spare_part_number_text_loc)

    # 勾选全选复选框
    def check_all_spare_part_checkbox(self):
        self.click_element(SparePartManagementLocator.spare_part_all_checkbox_loc)

    # 勾选第一个备件复选框
    def check_first_spare_part_checkbox(self):
        self.click_element(SparePartManagementLocator.first_spare_part_checkbox_loc)

    # 勾选第二个备件复选框
    def check_second_spare_part_checkbox(self):
        self.click_element(SparePartManagementLocator.second_spare_part_checkbox_loc)

    # 点击删除备件按钮
    def click_delete_spare_part_button(self):
        self.click_element(SparePartManagementLocator.delete_spare_part_button_loc)
        time.sleep(0.5)
