from selenium.webdriver.common.by import By


class MyAlreadyDoneLocator():
    # 工单管理
    work_order_management_loc = (By.XPATH, '//*[text()="工单管理"]')
    # 工单列表
    work_order_list_loc = (By.XPATH, '//*[text()="工单列表"]')
    # 我的工单
    my_work_order_loc = (By.XPATH, '//*[text()="我的工单"]')
    # 我的已办接
    my_already_done_loc = (By.XPATH, '//*[text()="我的已办"]')


    # -----------搜索框相关
    # 工单类型
    work_order_type_loc = (By.XPATH, '(//*[@class="ant-select-selector"])')
    # 工单类型 -系统异常工单
    system_abnormal_work_order_loc = (By.XPATH, '//*[@title="系统异常工单"]')
    # 工单类型 - 手工异常工单
    manual_abnormal_work_order_loc = (By.XPATH, '//*[@title="手工异常工单"]')

    # 处理状态
    handle_status_loc = (By.XPATH, '(//*[@class="ant-select-selector"])')