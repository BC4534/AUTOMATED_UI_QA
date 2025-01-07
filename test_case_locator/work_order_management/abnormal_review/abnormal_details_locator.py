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
    # 判断是否在异常明细界面 //*[text()="异常明细"]/..
    abnormal_detail_class_loc = (By.XPATH, '//*[text()="异常明细"]/..')

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


    # ----------------- 界面操作相关 -----------------
    #异常统计 展开合并按钮 //*[@class="upDownIcon___xrlxN"]
    abnormal_statistic_expand_button_loc = (By.XPATH, '//*[@class="upDownIcon___xrlxN"]')
    # 是否展开判断元素 //*[@class="upDownIcon___xrlxN"]/preceding-sibling::*
    abnormal_statistic_expand_button_judge_loc = (By.XPATH, '//*[@class="upDownIcon___xrlxN"]/preceding-sibling::*')

    # 附件弹框界面标题 id=":r7c:"
    attachment_dialog_title_loc = (By.ID, ':r7c:')
    # 附件弹框界面关闭按钮 //*[@class="ant-modal-close"]
    attachment_dialog_close_button_loc = (By.XPATH, '//*[@class="ant-modal-close"]')
    # 附件弹框界面附件确定按钮
    attachment_dialog_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]/..')
    # 附件弹框界面附件取消按钮
    attachment_dialog_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]/..')
    # 第一个工单的附件按钮 //span[text()="附件"]/..
    first_work_order_attachment_button_loc = (By.XPATH, '//span[text()="附件"]/..')
    # 第一个工单的详情按钮 //span[text()="详情"]/..
    first_work_order_details_button_loc = (By.XPATH, '//span[text()="详情"]/..')
    # 第一个工单的编号 //*[@class="ant-table-tbody"]/tr[2]/td[1]
    first_work_order_number_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[1]')
    # 第二个工单编号
    second_work_order_number_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[1]')
    # 第一个工单的异常名称
    first_work_order_abnormal_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[2]')
    # 第二个工单的异常名称
    second_work_order_abnormal_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[2]')

    # 第一个工单关联项目
    first_work_order_relation_project_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[5]')
    # 第二个工单关联项目
    second_work_order_relation_project_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[5]')

    # 第一个工单的关联工单类型
    first_work_order_relation_work_order_type_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[6]')

    # 第一个工单的异常部件
    first_work_order_abnormal_part_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[6]')
    # 第二个工单的异常部件
    second_work_order_abnormal_part_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[6]')

    # 第一个工单的责任厂商
    first_work_order_responsible_vendor_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[7]')

    # 第二个工单的责任厂商
    second_work_order_responsible_vendor_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[7]')

    # 工单列表界面的详情 # 第一条数据的详情按钮
    work_order_list_details_button_loc = (By.XPATH, '//*[text()="详情"]')
    # 是否需要领用/采购备件或耗材 //*[text()="是否领用/采购备件或耗材"]/following::span
    is_purchase_loc = (By.XPATH, '//*[text()="是否领用/采购备件或耗材"]/following::span')
    # 详情界面的X按钮
    detail_close_button_loc = (By.XPATH, '(//*[@fill-rule="evenodd"])[last()]')


    # 第一个工单的异常处理人
    first_work_order_abnormal_processing_person_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[20]')
    # 第二个工单的异常处理人
    second_work_order_abnormal_processing_person_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[20]')