from selenium.webdriver.common.by import By


class ManagementRoleLocator:
    # 运维工作台 li元素的 class
    operation_and_maintenance_workbench_basic_loc = (
        By.XPATH,
        '//*[text()="运维工作台"]/../..',
    )
    # 运维工作台
    operation_and_maintenance_workbench = (By.XPATH, '//*[text()="运维工作台"]')
    # 在途项目看板
    in_transit_project_lookboard_loc = (By.XPATH, '//*[text()="在途项目看板"]')
    # 管理角色
    management_role_loc = (By.XPATH, '//*[text()="管理角色"]/../../..')
    # --------在途项目看板部分元素
    # 数据维度 选择框
    data_dimension_select_loc = (By.XPATH, '//*[@class="ant-select-selection-item"]')
    # 数据维度 项目类型项
    data_dimension_project_type_loc = (By.XPATH, '//*[text()="项目类型图"]')
    # 数据维度 项目阶段项
    data_dimension_project_stage_loc = (By.XPATH, '//*[text()="项目阶段图"]')

    # -------------------工单、任务部分元素
    # 在途 异常 工单

    abnormal_work_order_loc = (By.XPATH, '//*[text()="在途异常工单"]')
    # 在途异常工单 数量
    abnormal_work_order_number_loc = (
        By.XPATH,
        '//*[@title="在途异常工单"]/following-sibling::a',
    )
    # 在途其他工单
    abnormal_other_work_order_loc = (By.XPATH, '//*[text()="在途其他工单"]')
    # 在途其他工单 数量
    abnormal_other_work_order_number_loc = (
        By.XPATH,
        '//*[@title="在途其他工单"]/following-sibling::a',
    )
    # 发起工单数
    initiate_work_order_loc = (By.XPATH, '//*[text()="发起工单数"]')
    # 发起工单数 数量
    initiate_work_order_number_loc = (
        By.XPATH,
        '//*[@title="发起工单数"]/following-sibling::a',
    )
    # 已执行总数
    executed_work_order_loc = (By.XPATH, '//*[text()="已执行工单总数"]')
    # 已执行总数 数量
    executed_work_order_number_loc = (
        By.XPATH,
        '//*[@title="已执行总数"]/following-sibling::a',
    )
    # 待执行工单数
    pending_work_order_loc = (By.XPATH, '//*[text()="待执行工单数"]')
    # 待执行工单数 数量
    pending_work_order_number_loc = (
        By.XPATH,
        '//*[@title="待执行工单总数"]/following-sibling::a',
    )
    # 待执行异常工单
    pending_abnormal_work_order_loc = (By.XPATH, '//*[text()="待执行异常工单"]')
    # 待执行异常工单 数量
    pending_abnormal_work_order_number_loc = (
        By.XPATH,
        '//*[@title="待执行异常工单"]/following-sibling::a',
    )

    # 任务过程看板 周
    week_loc = (By.XPATH, '//*[text()="周"]')
    # 任务过程看板 月
    month_loc = (By.XPATH, '//*[text()="月"]')
    # 任务过程看板，断言元素
    week_or_month_assert_loc = (
        By.XPATH,
        '//*[@class="ant-radio-button"]/following-sibling::span',
    )

    # 实施工单
    implement_work_order_loc = (By.XPATH, '//*[text()="实施工单"]')
    # 运维工单
    operation_work_order_loc = (By.XPATH, '//*[text()="运维工单"]')

    # -----------------人员任务统计
    # 区域选择框
    area_select_loc = (By.XPATH, '//*[@class="ant-select-selection-overflow"]')
    # 区域 东部项
    area_east_loc = (By.XPATH, '//*[text()="东部"]')
    # 区域 西北项
    area_northwest_loc = (By.XPATH, '//*[text()="西北"]')
    # 区域 南方项
    area_south_loc = (By.XPATH, '//*[text()="南方"]')
    # 区域 海外项
    area_overseas_loc = (By.XPATH, '//*[text()="海外"]')
    # 区域 大储运维（宁夏）项
    area_big_storage_operation_loc = (By.XPATH, '//*[text()="大储运维（宁夏）"]')

    #  大储运维（宁夏）项X按钮
    #  //*[text()="大储运维（宁夏）"]/following-sibling::span
    area_big_storage_operation_close_loc = (
        By.XPATH,
        '//*[text()="大储运维（宁夏）"]/following-sibling::span',
    )

    # 区域 取消 全部选项 按钮
    area_cancel_all_loc = (By.XPATH, '(//*[@class="ant-select-clear"])[2]')

    # 时间维度
    time_dimension_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[3]')
    # 时间维度 年
    time_dimension_year_loc = (
        By.XPATH,
        '//*[text()="年" and @class="ant-select-item-option-content"]',
    )
    # 时间维度 月
    time_dimension_month_loc = (
        By.XPATH,
        '//*[text()="月" and @class="ant-select-item-option-content"]',
    )

    # 年 弹窗
    year_popup_loc = (By.XPATH, '//*[@placeholder="请选择年份"]')
