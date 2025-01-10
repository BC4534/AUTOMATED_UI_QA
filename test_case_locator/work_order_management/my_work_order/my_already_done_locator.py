from selenium.webdriver.common.by import By


class MyAlreadyDoLocator:
    # 工单管理界面是否展开
    work_order_management_expand_loc = (By.XPATH, '//*[text()="工单管理"]/../..')
    # 工单管理 模块按钮
    work_order_management_loc = (By.XPATH, '//*[text()="工单管理"]')
    # 我的工单
    my_work_order_loc = (By.XPATH, '//*[text()="我的工单"]/../..')
    # 我的待办
    my_need_to_do_loc = (By.XPATH, '//*[text()="我的待办"]')
    # 我的已办
    my_already_do_loc = (By.XPATH, '//*[text()="我的已办"]')

    # -----------搜索框相关
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]/..')
    # 点击重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]/..')
    # 工单编号输入框
    work_order_number_input_loc = (
        By.XPATH,
        '//*[text()="工单编号"]/following::span/input',
    )
    # 工单发布时间选择框
    work_order_release_time_select_loc = (
        By.XPATH,
        '//*[text()="工单发布时间"]/following::span/input',
    )
    # 工单名称输入框
    work_order_name_input_loc = (
        By.XPATH,
        '//*[text()="工单名称"]/following::span/input',
    )
    # 工单类型下拉框
    work_order_type_select_loc = (By.XPATH, '//*[text()="工单类型"]/following::div')
    # 定期标准巡检工单
    regular_standard_inspection_work_order_loc = (
        By.XPATH,
        '//*[@title="定期标准巡检工单"]',
    )
    # 手工标准巡检工单
    manual_standard_inspection_work_order_loc = (
        By.XPATH,
        '//*[@title="手工标准巡检工单"]',
    )
    # 实施工单
    implement_work_order_loc = (By.XPATH, '//*[@title="实施工单"]')
    # 系统异常工单
    system_exception_work_order_loc = (By.XPATH, '//*[@title="系统异常工单"]')
    # 手工异常工单
    manual_exception_work_order_loc = (By.XPATH, '//*[@title="手工异常工单"]')
    # 手工非标准巡检工单
    manual_non_standard_inspection_work_order_loc = (
        By.XPATH,
        '//*[@title="手工非标准巡检工单"]',
    )
    # 手工其他工单
    manual_other_work_order_loc = (By.XPATH, '//*[@title="手工其他工单"]')
    # 关联项目选择框
    association_project_select_loc = (By.XPATH, '//*[text()="关联项目"]/following::div')
    # 计划开始日期输入框
    plan_start_date_input_loc = (
        By.XPATH,
        '//*[text()="计划开始时间："]/following::div',
    )
    # 计划结束日期输入框
    plan_end_date_input_loc = (By.XPATH, '//*[text()="计划结束时间："]/following::div')
    # 工单所属区域选择框
    work_order_belong_area_select_loc = (
        By.XPATH,
        '//*[text()="工单所属区域"]/following::div',
    )
    # 工单所属区域选择框-东部
    work_order_belong_area_east_loc = (By.XPATH, '//*[@title="东部"]')
    # 工单所属区域选择框-西北
    work_order_belong_area_northwest_loc = (By.XPATH, '//*[@title="西北"]')
    # 工单所属区域选择框-南方
    work_order_belong_area_south_loc = (By.XPATH, '//*[@title="南方"]')
    # 工单所属区域选择框-海外
    work_order_belong_area_overseas_loc = (By.XPATH, '//*[@title="海外"]')
    # 工单所属区域选择框-大储运维（宁夏）
    work_order_belong_area_nx_loc = (By.XPATH, '//*[@title="大储运维（宁夏）"]')
    # 工单发起人下拉框
    work_order_initiator_select_loc = (
        By.XPATH,
        '//*[text()="工单发起人"]/following::div',
    )

    # 工单接收人选择框
    work_order_receiver_select_loc = (
        By.XPATH,
        '//*[text()="工单接收人"]/following::div',
    )
    # 当前处理人选择框
    current_handler_select_loc = (By.XPATH, '//*[text()="当前处理人"]/following::div')

    # 第一个工单的工单接收人
    first_work_order_receiver_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[11]',
    )
    # 第一个工单的当前处理人
    first_work_order_current_handler_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[12]',
    )
