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
    project_time_select_loc = (By.XPATH, '//*[text()="立项时间："]/following::input[@placeholder="请选择日期"]')
    # 立项时间 - 前一年
    project_time_last_year_loc = (By.XPATH, '//*[@title="前一年"]')
    # 立项时间 - 后一年
    project_time_next_year_loc = (By.XPATH, '//*[@title="后一年"]')
    # 立项时间 -前一月
    project_time_last_month_loc = (By.XPATH, '//*[@title="前一月"]')
    # 立项时间 -后一月
    project_time_next_month_loc = (By.XPATH, '//*[@title="后一月"]')
    # 立项时间 - 今天
    project_time_today_loc = (By.XPATH, '//*[text()="今天"]')
    # 当前所选年份
    current_year_loc = (By.XPATH, '//*[@class="ant-picker-year-btn"]')
    # 当前所选月份
    current_month_loc = (By.XPATH, '//*[@class="ant-picker-month-btn"]')


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

    # 保存
    save_button_loc = (By.XPATH, '//*[text()="保 存"]')
    # 下一步
    next_button_loc = (By.XPATH, '//*[text()="下一步"]')
    # 上一步
    previous_button_loc = (By.XPATH, '//*[text()="上一步"]')
    # 提交
    submit_button_loc = (By.XPATH, '//*[text()="提 交"]')

    # 第一个项目编辑按钮
    first_project_edit_button_loc = (By.XPATH, '//*[text()="编辑"]')
    # 第一个项目删除按钮
    first_project_delete_button_loc = (By.XPATH, '//*[text()="删除"]')
    # 第一个项目详情按钮
    first_project_detail_button_loc = (By.XPATH, '//*[text()="详情"]')
    # 第一个项目批量下载巡检项按钮
    first_project_download_inspection_item_button_loc = (By.XPATH, '//*[text()="批量下载巡检码"]')
    # 第一个执行巡检的编辑按钮
    first_project_execute_inspection_edit_button_loc = (By.XPATH, '//*[@class="ant-table-measure-row"]/following::span[text()="是"]/following::a[text()="编辑"]')
    # 项目资料里面的批量下载巡检码 //*[text()="巡检组管理"]/following::span[text()="批量下载巡检码"]
    project_info_download_inspection_item_loc = (By.XPATH, '//*[text()="巡检组管理"]/following::span[text()="批量下载巡检码"]')

    # 确认删除按钮
    confirm_delete_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 取消删除按钮
    cancel_delete_button_loc = (By.XPATH, '//*[text()="取 消"]')

    # 页面提示信息 //*[@class="ant-message-notice-content"]/div/span[last()]
    page_tip_loc = (By.XPATH, '//*[@class="ant-message-notice-content"]/div/span[last()]')
    # page_tip_loc = (By.XPATH, '//*[@aria-label="check-circle"]/following::span')




    # 第一个项目名称
    first_project_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td')
    # 第二个项目名称
    second_project_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td')
    # 第一个项目立项时间
    first_project_init_time_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[3]')
    # 第二个项目立项时间
    second_project_init_time_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[3]')
    # 当前年 //*[@class="ant-picker-header-view"]/button[1]
    current_year_value_loc = (By.XPATH, '//*[@class="ant-picker-header-view"]/button[1]')
    # 当前月 //*[@class="ant-picker-header-view"]/button[2]
    current_month_value_loc = (By.XPATH, '//*[@class="ant-picker-header-view"]/button[2]')
    # 前一年按钮 //*[@class="ant-picker-header-super-prev-btn"]
    previous_year_button_loc = (By.XPATH, '//*[@class="ant-picker-header-super-prev-btn"]')
    # 后一年按钮 class="ant-picker-header-super-next-btn"
    next_year_button_loc = (By.XPATH, '//*[@class="ant-picker-header-super-next-btn"]')
    # 前一月按钮 //*[@class="ant-picker-header-prev-btn"]
    previous_month_button_loc = (By.XPATH, '//*[@class="ant-picker-header-prev-btn"]')
    # 后一月按钮 //*[@class="ant-picker-header-next-btn"]
    next_month_button_loc = (By.XPATH, '//*[@class="ant-picker-header-next-btn"]')

    # 第一个项目所属区域
    first_project_area_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[10]')
    # 第二个项目所属区域
    second_project_area_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[10]')


    # 项目基础资料维护
    project_basic_info_loc = (By.XPATH, '//*[text()="项目基础资料维护"]')
    # 项目详细资料维护
    project_detail_info_loc = (By.XPATH, '//*[text()="项目详细资料维护"]')
    # 维护实施管理信息
    implementation_maintenance_info_loc = (By.XPATH, '//*[text()="维护实施管理信息"]')
    # 运维管理信息
    operation_management_info_loc = (By.XPATH, '//*[text()="运维管理信息"]')

    # 项目基础资料维护 状态判断
    project_basic_info_status_loc = (By.XPATH, '//*[@class="ant-modal-body"]/div/div[1]')
    # 项目详细资料维护 状态判断
    project_detail_info_status_loc = (By.XPATH, '//*[@class="ant-modal-body"]/div/div[2]')
    # 维护实施管理信息 状态判断
    implementation_maintenance_info_status_loc = (By.XPATH, '//*[@class="ant-modal-body"]/div/div[3]')
    # 运维管理信息 状态判断
    operation_management_info_status_loc = (By.XPATH, '//*[@class="ant-modal-body"]/div/div[4]')

    # 获取项目详情页面的title  //*[@class="ant-modal-title"]/div/div[2]
    edit_project_title_loc = (By.XPATH, '//*[@class="ant-modal-title"]/div/div[2]')



    # 获取项目详情页面的title  //*[@class="ant-drawer-header-title"]
    project_detail_info_title_loc = (By.XPATH, '//*[@class="ant-drawer-header-title"]/div')

    # X按钮 //*[@class="anticon anticon-close"]
    close_button_loc = (By.XPATH, '//*[@class="anticon anticon-close"]')







