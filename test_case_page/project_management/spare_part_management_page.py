import time
from selenium.webdriver.common.by import By
from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.project_management.spare_parts_management_locator.spare_part_management_locator import \
    SparePartManagementLocator


class SparePartManagementPage(BasePage):

    # 获取项目管理模块是否展开
    def get_project_management_is_expand(self):
        return "ant-menu-submenu-open" not in self.get_attribute(SparePartManagementLocator.project_management_is_expand_loc, "class")

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
    # 点击备件入库 取消按钮
    def click_spare_part_inbound_cancel_button(self):
        self.click_element(SparePartManagementLocator.fill_data_cancel_button_loc)
    # 点击备件入库 X按钮
    def click_spare_part_inbound_close_button(self):
        self.click_element(SparePartManagementLocator.fill_data_close_button_loc)

    # 新增备件入库
    def add_spare_part_inbound(self, part_attribute, part_name, part_number, part_remark, part_type, part_vendor, part_warehouse, part_inbound_remark):

        # 检查入库方式 ant-radio-checked
        if "ant-radio-checked" not in self.get_attribute(SparePartManagementLocator.add_spare_part_button_loc, "class"):
            self.click_element(SparePartManagementLocator.add_spare_part_button_loc)
        # 备件属性 选择框
        self.click_element(SparePartManagementLocator.fill_data_spare_part_attribute_select_loc)
        if part_attribute not in ["供应商预存备件", "采日自研备件", "采日自采备件"]:
            self.click_element(SparePartManagementLocator.self_developed_by_spare_part_option_loc)
            logger.info("备件属性选择有误，默认选择采日自研备件")
        else:
            self.click_element((By.XPATH, f'//*[@title="{part_attribute}" and @aria-selected]'))
        self.random_sleep(0.5)
        # 备件类型
        self.click_element(SparePartManagementLocator.fill_data_spare_part_type_select_loc)
        if part_type not in ["EMS类附件", "PCS类附件", "变压器", "汇集交换机", "BMU", "高压箱", "显示屏", "高压箱内附件", "汇流柜内附件",
                             "电芯", "电池模组内附件", "液冷系统", "消防系统", "动力线束", "通信线束", "空调", "集装箱附件", "熔断器",
                             "采样线束", "UPS", "接触器"]:
            self.click_element(SparePartManagementLocator.type_of_ems_option_loc)
        else:
            try:
                self.click_element((By.XPATH, f'//*[@title="{part_type}" and @aria-selected]'))
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
                self.click_element((By.XPATH, f'//*[@title="{part_vendor}" and @aria-selected]'))
            except:
                self.click_element(SparePartManagementLocator.first_vendor_option_loc)

        # 所属仓库
        self.click_element(SparePartManagementLocator.fill_data_warehouse_select_loc)
        if part_warehouse not in ["上海备品仓", "宁夏备品仓"]:
            self.click_element(SparePartManagementLocator.warehouse_of_shanghai_option_loc)
            logger.info("备件仓库选择有误，默认选择上海备品仓")
        else:
            self.click_element((By.XPATH, f'//*[@title="{part_warehouse}" and @aria-selected]'))
        self.random_sleep(0.5)
        # 备件名称
        self.send_keys_by_clear_and_typing(SparePartManagementLocator.fill_data_spare_part_name_input_loc, part_name)
        # 备件数量
        self.send_keys_by_clear_and_typing(SparePartManagementLocator.fill_data_spare_part_number_input_loc, part_number)
        #  备件备注
        self.send_keys_by_clear_and_typing(SparePartManagementLocator.fill_data_spare_part_remark_input_loc, part_remark)
        # 入库备注
        self.send_keys_by_clear_and_typing(SparePartManagementLocator.fill_data_spare_part_inbound_remark_input_loc, part_inbound_remark)

    # 维护已有备件
    def maintain_spare_part(self, part_name, part_number, part_inbound_remark):
        # 备件名称选择
        self.click_element(SparePartManagementLocator.fill_data_spare_part_name_input_loc)
        self.click_element((By.XPATH, f'//*[@title="{part_name}" and @aria-selected]'))
        # 备件数量
        self.send_keys_by_clear_and_typing(SparePartManagementLocator.fill_data_spare_part_number_input_loc, part_number)
        #入库备注
        self.send_keys_by_clear_and_typing(SparePartManagementLocator.fill_data_spare_part_inbound_remark_input_loc, part_inbound_remark)


    # 获取第一个备件名称
    def get_first_spare_part_name(self):
        return self.text(SparePartManagementLocator.first_spare_part_name_loc)

    def get_page_tip_text(self):
        b = self.text(SparePartManagementLocator.page_tip_loc)
        logger.debug("页面保存成功提示信息为：" + b)
        return b

    # 判断是否在别急入库信息填写界面
    def is_in_spare_part_inbound_page(self):
        try:
            self.visibility_of_element_located(SparePartManagementLocator.spare_part_inbound_title_loc, 1, 1)
            return True
        except:
            return False
