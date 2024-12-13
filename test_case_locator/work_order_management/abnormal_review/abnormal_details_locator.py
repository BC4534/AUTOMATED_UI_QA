from selenium.webdriver.common.by import By


class AbnormalDetailsLocator:
    # 工单管理
    work_order_management_loc = (By.XPATH, '//*[text()="工单管理"]')
    # 异常复盘
    abnormal_review_loc = (By.XPATH, '//*[text()="异常复盘"]')
    # 异常统计
    abnormal_statistic_loc = (By.XPATH, '//*[text()="异常统计"]')
    # 异常明细
    abnormal_detail_loc = (By.XPATH, '//*[text()="异常明细"]')

    # ----------------- 查询条件相关 -----------------
    # 工单编号输入框  //*[@placeholder="请输入工单编号"] valus是输入的值
    work_order_number_input_loc = (By.XPATH, '//*[@placeholder="请输入工单编号"]')


    # 异常名称输入框
    abnormal_name_input_loc = (By.XPATH, '//*[@placeholder="请输入异常名称"]')
    # 关联项目下拉框
    relation_project_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[1]')
    # 关联工单类型
    relation_work_order_type_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[2]')
    # 异常部件下拉框
    abnormal_part_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[3]')
    # 责任厂商下拉框
    responsible_vendor_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[4]')
    # 是否领用/采购备件或耗材 下拉框
    is_purchase_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[5]')
    # 异常处理人 下拉框
    abnormal_processing_person_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[6]')

    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')


