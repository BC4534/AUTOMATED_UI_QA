from selenium.webdriver.common.by import By


class WorkOrderListLocator:
    # 工单管理界面是否展开
    work_order_management_expand_loc = (By.XPATH, '//*[text()="工单管理"]/../..')
    # 工单管理 模块按钮
    work_order_management_loc = (By.XPATH, '//*[text()="工单管理"]')
    # 工单列表 页面
    work_order_list_loc = (By.XPATH, '//*[text()="工单列表"]/../..')

    # ----搜索框相关元素
    # 工单类型
    work_order_type_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[3]')
    # 工单类型 系统异常工单
    system_abnormal_work_order_loc = (By.XPATH, '//*[@title="系统异常工单"]')
    # 工单类型 手工异常工单
    manual_abnormal_work_order_loc = (By.XPATH, '//*[@title="手工异常工单"]')
    # 工单类型 定期标准巡检工单
    regular_standard_inspection_work_order_loc = (By.XPATH, '//*[@title="定期标准巡检工单"]')
    # 工单类型 手工标准巡检工单
    manual_standard_inspection_work_order_loc = (By.XPATH, '//*[@title="手工标准巡检工单"]')
    # 工单类型 手工非标巡检工单
    manual_non_standard_inspection_work_order_loc = (By.XPATH, '//*[@title="手工非标巡检工单"]')
    # 工单类型 手工其他工单
    other_work_order_loc = (By.XPATH, '//*[@title="手工其他工单"]')
    # 工大类型 实施工单
    implement_work_order_loc = (By.XPATH, '//*[@title="实施工单"]')

    # 工单发起人
    initiator_of_work_order_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[5]')
    # 工单发起人 系统管理员
    initiator_of_work_order_system_administrator_loc = (By.XPATH, '//*[@title="系统管理员"]')

    # 处理状态 选择框
    handle_status_loc = (By.XPATH, '(//*[@class="ant-select-selector"])')
    # 处理状态 已完成
    handle_status_completed_loc = (By.XPATH, '//*[@title="已完成"]')
    # 未完成
    handle_status_unfinished_loc = (By.XPATH, '//*[@title="未完成"]')

    # 发布时间 展开框的 前一年按钮
    previous_year_button_loc = (By.XPATH, '//*[@class="ant-picker-header-super-prev-btn"]')
    # 后一年按钮
    next_year_button_loc = (By.XPATH, '(//*[@class="ant-picker-header-super-next-btn"])[2]')
    # 计划开始时间 后一年按钮
    plan_time_next_year_button_loc = (By.XPATH, '//*[@class="ant-picker-header-super-next-btn"]')
    # 前一个月按钮
    previous_month_button_loc = (By.XPATH, '//*[@class="ant-picker-header-prev-btn"]')
    # 后一个月按钮
    next_month_button_loc = (By.XPATH, '(//*[@class="ant-picker-header-next-btn"])[2]')
    # 计划开始时间后一个月按钮
    plan_time_next_month_button_loc = (By.XPATH, '(//*[@class="ant-picker-header-next-btn"])')
    # 当前开始时间页 1号按钮
    start_time_1_button_loc = (By.XPATH, '//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="1"]')
    # 开始时间页面，28号按钮
    start_time_28_button_loc = (By.XPATH, '//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="28"]')

    # 结束页面 1号按钮
    end_time_1_button_loc = (By.XPATH, '(//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="1"])[2]')
    # 结束页面 28号按钮
    end_time_28_button_loc = (By.XPATH, '(//*[@class="ant-picker-cell ant-picker-cell-in-view"]/div[text()="28"])[2]')

    # 发布时间的时间页面展开/清除已填时间 loc
    clear_time_button_loc = (By.XPATH, '//*[@fill-rule="evenodd"]')
    # 发布时间展开
    publish_time_expand_button_loc = (By.XPATH, '//*[text()="发布时间："]/following-sibling::div')

    # 处理状态 选择框
    handle_status_select_loc = (By.XPATH, '//*[text()="处理状态"]/following-sibling::div')
    # 未完成
    handle_status_unfinished_loc = (By.XPATH, '//*[text()="未完成" and @class="ant-select-item-option-content"]')
    # 已完成
    handle_status_finished_loc = (By.XPATH, '//*[text()="已完成" and @class="ant-select-item-option-content"]')

    # 工单编号输入框
    work_order_number_input_loc = (By.XPATH, '//*[text()="工单编号"]/following-sibling::span/input')
    # 第一条数据的处理状态文本
    first_data_handle_status_loc = (
    By.XPATH, '//*[@class="ant-table-cell-fix-right ant-table-cell-fix-right-first"]/div')
    # 搜索查询界面 工单名称输入框
    select_work_order_name_input_loc = (By.XPATH, '//*[text()="工单名称"]/following-sibling::span/input')
    # 搜索界面，关联项目选择框
    select_association_project_select_loc = (By.XPATH, '//*[text()="关联项目"]/following-sibling::div/div/span')
    # 搜索界面，关联项目文本
    select_association_project_text_loc = (By.XPATH, '//*[text()="关联项目"]/following-sibling::div/div/span[2]')
    # 关联项目 第一个选项
    association_project_first_option_loc = (By.XPATH, '(//*[@class="ant-select-item-option-content"])[3]')
    # 搜搜计划开始时间按钮
    plan_start_time_button_loc = (By.XPATH, '//*[text()="计划开始时间："]/following-sibling::div/div/input')
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')
    # 搜索 计划结束时间
    plan_end_time_button_loc = (By.XPATH, '//*[text()="计划结束时间："]/following-sibling::div/div/input')
    # 手工新增工单按钮
    manual_add_work_order_loc = (By.XPATH, '//*[text()="手工新增工单"]')
    # 删除工单按钮
    delete_work_order_loc = (By.XPATH, '//*[text()="删除工单"]')
    # ------------------新增工单界面 元素
    # 工单类型 选择框
    # work_order_type_select_loc = (By.XPATH, '//*[@id="basic_createType"]')
    work_order_type_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[8]')
    # 工单类型 巡检工单项
    work_order_type_inspection_loc = (By.XPATH, '//*[text()="巡检工单"]')
    # 工单类型 其他工单项
    work_order_type_other_loc = (By.XPATH, '//*[text()="其他工单"]')
    # 工单类型 异常工单项
    work_order_type_abnormal_loc = (By.XPATH, '//*[text()="异常工单"]')
    # 工单名称输入框
    work_order_name_input_loc = (By.XPATH, '//*[@id="basic_title"]')
    # 工单描述输入框
    work_order_description_input_loc = (By.XPATH, '//*[@id="basic_description"]')
    #  关联项目选择框
    association_project_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[9]')
    # 关联项目 第一个项目
    association_project_first_loc = (By.XPATH, '(//*[@class="rc-virtual-list-holder-inner"])[2]/div')
    # 负责人选择框
    responsible_person_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[10]')
    # 负责人 第一个负责人 系统管理员
    responsible_person_first_loc = (By.XPATH, '(//*[@class="rc-virtual-list-holder-inner"])[3]/div')
    # 计划开始时间
    plan_start_time_loc = (By.XPATH, '//*[@id="basic_planStartDate"]')
    # 计划结束时间
    plan_end_time_loc = (By.XPATH, '//*[@id="basic_planEndDate"]')
    #  计划开始时间 此刻
    plan_start_time_now_loc = (By.XPATH, '//*[text()="此刻"]')
    # 计划结束时间 此刻
    plan_end_time_now_loc = (By.XPATH, '(//*[text()="此刻"])[2]')
    # 必填项效验相关元素
    # 工单类型必填项提示
    work_order_type_required_loc = (By.XPATH, '//*[@class="ant-form-item-explain-error"]')
    # 工单名称必填项提示
    work_order_name_required_loc = (By.XPATH, '(//*[@class="ant-form-item-explain-error"])[2]')
    # 工单描述必填项提示
    work_order_description_required_loc = (By.XPATH, '(//*[@class="ant-form-item-explain-error"])[3]')
    # 关联项目必填项提示
    association_project_required_loc = (By.XPATH, '(//*[@class="ant-form-item-explain-error"])[4]')
    # 负责人必填项提示
    responsible_person_required_loc = (By.XPATH, '(//*[@class="ant-form-item-explain-error"])[5]')
    # 计划开始时间必填项提示
    plan_start_time_required_loc = (By.XPATH, '(//*[@class="ant-form-item-explain-error"])[6]')
    # 计划结束时间必填项提示
    plan_end_time_required_loc = (By.XPATH, '(//*[@class="ant-form-item-explain-error"])[7]')

    # 确认按钮
    confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 取消按钮
    cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # X按钮
    close_button_loc = (By.XPATH, '//*[@aria-label="close"]')

    # 全选按钮
    select_all_loc = (By.XPATH, '//*[@type="checkbox"]/parent::span')
    # 未选中状态 第2条数据复选框
    second_data_checkbox_loc = (By.XPATH, '(//*[@class="ant-checkbox ant-wave-target css-1hzb5nd"])[2]')
    # 未选中状态 第1条数据复选框
    first_data_checkbox_loc = (By.XPATH, '(//*[@class="ant-checkbox ant-wave-target css-1hzb5nd"])')

    # 界面提示弹窗
    page_tip_loc = (By.XPATH, '//*[@class="ant-message-notice-content"]/div/span[2]')
    # 第一条工单编号
    first_work_order_number_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[2]')
    # 第一条数据的详情按钮
    first_data_detail_button_loc = (By.XPATH, '//*[text()="详情"]')
    # 详情界面的X按钮
    detail_close_button_loc = (By.XPATH, '(//*[@fill-rule="evenodd"])[last()]')
    # 第一条数据的工单名称文本
    first_data_work_order_name_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[3]')
    # 第一条数据的处理状态文本
    first_data_handle_status_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[4]')
    # 第一条数据的发布时间
    first_data_publish_time_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[5]')
    # 第一条数据的关联项目
    first_data_association_project_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[6]')
    # 第一条数据的工单类型
    first_data_work_order_type_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[6]')
    # 第一条数据的所属区域
    first_data_area_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[8]')
    # 第一条数据的计划开始时间
    first_data_plan_start_time_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[9]')
    # 第一条数据的计划结束时间
    first_data_plan_end_time_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[10]')
    # 第一条数据的工单发起人
    first_data_initiator_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[11]')
    # 第一条数据的工单接受人
    first_data_responsible_person_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[12]')
    # 第一条数据的当前处理人
    first_data_current_handler_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[13]')
    # 第一条数据的实际处理人
    first_data_actual_handler_loc = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]/td[14]')

    # 勾选复选框后 展示勾选数量元素
    checkbox_number_loc = (By.XPATH, '//*[text()="删除工单"]/following-sibling::*')
