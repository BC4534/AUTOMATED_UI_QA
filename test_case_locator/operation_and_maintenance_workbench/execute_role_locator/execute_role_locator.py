from selenium.webdriver.common.by import By

class ExecuteRoleLocator:
    # 运维工作台基本元素
    operation_and_maintenance_workbench_basic_loc = (By.XPATH, '//*[text()="运维工作台"]/../..')
    # 运维工作台
    operation_and_maintenance_workbench = (By.XPATH, '//*[text()="运维工作台"]')
    # 在途项目看板
    in_transit_project_lookboard_loc = (By.XPATH, '//*[text()="在途项目看板"]')
    # 执行角色
    execute_role_loc = (By.XPATH, '//*[text()="执行角色"]/../../..')

    # --------在途项目看板部分元素
    # 数据维度 选择框
    data_dimension_select_loc = (By.XPATH, '//*[@class="ant-select-selection-item"]')
    # 数据维度 项目类型项
    data_dimension_project_type_loc = (By.XPATH, '//*[text()="项目类型图"]')
    # 数据维度 项目阶段项
    data_dimension_project_stage_loc = (By.XPATH, '//*[text()="项目阶段图"]')

    # ----------我的代办部分元素
    # 工单总数 数量
    work_order_number_loc = (By.XPATH, '//*[text()="工单总数"]/following-sibling::a')
    # 已执行工单  数量
    executed_work_order_number_loc = (By.XPATH, '//*[text()="已执行工单"]/following-sibling::a')
    # 待执行工单  数量
    pending_work_order_number_loc = (By.XPATH, '//*[text()="待执行工单"]/following-sibling::a')


    # 任务过程看板 周
    week_loc = (By.XPATH, '//*[text()="周"]')
    # 任务过程看板 月
    month_loc = (By.XPATH, '//*[text()="月"]')
    # 任务过程看板，断言元素
    week_or_month_assert_loc = (By.XPATH, '//*[@class="ant-radio-button"]/following-sibling::span')


    # ----------负责项目统计
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
    area_big_storage_operation_close_loc = (By.XPATH, '//*[text()="大储运维（宁夏）"]/following-sibling::span')

    # 区域 取消 全部选项 按钮
    area_cancel_all_loc = (By.XPATH, '(//*[@aria-label="close-circle"])[2]')

