from selenium.webdriver.common.by import By


class SparePartManagementLocator():

    # 项目管理模块是否展开 //*[text()="项目管理"]/../..
    project_management_is_expand_loc = (By.XPATH, '//*[text()="项目管理"]/../..')

    # 项目管理
    project_management_loc = (By.XPATH, '//*[text()="项目管理"]')
    # 备件管理
    spare_part_management_loc = (By.XPATH, '//*[text()="备件管理"]/../..')

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
    # 查询条件 ：备件属性选择框

    # spare_part_attribute_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[3]')
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
    # 备件入库界面的标题
    spare_part_inbound_title_loc = (By.XPATH, '//*[@class="ant-modal-title" and text()="备件入库"]')
    # 新增备件
    add_spare_part_button_loc = (By.XPATH, '//*[text()="新增备件"]/preceding-sibling::span')
    # 维护已有备件
    maintain_spare_part_button_loc = (By.XPATH, '//*[text()="维护已有备件"]/preceding-sibling::span')
    # 备件属性选择框  id="attribute"
    fill_data_spare_part_attribute_select_loc = (By.XPATH, '//*[@id="attribute"]/..')
    # 备件属性 --供应商预存备件 //*[@title="供应商预存备件" and @aria-selected]
    supplier_pre_spare_part_option_loc = (By.XPATH, '//*[@title="供应商预存备件" and @aria-selected]')
    # 备件属性 --采日自研备件
    self_developed_by_spare_part_option_loc = (By.XPATH, '//*[@title="采日自采备件" and @aria-selected]')
    # 备件属性 --采日自采备件
    self_purchase_by_spare_part_option_loc = (By.XPATH, '//*[@title="采日自采备件" and @aria-selected]')


    # 备件类型选择框 id="type"
    fill_data_spare_part_type_select_loc = (By.XPATH, '//*[@id="type"]/..')
    # 备件类型 --EMS类附件
    type_of_ems_option_loc = (By.XPATH, '//*[@title="EMS类附件" and @aria-selected]')
    # 备件类型 --PCS类附件
    type_of_pcs_option_loc = (By.XPATH, '//*[@title="PCS类附件" and @aria-selected]')
    # 备件类型 --变压器
    type_of_transformer_option_loc = (By.XPATH, '//*[@title="变压器" and @aria-selected]')
    # 备件类型 --汇集交换机
    type_of_aggregation_switch_option_loc = (By.XPATH, '//*[@title="汇集交换机" and @aria-selected]')
    # 备件类型 --BMU
    type_of_bmu_option_loc = (By.XPATH, '//*[@title="BMU" and @aria-selected]')
    # 备件类型 --高压箱
    type_of_high_voltage_box_option_loc = (By.XPATH, '//*[@title="高压箱" and @aria-selected]')
    # 备件类型 --显示屏
    type_of_display_option_loc = (By.XPATH, '//*[@title="显示屏" and @aria-selected]')
    # 备件类型 --高压箱内附件
    type_of_high_voltage_box_attachment_option_loc = (By.XPATH, '//*[@title="高压箱内附件" and @aria-selected]')
    # 备件类型 --汇流柜内附件
    type_of_aggregation_cabinet_attachment_option_loc = (By.XPATH, '//*[@title="汇流柜内附件" and @aria-selected]')
    # 备件类型 --电芯
    type_of_cell_option_loc = (By.XPATH, '//*[@title="电芯" and @aria-selected]')
    # 备件类型 --电池模组内附件
    type_of_battery_module_attachment_option_loc = (By.XPATH, '//*[@title="电池模组内附件" and @aria-selected]')
    # 备件类型 --液冷系统
    type_of_liquid_cooling_system_option_loc = (By.XPATH, '//*[@title="液冷系统" and @aria-selected]')
    # 备件类型 --消防系统
    type_of_fire_protection_system_option_loc = (By.XPATH, '//*[@title="消防系统" and @aria-selected]')
    # 备件类型 --动力线束
    type_of_power_harness_option_loc = (By.XPATH, '//*[@title="动力线束" and @aria-selected]')
    # 备件类型 --通信线束
    type_of_communication_harness_option_loc = (By.XPATH, '//*[@title="通信线束" and @aria-selected]')
    # 备件类型 --空调
    type_of_air_conditioner_option_loc = (By.XPATH, '//*[@title="空调" and @aria-selected]')
    # 备件类型 --集装箱附件
    type_of_container_attachment_option_loc = (By.XPATH, '//*[@title="集装箱附件" and @aria-selected]')
    # 备件类型 --熔断器
    type_of_fuse_option_loc = (By.XPATH, '//*[@title="熔断器" and @aria-selected]')
    # 备件类型 --采样线束
    type_of_sampling_harness_option_loc = (By.XPATH, '//*[@title="采样线束" and @aria-selected]')
    # 备件类型 --UPS
    type_of_ups_option_loc = (By.XPATH, '//*[@title="UPS" and @aria-selected]')
    # 备件类型 --接触器
    type_of_contact_option_loc = (By.XPATH, '//*[@title="接触器" and @aria-selected]')
    # 备件类型列表
    type_list_option_loc = (By.XPATH, '//*[@id="type_list"]/../..')

    # 所属供应商id="supplierId"
    fill_data_vendor_select_loc = (By.XPATH, '//*[@id="supplierId"]/..')
    # 第一个供应商
    first_vendor_option_loc = (By.XPATH, '//*[@id="supplierId_list"]/div')
    # 供应商列表元素  class="rc-virtual-list-holder-inner"
    vendor_list_option_loc = (By.XPATH, '//*[@id="supplierId_list"]/..')


    # 所属仓库 id="warehouse"
    fill_data_warehouse_select_loc = (By.XPATH, '//*[@id="warehouse"]/..')
    # 上海备品仓
    warehouse_of_shanghai_option_loc = (By.XPATH, '//*[@title="上海备品仓" and @aria-selected]')
    # 宁夏备品仓
    warehouse_of_nx_option_loc = (By.XPATH, '//*[@title="宁夏备品仓" and @aria-selected]')


    # 备件名称输入框 id="name"
    fill_data_spare_part_name_input_loc = (By.XPATH, '//*[@id="name"]')
    # 备件数量 id="stock"
    fill_data_spare_part_number_input_loc = (By.XPATH, '//*[@id="stock"]')
    # 备件备注id="remark"
    fill_data_spare_part_remark_input_loc = (By.XPATH, '//*[@id="remark"]')
    # 入库备注 id="operateRemark"
    fill_data_spare_part_inbound_remark_input_loc = (By.XPATH, '//*[@id="operateRemark"]')
    # 确认 按钮
    fill_data_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 取消 按钮
    fill_data_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # X 按钮
    fill_data_close_button_loc = (By.XPATH, '//*[@class="ant-modal-close"]')

    # 第一个备件名称 //*[@class="ant-table-tbody"]/tr[2]/td[2]/div
    first_spare_part_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[2]/div')

    # 页面提示信息元素
    page_tip_loc = (By.XPATH, '//*[@class="ant-message-notice-content"]/div/span[last()]')






