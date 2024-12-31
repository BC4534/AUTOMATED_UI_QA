from common.loggerhandler import logger
from test_case_locator.project_management.electronic_archives_locator.add_project_locator import ProjectBaseInfoLocator
from test_case_page.project_management.electronic_archives_page.electronic_archives_page import ElectronicArchivesPage


class AddProjectBaseInfoPage(ElectronicArchivesPage):



    # 新增项目 填写项目基础资料信息
    def fill_basic_information(self, init_time: str, project_name, project_install_power
                               , project_install_capacity,
                               project_stage, project_progress, project_type, product_type
                               , outdoor_cabinet_type, project_area, is_support_inspection):
        self.input_init_time(init_time)  # 选择立项时间
        self.input_project_name(project_name)  # 输入项目名称
        self.input_project_install_power(project_install_power)  # 输入项目装机功率
        self.input_project_install_capacity(project_install_capacity)  # 输入项目装机容量
        self.select_project_stage(project_stage)  # 选择项目阶段
        self.select_project_progress(project_progress)  # 选择项目进度
        self.select_project_type(project_type)  # 选择项目类型
        self.select_product_type(product_type)  # 选择产品类型
        self.select_outdoor_cabinet_type(outdoor_cabinet_type)  # 选择户外柜规格
        self.select_project_area(project_area)  # 选择所属区域
        self.is_support_inspection_standard(is_support_inspection)  # 选择是否支持巡检标准

    # 选择立项时间
    def input_init_time(self, init_time):
        # 点击立项时间
        self.click_element(ProjectBaseInfoLocator.project_time_select_loc)
        # 选择时间  逻辑处理比较复杂，先都是选择今天
        if init_time != " ":
            if len(init_time) != 8:
                logger.error("输入的立项时间格式不正确，默认选择今天")
                self.click_element(ProjectBaseInfoLocator.project_time_today_loc)
            else:
                year = init_time[0:4]
                month = init_time[4:6]
                day = init_time[6:]
                self.click_element(ProjectBaseInfoLocator.project_time_today_loc)
        else:
            self.click_element(ProjectBaseInfoLocator.project_time_today_loc)
            logger.info("立项时间未填，默认选择今天")
        self.random_sleep(0.5)

    # 输入项目名称
    def input_project_name(self, project_name):
        # 输入项目名称
        self.send_keys_by_clear(ProjectBaseInfoLocator.project_name_input_loc, project_name)
        self.random_sleep(0.5)

    # 输入项目装机功率
    def input_project_install_power(self, project_install_power):
        # 输入项目装机功率
        self.send_keys_by_clear(ProjectBaseInfoLocator.project_install_power_input_loc, project_install_power)
        self.random_sleep(0.5)

    # 输入项目装机容量
    def input_project_install_capacity(self, project_install_capacity):
        # 输入项目装机容量
        self.send_keys_by_clear(ProjectBaseInfoLocator.project_install_capacity_input_loc, project_install_capacity)
        self.random_sleep(0.5)

    # 选择项目阶段
    def select_project_stage(self, project_stage):
        # 选择项目阶段
        self.click_element(ProjectBaseInfoLocator.project_stage_select_loc)
        if project_stage != " ":
            if project_stage == "待实施阶段":
                self.driver.execute_script("document.getElementById('basic_phase').click();")
                self.click_element(ProjectBaseInfoLocator.project_stage_wait_for_implementation_loc)
                logger.debug("选择项目阶段为：待实施阶段")
            elif project_stage == "实施阶段":
                self.click_element(ProjectBaseInfoLocator.project_stage_implementation_loc)
                logger.debug("选择项目阶段为：实施阶段")
            elif project_stage == "售后阶段":
                self.click_element(ProjectBaseInfoLocator.project_stage_after_sale_loc)
                logger.debug("选择项目阶段为：售后阶段")
            else:
                logger.error("输入的项目阶段不正确，默认选择待实施阶段")
                self.click_element(ProjectBaseInfoLocator.project_stage_wait_for_implementation_loc)
            self.random_sleep(0.5)
        else:
            logger.info("项目阶段未填，默认选择待实施阶段")
            self.click_element(ProjectBaseInfoLocator.project_stage_wait_for_implementation_loc)

    # 选择项目进度
    def select_project_progress(self, project_progress):
        self.click_element(ProjectBaseInfoLocator.project_progress_select_loc)
        if project_progress != " ":
            if project_progress == "计划期":
                self.click_element(ProjectBaseInfoLocator.project_progress_plan_loc)
            elif project_progress == "准备期":
                self.click_element(ProjectBaseInfoLocator.project_progress_preparation_loc)
            elif project_progress == "发货期":
                self.click_element(ProjectBaseInfoLocator.project_progress_send_out_goods_loc)
            elif project_progress == "调试期":
                self.click_element(ProjectBaseInfoLocator.project_progress_debug_loc)
            elif project_progress == "试运行":
                self.click_element(ProjectBaseInfoLocator.project_progress_test_run_loc)
            elif project_progress == "质保期":
                self.click_element(ProjectBaseInfoLocator.project_progress_warranty_loc)
            elif project_progress == "已过保":
                self.click_element(ProjectBaseInfoLocator.project_progress_warranty_expired_loc)
            else:
                logger.error("输入的项目进度不正确，默认选择计划期")
                self.click_element(ProjectBaseInfoLocator.project_progress_plan_loc)
        else:
            logger.info("项目进度未填，默认选择计划期")
            self.click_element(ProjectBaseInfoLocator.project_progress_plan_loc)
        self.random_sleep(0.5)

    # 选择项目类型
    def select_project_type(self, project_type):
        # 项目类型
        self.click_element(ProjectBaseInfoLocator.project_type_select_loc)
        if project_type != " ":
            if project_type == "工商业":
                self.click_element(ProjectBaseInfoLocator.project_type_commercial_loc)
            elif project_type == "电源侧":
                self.click_element(ProjectBaseInfoLocator.project_type_power_side_loc)
            elif project_type == "电网侧":
                self.click_element(ProjectBaseInfoLocator.project_type_electricity_side_loc)
            else:
                logger.error("输入的项目类型不正确，默认选择工商业")
                self.click_element(ProjectBaseInfoLocator.project_type_commercial_loc)
        self.random_sleep(0.5)

    # 选择憨批类型
    def select_product_type(self, product_type):
        # 产品类型
        self.click_element(ProjectBaseInfoLocator.product_type_select_loc)
        if product_type != " ":
            if product_type == "户外柜":
                self.click_element(ProjectBaseInfoLocator.product_type_outdoor_cabinet_loc)
            elif product_type == "集装箱":
                self.click_element(ProjectBaseInfoLocator.product_type_container_loc)
            elif product_type == "非系统":
                self.click_element(ProjectBaseInfoLocator.product_type_non_system_loc)
            else:
                logger.error("输入的产品类型不正确，默认选择户外柜")
                self.click_element(ProjectBaseInfoLocator.product_type_outdoor_cabinet_loc)

    # 选择户外柜类型
    def select_outdoor_cabinet_type(self, outdoor_cabinet_type):
        if self.get_product_type_text() == "户外柜":
            self.click_element(ProjectBaseInfoLocator.outdoor_cabinet_type_select_loc)
            if outdoor_cabinet_type != " ":  # 215户外柜国标1.0 215户外柜国标2.0 232户外柜
                if outdoor_cabinet_type == "215户外柜国标1.0":
                    self.click_element(ProjectBaseInfoLocator.outdoor_cabinet_type_215_gb1_0_loc)
                elif outdoor_cabinet_type == "215户外柜国标2.0":
                    self.click_element(ProjectBaseInfoLocator.outdoor_cabinet_type_215_gb2_0_loc)
                elif outdoor_cabinet_type == "232户外柜":
                    self.click_element(ProjectBaseInfoLocator.outdoor_cabinet_type_232_loc)
                else:
                    logger.error("输入 outdoor_cabinet_type不正确，默认选择215户外柜国标1.0")
                    self.click_element(ProjectBaseInfoLocator.outdoor_cabinet_type_215_gb1_0_loc)
            else:
                logger.info("产品类型为户外柜，outdoor_cabinet_type未填，默认选择215户外柜国标1.0")
                self.click_element(ProjectBaseInfoLocator.outdoor_cabinet_type_215_gb1_0_loc)
            self.random_sleep(0.5)

    # 选择所属区域
    def select_project_area(self, project_area):
        # 所属区域
        self.click_element(ProjectBaseInfoLocator.project_area_select_loc)
        if project_area != " ":
            if project_area == "东部":
                self.click_element(ProjectBaseInfoLocator.project_area_east_loc)
            elif project_area == "西北":
                self.click_element(ProjectBaseInfoLocator.project_area_northwest_loc)
            elif project_area == "南方":
                self.click_element(ProjectBaseInfoLocator.project_area_south_loc)
            elif project_area == "海外":
                self.click_element(ProjectBaseInfoLocator.project_area_overseas_loc)
            elif project_area == "大储运维（宁夏）":
                self.click_element(ProjectBaseInfoLocator.project_area_ningxia_loc)
            else:
                logger.error("输入的所属区域不正确，默认选择东部")
                self.click_element(ProjectBaseInfoLocator.project_area_east_loc)
        else:
            logger.info("所属区域未填，默认选择东部")
            self.click_element(ProjectBaseInfoLocator.project_area_east_loc)
        self.random_sleep(0.5)

    # 选择是否执行巡检标准
    def is_support_inspection_standard(self, is_support_inspection):
        # 选择是否支持巡检标准
        if is_support_inspection != " ":
            if is_support_inspection == "是":
                self.click_element(ProjectBaseInfoLocator.is_support_inspection_standard_yes_loc)
            elif is_support_inspection == "否":
                self.click_element(ProjectBaseInfoLocator.is_support_inspection_standard_no_loc)
            else:
                # 巡检标准 默认选择是
                logger.info("是否支持巡检标准填写错误，默认选择是")
                self.click_element(ProjectBaseInfoLocator.is_support_inspection_standard_yes_loc)
        else:
            logger.info("是否支持巡检标准未填，默认选择是")
            self.click_element(ProjectBaseInfoLocator.is_support_inspection_standard_yes_loc)

    # 必填项提示信息
    # 获取立项时间必填项
    def get_init_time_required_text(self):
        return self.text(ProjectBaseInfoLocator.init_time_required_text_loc)

    # 获取项目名称必填项提示信息
    def get_project_name_required_text(self):
        return self.text(ProjectBaseInfoLocator.project_name_required_text_loc)

    # 获取项目装机功率必填项提示信息
    def get_project_install_power_required_text(self):
        return self.text(ProjectBaseInfoLocator.project_install_power_required_text_loc)

    # 获取项目装机容量必填项提示信息
    def get_project_install_capacity_required_text(self):
        return self.text(ProjectBaseInfoLocator.project_install_capacity_required_text_loc)

    # 获取项目阶段必填项提示信息
    def get_project_stage_required_text(self):
        return self.text(ProjectBaseInfoLocator.project_stage_required_text_loc)

    # 获取项目进度必填项提示信息
    def get_project_progress_required_text(self):
        return self.text(ProjectBaseInfoLocator.project_progress_required_text_loc)

    # 获取项目类型必填项提示信息
    def get_project_type_required_text(self):
        return self.text(ProjectBaseInfoLocator.project_type_required_text_loc)

    # 获取产品类型必填项提示信息
    def get_product_type_required_text(self):
        return self.text(ProjectBaseInfoLocator.product_type_required_text_loc)

    # 获取户外柜类型必填项提示信息
    def get_outdoor_cabinet_type_required_text(self):
        return self.text(ProjectBaseInfoLocator.outdoor_cabinet_type_required_text_loc)

    # 获取所属区域必填项提示信息
    def get_project_area_required_text(self):
        return self.text(ProjectBaseInfoLocator.project_area_required_text_loc)

    # 获取是否支持巡检标准必填项提示信息
    def get_is_support_inspection_standard_required_text(self):
        return self.text(ProjectBaseInfoLocator.is_support_inspection_standard_required_text_loc)

    #
