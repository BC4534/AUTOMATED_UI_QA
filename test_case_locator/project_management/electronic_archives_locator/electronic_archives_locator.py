from selenium.webdriver.common.by import By


class ElectronicArchivesLocator:
    # 项目管理模块
    project_management_module_class_attributes_loc = (By.XPATH, '//*[text()="项目管理"]/../..')
    # 项目管理
    project_management_loc = (By.XPATH, '//*[text()="项目管理"]')
    # 电子档案
    electronic_archives_loc = (By.XPATH, '//*[text()="电子档案"]')

    #==================搜索功能======================
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')
    # 是否支持巡检标准
    # 是否支持巡检标准-是
    is_support_inspection_standard_yes_loc = (By.XPATH, '//*[@title="是"]')
    # 是否支持巡检标准-否
    is_support_inspection_standard_no_loc = (By.XPATH, '//*[@title="否"]')
    # 项目名称输入框
    project_name_input_loc = (By.XPATH, '//*[@placeholder="请输入项目名称"]')
    # 立项时间选择框
    project_time_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 立项时间 - 前一年
    project_time_last_year_loc = (By.XPATH, '//*[@title="前一年"]')
    # 立项时间 - 后一年
    project_time_next_year_loc = (By.XPATH, '//*[@title="后一年"]')
    # 立项时间 -前一月
    project_time_last_month_loc = (By.XPATH, '//*[@title="前一月"]')
    # 立项时间 -后一月
    project_time_next_month_loc = (By.XPATH, '//*[@title="后一月"]')
    # 立项时间 - 今天
    project_time_today_loc = (By.XPATH, '//*[@title="今天"]')

    # 工单所属区域选择框
    work_order_area_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 工单所属区域 - 东部
    work_order_area_east_loc = (By.XPATH, '//*[@title="东部"]')
    # 工单所属区域 - 西北
    work_order_area_northwest_loc = (By.XPATH, '//*[@title="西北"]')
    # 工单所属区域 - 大储运维（宁夏）
    work_order_area_ningxia_loc = (By.XPATH, '//*[@title="大储运维（宁夏）"]')
    # 工单所属区域 - 南方
    work_order_area_south_loc = (By.XPATH, '//*[@title="南方"]')
    # 工单所属区域 - 海外
    work_order_area_overseas_loc = (By.XPATH, '//*[@title="海外"]')

    # 项目阶段选择框
    project_stage_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 项目阶段 - 待实施阶段
    project_stage_wait_for_implementation_loc = (By.XPATH, '//*[@title="待实施阶段"]')
    # 项目阶段 - 实施阶段
    project_stage_implementation_loc = (By.XPATH, '//*[@title="实施阶段"]')
    # 项目阶段 -售后阶段
    project_stage_after_sale_loc = (By.XPATH, '//*[@title="售后阶段"]')

    # 项目进度 待实施阶段（计划期）、实施阶段（准备期、发货期、并网、调试期、试运行）、售后阶段（质保期、已过保）、全部；默认全部
    project_progress_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 项目进度 - 待实施阶段（计划期）
    project_progress_wait_for_implementation_loc = (By.XPATH, '//*[@title="待实施阶段（计划期）"]')
    # 项目进度 - 实施阶段（准备期）
    project_progress_implementation_preparation_loc = (By.XPATH, '//*[@title="实施阶段（准备期）"]')

    # 项目类型 选择框
    project_type_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 项目类型 - 工商业
    project_type_commercial_loc = (By.XPATH, '//*[@title="商用"]')
    # 项目类型 - 电网侧
    project_type_electricity_side_loc = (By.XPATH, '//*[@title="电网侧"]')
    # 项目类型 - 电源侧
    project_type_power_side_loc = (By.XPATH, '//*[@title="电源侧"]')

    # 产品类型 选择框
    product_type_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 产品类型 -户外柜
    product_type_outdoor_cabinet_loc = (By.XPATH, '//*[@title="户外柜"]')
    # 产品类型 - 集装箱
    product_type_container_loc = (By.XPATH, '//*[@title="集装箱"]')
    # 产品类型 - 非系统
    product_type_non_system_loc = (By.XPATH, '//*[@title="非系统"]')
    # 实施负责人选择框
    implementation_responsible_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 实施负责人 --根据名字定位
    # implementation_responsible_loc = (By.XPATH, f'//*[@title="{}"]')
    # 运维负责人
    operation_responsible_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 状态 选择框
    status_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 状态 - 草稿
    status_draft_loc = (By.XPATH, '//*[@title="草稿"]')
    # 状态 - 已生效
    status_effective_loc = (By.XPATH, '//*[@title="已生效"]')

    # ======================查询结束====================
    #=======================主界面元素====================
    # 新增项目按钮
    add_project_button_loc = (By.XPATH, '//*[text()="新增项目"]')

    # 供应商维护按钮
    supplier_maintenance_button_loc = (By.XPATH, '//*[text()="供应商维护"]')











