import time

from selenium.webdriver.common.by import By

from common.base_method import BasePage
from test_case_locator.project_management.electronic_archives_locator.electronic_archives_locator import \
    ElectronicArchivesLocator
from test_case_locator.project_management.electronic_archives_locator.add_project_locator import \
    AddProjectLocator, ProjectBaseInfoLocator, ImplementationMaintenanceInfoLocator, OperationManagementInfoLocator
from common.loggerhandler import logger


class ElectronicArchivesPage(BasePage):

    # 获取第一个项目名称
    def get_first_project_name(self):
        b = self.text(ElectronicArchivesLocator.first_project_name_loc)
        logger.debug("第一个项目名称为：" + b)
        return b
    # 获取第二个项目名称
    def get_second_project_name(self):
        b = self.text(ElectronicArchivesLocator.second_project_name_loc)
        logger.debug("第二个项目名称为：" + b)
        return b

    # 获取第二个项目的立项时间
    def get_second_project_init_time(self):
        b = self.text(ElectronicArchivesLocator.second_project_init_time_loc)
        logger.debug("第二个项目的立项时间为：" + b)
        return b

    # 获取第一个项目的立项时间
    def get_first_project_init_time(self):
        b = self.text(ElectronicArchivesLocator.first_project_init_time_loc)
        logger.debug("第一个项目的立项时间为：" + b)
        return b
    # 立项时间查询框输入 立项时间查询条件
    # def input_init_time_query_condition(self, init_time):
    #     year = self.text(ElectronicArchivesLocator.current_year_value_loc)[2:4]
    #     month = self.text(ElectronicArchivesLocator.current_month_value_loc)[0:2]
    #     y = init_time[0:4]
    #     m = init_time[5:7]
    #     d = init_time[8:10]
    #     if int(y) == int(year):
    #         if int(m) == int(month):
    #             # //*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="25"]
    #             self.click_element(
    #                 (By.XPATH, f'//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="{d}"]'))
    #         elif int(m) < int(month):
    #             for i in range(int(month) - int(m)):
    #                 self.click_element(ElectronicArchivesLocator.previous_month_button_loc)
    #             self.click_element(
    #                 (By.XPATH, f'//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="{d}"]'))
    #     elif int(y) < int(year):
    #         for i in range(int(year) - int(y)):
    #             self.click_element(ElectronicArchivesLocator.previous_year_button_loc)
    #
    #         if int(m) == int(month):
    #             # //*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="25"]
    #             self.click_element((By.XPATH,f'//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="{d}"]'))
    #         elif int(m) < int(month):
    #             for i in range(int(month) - int(m)):
    #                 self.click_element(ElectronicArchivesLocator.previous_month_button_loc)
    #             self.click_element((By.XPATH,f'//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="{d}"]'))

    def input_init_time_query_condition(self, init_time):
        """
        输入指定的日期。
        """
        self.move_to_element(ElectronicArchivesLocator.project_time_select_loc)
        self.click_element(ElectronicArchivesLocator.project_time_select_loc)
        year = self.text(ElectronicArchivesLocator.current_year_value_loc)[0:4]
        month = self.text(ElectronicArchivesLocator.current_month_value_loc)[0:2]
        y = init_time[0:4]
        m = init_time[5:7]
        d = init_time[8:10]
        # 如果年份相同
        if int(y) == int(year):
            # 如果月份相同，直接点击日期
            if int(m) == int(month):
                self.click_date(d)
            else:
                for _ in range(int(month) - int(m)):
                    self.click_element(ElectronicArchivesLocator.previous_month_button_loc)
                self.click_date(d)
        # 如果年份小于当前年份，先点击上一年按钮，然后导航到日期
        else:
            for _ in range(int(year) - int(y)):
                self.click_element(ElectronicArchivesLocator.previous_year_button_loc)
            if int(m) == int(month):
                self.click_date(d)
            else:
                for _ in range(int(month) - int(m)):
                    self.click_element(ElectronicArchivesLocator.previous_month_button_loc)
                self.click_date(d)

    def click_date(self, day):
        """
        点击指定的日期。
        """
        self.click_element(
            (By.XPATH, f'//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="{day}"]'))



    # 选择工单所属区域 -默认东部
    def select_work_order_area(self, area):
        self.click_element(ElectronicArchivesLocator.work_order_area_select_loc)
        self.click_element((By.XPATH, f'//*[@title="{area}"]'))

    # 获取第二个项目的所属区域
    def get_second_project_area(self):
        b = self.text(ElectronicArchivesLocator.second_project_area_loc)
        logger.debug("第二个项目的所属区域为：" + b)
        return b
    # 获取第一个项目的所属区域
    def get_first_project_area(self):
        b = self.text(ElectronicArchivesLocator.first_project_area_loc)
        logger.debug("第一个项目的所属区域为：" + b)
        return b

    # 获取第一个项目所属阶段
    def get_first_project_stage(self):
        return self.text(ElectronicArchivesLocator.first_project_stage_loc)

    # 获取第二个项目所属阶段
    def get_second_project_stage(self):
        return self.text(ElectronicArchivesLocator.second_project_stage_loc)

    # 项目阶段查询操作过程
    def input_project_stage_query(self, stage):
        self.click_element(ElectronicArchivesLocator.project_stage_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{stage}"]'))
        self.random_sleep(0.5)

    # 获取第一个项目进度
    def get_first_project_progress(self):
        return self.text(ElectronicArchivesLocator.first_project_progress_loc)

    # 获取第二个项目进度
    def get_second_project_progress(self):
        return self.text(ElectronicArchivesLocator.second_project_progress_loc)

    # 项目进度查询操作过程
    def input_project_progress_query(self, progress):
        self.click_element(ElectronicArchivesLocator.project_stage_select_loc)
        if progress == "计划期":
            self.click_element(ElectronicArchivesLocator.project_stage_wait_for_implementation_loc)
            self.random_sleep(0.5)
            self.click_element(ElectronicArchivesLocator.project_progress_select_loc)
            self.random_sleep(0.5)
            self.click_element((By.XPATH, f'//*[@title="{progress}"]'))
        elif progress in ["准备期","发货期","调试期","试运行"]:
            self.click_element(ElectronicArchivesLocator.project_stage_implementation_loc)
            self.random_sleep(0.5)
            self.click_element(ElectronicArchivesLocator.project_progress_select_loc)
            self.random_sleep(0.5)
            self.click_element((By.XPATH, f'//*[@title="{progress}"]'))
        elif progress in ["质保期","已过保"]:
            self.click_element(ElectronicArchivesLocator.project_stage_after_sale_loc)
            self.random_sleep(0.5)
            self.click_element(ElectronicArchivesLocator.project_progress_select_loc)
            self.random_sleep(0.5)
            self.click_element((By.XPATH, f'//*[@title="{progress}"]'))
        else:
            logger.error("输入的进度类型不存在！")





    # 获取第一个项目类型
    def get_first_project_type(self):
        return self.text(ElectronicArchivesLocator.first_project_type_loc)
    # 获取第二个项目类型
    def get_second_project_type(self):
        return self.text(ElectronicArchivesLocator.second_project_type_loc)

    # 项目类型查询操作过程
    def input_project_type_query(self, type):
        self.click_element(ElectronicArchivesLocator.project_type_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{type}"]'))
        self.random_sleep(0.5)


    # 获取第一个产品类型
    def get_first_project_product_type(self):
        return self.text(ElectronicArchivesLocator.first_project_product_type_loc)
    # 获取第二个产品类型
    def get_second_project_product_type(self):
        return self.text(ElectronicArchivesLocator.second_project_product_type_loc)
    # 项目产品类型查询操作过程
    def input_project_product_type_query(self, type):
        self.click_element(ElectronicArchivesLocator.product_type_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{type}"]'))
        self.random_sleep(0.5)


    # 获取第一个实施负责人
    def get_first_project_implement_leader(self):
        return self.text(ElectronicArchivesLocator.first_project_implement_leader_loc)
    # 获取第二个实施负责人
    def get_second_project_implement_leader(self):
        return self.text(ElectronicArchivesLocator.second_project_implement_leader_loc)
    # 项目实施负责人查询操作过程
    def input_project_implement_leader_query(self, leader):
        self.click_element(ElectronicArchivesLocator.implement_leader_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{leader}"]'))
    # 获取第一个项目运维负责人
    def get_first_project_operation_leader(self):
        return self.text(ElectronicArchivesLocator.first_project_operation_leader_loc)
    # 获取第二个项目运维负责人
    def get_second_project_operation_leader(self):
        n = 3
        while True:
            a = self.text((By.XPATH, f'//*[@class="ant-table-tbody"]/tr[{n}]/td[13]'))
            if  a == "":
                n += 1
            else:
                return self.text((By.XPATH, f'//*[@class="ant-table-tbody"]/tr[{n}]/td[13]'))


    # 项目运维负责人查询操作过程
    def input_project_operation_leader_query(self, leader):
        self.click_element(ElectronicArchivesLocator.operation_leader_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{leader}"]'))
    # 获取第一个项目状态
    def get_first_project_status(self):
        return self.text(ElectronicArchivesLocator.first_project_status_loc)

    # 选择草稿状态搜索
    def input_project_status_query(self, status):
        self.click_element(ElectronicArchivesLocator.project_status_select_loc)
        self.random_sleep(0.5)
        self.click_element((By.XPATH, f'//*[@title="{status}"]'))
    # 获取第一个项目是否支持标准巡检
    def get_first_project_is_support_standard_inspection(self):
        return self.text(ElectronicArchivesLocator.first_project_is_support_standard_inspection_loc)

    # 巡检状态查询操作过程
    def input_project_is_support_standard_inspection_query(self, status):
        self.click_element((By.XPATH, f'//*[text()="{status}"]/preceding-sibling::span'))













    # 页面保存成功提示信息
    def get_page_tip_text(self):
        b = self.text(ElectronicArchivesLocator.page_tip_loc)
        logger.debug("页面保存成功提示信息为：" + b)
        return b

    # 获取项目管理模块class属性
    def _get_project_management_module_class(self):
        # ant-menu-submenu ant-menu-submenu-inline
        # ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-open ant-menu-submenu-active

        b = self.get_attribute(ElectronicArchivesLocator.project_management_module_class_attributes_loc, "class")
        logger.debug("项目管理模块class属性为：" + b)
        return b

    # 切换至电子档案界面
    def switch_to_electronic_archives(self):
        # 'ant-menu-submenu ant-menu-submenu-inline'
        if "ant-menu-submenu ant-menu-submenu-inline" == self._get_project_management_module_class():
            self.click_element(ElectronicArchivesLocator.project_management_loc)
            print(self._get_project_management_module_class())
        self.click_element_by_js(ElectronicArchivesLocator.electronic_archives_loc)
        self.logger.info("切换至电子档案界面")

    # 点击保存按钮
    def click_save_button(self):
        self.click_element(ElectronicArchivesLocator.save_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击保存按钮")

    # 点击下一步按钮
    def click_next_button(self):
        self.click_element(ElectronicArchivesLocator.next_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击下一步按钮")

    # 点击上一步按钮
    def click_previous_button(self):
        self.click_element(ElectronicArchivesLocator.previous_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击上一步按钮")

    # 点击提交
    def click_submit_button(self):
        time.sleep(2)
        self.click_element(ElectronicArchivesLocator.submit_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击提交按钮")
        time.sleep(4)

    # 点击关闭按钮
    def click_close_button(self):
        self.click_element(AddProjectLocator.close_button_loc)
        self.random_sleep(0.5)
        self.logger.info("点击关闭按钮")

    # 获取新增项目按钮文本值
    def get_add_project_button_text(self):
        b = self.text(ElectronicArchivesLocator.add_project_button_loc)
        logger.debug("新增项目按钮文本值为：" + b)
        return b

    # 获取供应商维护按钮文本值
    def get_supplier_maintenance_button_text(self):
        b = self.text(ElectronicArchivesLocator.supplier_maintenance_button_loc)
        logger.debug("供应商维护按钮文本值为：" + b)
        return b

    # 获取产品类型的值
    def get_product_type_text(self):
        b = self.text(ProjectBaseInfoLocator.product_type_text_loc)
        logger.debug("产品类型为：" + b)
        return b

    # 获取当前年份 月份
    def get_current_year_month(self):
        year = self.text(ElectronicArchivesLocator.current_year_loc)[0:4]
        month = self.text(ElectronicArchivesLocator.current_month_loc)[0:2]
        logger.debug("当前年份为：" + year + "，当前月份为：" + month)
        return int(year), int(month)

    # 点击新增项目按钮
    def click_add_project_button(self):
        self.click_element(ElectronicArchivesLocator.add_project_button_loc)
        self.logger.info("点击新增项目按钮")

    # 勾选第一条数据，删除
    def delete_first_project(self):
        self.refresh()
        time.sleep(1)
        self.click_element(ElectronicArchivesLocator.first_project_delete_button_loc)
        time.sleep(1)
        self.click_element(ElectronicArchivesLocator.confirm_delete_button_loc)
        time.sleep(1)
        self.logger.info("删除第一条数据")

    # 点击第一条数据的编辑按钮
    def _click_first_project_edit_button(self):
        time.sleep(1)
        self.click_element(ElectronicArchivesLocator.first_project_edit_button_loc)
        time.sleep(1)
        self.logger.info("点击第一条数据的编辑按钮")

    # 通过标签点击项目详细资料维护
    def _click_project_detail_info(self):
        self.click_element(ElectronicArchivesLocator.first_project_detail_button_loc)
        self.logger.info("点击项目详细资料维护")

    # 获取详情界面title
    def _get_project_detail_info_title(self):
        return self.text(ElectronicArchivesLocator.project_detail_info_title_loc)

    # 通过标签点击维护实施管理信息
    def _click_implementation_maintenance_info(self):
        self.click_element(ElectronicArchivesLocator.implementation_maintenance_info_loc)
        self.logger.info("点击维护实施管理信息")

    # 通过标签点击运维管理信息
    def _click_operation_management_info(self):
        self.click_element(ElectronicArchivesLocator.operation_management_info_loc)
        self.logger.info("点击运维管理信息")

    # 通过标签点击项目基础资料维护
    def _click_project_basic_info(self):
        self.click_element(ElectronicArchivesLocator.project_basic_info_loc)
        self.logger.info("点击项目基础资料维护")

    # 验证新增项目界面的页面切换
    def test_electronic_archives_05(self):
        self._click_implementation_maintenance_info()  # 维护实施管理信息
        self.random_sleep(0.5)
        self._click_project_basic_info()  # 项目基础资料维护
        self.random_sleep(0.5)
        self._click_project_detail_info()  # 项目详细资料维护
        self.random_sleep(0.5)
        self._click_operation_management_info()  # 运维管理信息
        self.random_sleep(0.5)
        self.click_previous_button()  # 3
        self.random_sleep(0.5)
        self.click_previous_button()  # 2
        self.random_sleep(0.5)
        self.click_previous_button()  # 1

    # 获取项目基础资料维护的页面标题状态
    def get_project_basic_info_title_status(self):
        b = self.get_attribute(ElectronicArchivesLocator.project_basic_info_status_loc, "class")
        logger.debug("项目基础资料维护的页面标题class状态为：" + b)
        return b

    # 获取编辑项目的页面名称
    def get_add_edit_project_title(self):
        return self.text(ElectronicArchivesLocator.edit_project_title_loc)

    # 点击第一个批量下载巡检码按钮
    def click_first_project_download_inspection_item_button(self):
        self.click_element(ElectronicArchivesLocator.first_project_download_inspection_item_button_loc)
        self.logger.info("点击第一个批量下载巡检码按钮")



    # 通过编辑，进入项目资料中点击批量下载巡检码按钮
    def test_electronic_archives_08_2(self):
        self.click_element(ElectronicArchivesLocator.first_project_execute_inspection_edit_button_loc)
        self.random_sleep(0.5)
        self._click_operation_management_info()
        self.random_sleep(0.5)
        self.click_element(ElectronicArchivesLocator.project_info_download_inspection_item_loc)
        self.random_sleep(0.5)


    # 通过点击第二页进行翻页

    def page_turning_by_click_page_2(self):
        if self.visibility_of_element_located(ElectronicArchivesLocator.page_2_loc, 5, 1):
            self.click_element(ElectronicArchivesLocator.page_2_loc)
            time.sleep(1)
        else:
            self.logger.info("第二页不存在")

    # 通过点击第一页进行翻页
    def page_turning_by_click_page_1(self):
        if self.visibility_of_element_located(ElectronicArchivesLocator.page_1_loc, 5, 1):
            self.click_element(ElectronicArchivesLocator.page_1_loc)
            time.sleep(1)
        else:
            self.logger.info("第一页不存在")
    # 点击下一页
    def page_turning_by_click_next_page(self):
        if self.visibility_of_element_located(ElectronicArchivesLocator.next_page_loc, 5, 1):
            self.click_element(ElectronicArchivesLocator.next_page_loc)
            time.sleep(1)
        else:
            self.logger.info("下一页不存在")

    # 点击上一页
    def page_turning_by_click_previous_page(self):
        if self.visibility_of_element_located(ElectronicArchivesLocator.previous_page_loc, 5, 1):
            self.click_element(ElectronicArchivesLocator.previous_page_loc)
            time.sleep(1)
        else:
            self.logger.info("上一页不存在")








