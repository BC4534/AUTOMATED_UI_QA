from selenium.webdriver.common.by import By


class SparePartManagementLocator():
    # 项目管理
    project_management_loc = (By.XPATH, '//*[text()="项目管理"]')
    # 备件管理
    spare_part_management_loc = (By.XPATH, '//*[text()="备件管理"]')

    # ----------搜索框 相关元素 ----------
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')
    # 备件名称输入框
    spare_part_name_input_loc = (By.XPATH, '//*[@placeholder="请输入备件名称"]')
    # 备件类型选择框1
    spare_part_type_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[1]')
    # 所属仓库选择框
    warehouse_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[2]')
    # 备件属性选择框
    spare_part_attribute_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[3]')
    # 所属供应商选择框
    vendor_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[4]')

    # -------------
    # 备件入库按钮
    spare_part_inbound_button_loc = (By.XPATH, '//*[text()="备件入库"]')
    # 删除备件按钮
    delete_spare_part_button_loc = (By.XPATH, '//*[text()="删除备件"]')

    # 备件领用按钮
    spare_part_receive_button_loc = (By.XPATH, '//*[text()="备件领用"]')
    # 查看出入库按钮
    check_in_out_button_loc = (By.XPATH, '//*[text()="查看出入库"]')

    # --------------------新增备件界面按钮
    # 备件属性
    spare_part_attribute_loc = (By.XPATH, '//*[@class="ant-select-selection-item"]')
    # 备件类型
    spare_part_type_loc = (By.XPATH, '//*[@class="ant-select-selection-item"]')
    # 所属供应商
    vendor_loc = (By.XPATH, '//*[@class="ant-select-selection-item"]')
    # 所属仓库
    warehouse_loc = (By.XPATH, '//*[@class="ant-select-selection-item"]')
    # 备件名称
    spare_part_name_loc = (By.XPATH, '//*[@placeholder="请输入备件名称"]')
    # 备件数量
    spare_part_number_loc = (By.XPATH, '//*[@placeholder="请输入备件数量"]')
    # 备件备注
    spare_part_remark_loc = (By.XPATH, '//*[@placeholder="请输入备件备注"]')
    # 入库备注
    inbound_remark_loc = (By.XPATH, '//*[@placeholder="请输入入库备注"]')
    # 确认 按钮
    confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 取消 按钮
    cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # X 按钮
    close_button_loc = (By.XPATH, '//*[@class="ant-modal-close"]')


