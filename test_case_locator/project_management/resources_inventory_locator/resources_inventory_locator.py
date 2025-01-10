from selenium.webdriver.common.by import By


class ResourcesInventoryLocator(object):
    """
    人力资源复盘页面元素定位
    """

    # 项目管理模块是否展开 //*[text()="项目管理"]/../..
    project_management_is_expand_loc = (By.XPATH, '//*[text()="项目管理"]/../..')

    # 项目管理
    project_management_loc = (By.XPATH, '//*[text()="项目管理"]')

    # 人力资源复盘
    resources_inventory_loc = (By.XPATH, '//*[text()="人力资源复盘"]/../..')

    # ================查询相关
    # 人员名称输入框 placeholder="请输入人员名称"
    resources_inventory_name_input_loc = (
        By.XPATH,
        '//*[@placeholder="请输入人员名称"]',
    )

    # 所属区域选择框
    resources_inventory_area_select_loc = (By.XPATH, '//*[text()="请选择所属区域"]/..')
    # 所属区域选择框选项 - 东部
    resources_inventory_area_option_east_loc = (By.XPATH, '//*[@title="东部"]')
    # 所属区域选择框选项 - 西北
    resources_inventory_area_option_northwest_loc = (By.XPATH, '//*[@title="西北"]')
    # 所属区域选择框选项 - 大储运维(宁夏)
    resources_inventory_area_option_northwest_nx_loc = (
        By.XPATH,
        '//*[@title="大储运维（宁夏）"]',
    )
    # 所属区域选择框选项 - 南方
    resources_inventory_area_option_south_loc = (By.XPATH, '//*[@title="南方"]')
    # 所属区域选择框选项 - 海外
    resources_inventory_area_option_west_loc = (By.XPATH, '//*[@title="海外"]')

    # 搜索按钮
    resources_inventory_search_button_loc = (By.XPATH, '//*[text()="搜 索"]/..')
    # 重置按钮
    resources_inventory_reset_button_loc = (By.XPATH, '//*[text()="重 置"]/..')
    # 第一个人员名称
    resources_inventory_first_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[1]',
    )
    # 第一个所属区域
    resources_inventory_first_area_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[2]',
    )
    # 第二个人员名称
    resources_inventory_second_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[1]',
    )
    # 第二个所属区域
    resources_inventory_second_area_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[2]',
    )

    # 确定按钮
    resources_inventory_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]/..')
    # 取消按钮
    resources_inventory_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]/..')
    # 关闭按钮
    resources_inventory_close_button_loc = (
        By.XPATH,
        '//*[@role="dialog"]//button[@aria-label="Close"]',
    )

    # 展开显示的项目名称字段  //*[@class="ant-table-cell"and text()="项目名称"]
    resources_inventory_project_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-cell"and text()="项目名称"]',
    )
    # 展开显示的工单名字段  //*[@class="ant-table-cell"and text()="工单名称"]
    resources_inventory_work_order_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-cell"and text()="工单名称"]',
    )

    # 第一个负责项目总数字段
    resources_inventory_first_project_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[3]/span',
    )
    # 第一个实施阶段项目数字段
    resources_inventory_first_implementation_project_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[4]/span',
    )
    # 第一个售后质保项目数字段
    resources_inventory_first_after_sales_warranty_project_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[5]/span',
    )
    # 第一个售后过保项目数字段
    resources_inventory_first_after_sales_expired_project_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[6]/span',
    )
    # 第一个处理任务总数字段
    resources_inventory_first_task_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[7]/span',
    )
    # 第一个处理实施工单数字段
    resources_inventory_first_implementation_work_order_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[8]/span',
    )
    # 第一个处理巡检工单数字段
    resources_inventory_first_inspection_work_order_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[9]/span',
    )
    # 第一个处理异常工单数字段
    resources_inventory_first_abnormal_work_order_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[10]/span',
    )
    # 第一个待办工单数字段
    resources_inventory_first_pending_work_order_count_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[1]/td[11]/span',
    )
