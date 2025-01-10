from selenium.webdriver.common.by import By


class SparePartManagementLocator:

    # 项目管理模块是否展开 //*[text()="项目管理"]/../..
    project_management_is_expand_loc = (By.XPATH, '//*[text()="项目管理"]/../..')

    # 项目管理
    project_management_loc = (By.XPATH, '//*[text()="项目管理"]')
    # 备件管理
    spare_part_management_loc = (By.XPATH, '//*[text()="备件管理"]/../..')

    # 全选复选框 //*[@aria-label="Select all"]
    spare_part_all_checkbox_loc = (By.XPATH, '(//*[@class="ant-checkbox-input"])[1]/..')
    # 第一个备件复选框  //*[@class="ant-checkbox-input"]
    first_spare_part_checkbox_loc = (
        By.XPATH,
        '(//*[@class="ant-checkbox-input"])[2]/..',
    )
    # 第二个备件复选框
    second_spare_part_checkbox_loc = (
        By.XPATH,
        '(//*[@class="ant-checkbox-input"])[3]/..',
    )

    # 第一个备件数量字段 //*[@class="ant-table-tbody"]/tr[2]/td[3]
    first_spare_part_number_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[4]',
    )
    # 第二个备件数量字段
    second_spare_part_number_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[3]/td[4]',
    )
    # 第三个备件数量字段
    third_spare_part_number_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[4]/td[4]',
    )

    # ----------搜索框 相关元素 ----------
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')
    # 备件名称输入框
    search_spare_part_name_input_loc = (By.XPATH, '//*[@placeholder="请输入备件名称"]')
    # 备件类型选择框
    search_spare_part_type_select_loc = (By.XPATH, '//*[text()="请选择备件类型"]/..')
    # 备件类型 第一个类型选项 //*[@class="rc-virtual-list-holder-inner"]/div
    search_spare_part_type_first_option_loc = (
        By.XPATH,
        '//*[@class="rc-virtual-list-holder-inner"]/div',
    )
    # 第一个备件的备件类型字段 //*[@class="ant-table-tbody"]/tr[2]/td[5]
    fitst_spare_part_type_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[5]',
    )
    # 第二个备件类型
    second_spare_part_type_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[3]/td[5]',
    )

    # 所属仓库选择框
    search_spare_part_warehouse_select_loc = (
        By.XPATH,
        '//*[text()="请选择所属仓库"]/..',
    )
    # 上海仓
    search_spare_part_warehouse_shanghai_loc = (
        By.XPATH,
        '//*[@title="上海备品仓" and @aria-selected]',
    )
    # 宁夏仓
    search_spare_part_warehouse_ningxia_loc = (
        By.XPATH,
        '//*[@title="宁夏备品仓" and @aria-selected]',
    )
    # 第一个备件的所属仓库
    first_spare_part_warehouse_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[6]',
    )

    # 查询条件 ：备件属性选择框
    search_spare_part_attribute_select_loc = (
        By.XPATH,
        '//*[text()="请选择备件属性"]/..',
    )
    # 备件属性 选择1 供应商预存备件
    search_spare_part_attribute_supplier_pre_spare_part_loc = (
        By.XPATH,
        '//*[@title="供应商预存备件" and @aria-selected]',
    )
    # 备件属性 选择2 采日自采备件
    search_spare_part_attribute_self_purchase_spare_part_loc = (
        By.XPATH,
        '//*[@title="采日自采备件" and @aria-selected]',
    )
    # 备件属性 选择3 采日自研备件
    search_spare_part_attribute_self_develop_spare_part_loc = (
        By.XPATH,
        '//*[@title="采日自研备件" and @aria-selected]',
    )

    # 第一个备件的备件属性字段
    first_spare_part_attribute_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[7]',
    )
    # 第二个备件的备件属性字段
    second_spare_part_attribute_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[3]/td[7]',
    )

    # 所属供应商选择框
    search_spare_part_supplier_select_loc = (
        By.XPATH,
        '//*[text()="请选择所属供应商"]/..',
    )
    # 所属供应商第一个选项
    # search_spare_part_supplier_first_option_loc = (By.XPATH, '(//*[@class="rc-virtual-list-holder-inner"])[4]/div/div')
    search_spare_part_supplier_first_option_loc = (
        By.XPATH,
        '//*[@class="ant-select-item-option-content" and text()]/..',
    )
    # first_spare_part_supplier_text_loc
    # 备件供应商字段
    first_spare_part_supplier_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[8]',
    )
    # 第二个备件供应商字段
    second_spare_part_supplier_text_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[3]/td[8]',
    )

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
    spare_part_inbound_title_loc = (
        By.XPATH,
        '//*[@class="ant-modal-title" and text()="备件入库"]',
    )
    # 新增备件
    add_spare_part_button_loc = (
        By.XPATH,
        '//*[text()="新增备件"]/preceding-sibling::span',
    )
    # 维护已有备件
    maintain_spare_part_button_loc = (
        By.XPATH,
        '//*[text()="维护已有备件"]/preceding-sibling::span',
    )
    # 第一个备件名称选项
    first_spare_part_name_option_loc = (
        By.XPATH,
        '//*[@class="rc-virtual-list-holder-inner"]/div',
    )

    # 备件属性选择框  id="attribute"
    fill_data_spare_part_attribute_select_loc = (By.XPATH, '//*[@id="attribute"]/..')
    # 备件属性 --供应商预存备件 //*[@title="供应商预存备件" and @aria-selected]
    supplier_pre_spare_part_option_loc = (
        By.XPATH,
        '//*[@title="供应商预存备件" and @aria-selected]',
    )
    # 备件属性 --采日自研备件
    self_developed_by_spare_part_option_loc = (
        By.XPATH,
        '//*[@title="采日自采备件" and @aria-selected]',
    )
    # 备件属性 --采日自采备件
    self_purchase_by_spare_part_option_loc = (
        By.XPATH,
        '//*[@title="采日自采备件" and @aria-selected]',
    )

    # 备件类型选择框 id="type"
    fill_data_spare_part_type_select_loc = (By.XPATH, '//*[@id="type"]/..')
    # 备件类型 --EMS类附件
    type_of_ems_option_loc = (By.XPATH, '//*[@title="EMS类附件" and @aria-selected]')
    # 备件类型 --PCS类附件
    type_of_pcs_option_loc = (By.XPATH, '//*[@title="PCS类附件" and @aria-selected]')
    # 备件类型 --变压器
    type_of_transformer_option_loc = (
        By.XPATH,
        '//*[@title="变压器" and @aria-selected]',
    )
    # 备件类型 --汇集交换机
    type_of_aggregation_switch_option_loc = (
        By.XPATH,
        '//*[@title="汇集交换机" and @aria-selected]',
    )
    # 备件类型 --BMU
    type_of_bmu_option_loc = (By.XPATH, '//*[@title="BMU" and @aria-selected]')
    # 备件类型 --高压箱
    type_of_high_voltage_box_option_loc = (
        By.XPATH,
        '//*[@title="高压箱" and @aria-selected]',
    )
    # 备件类型 --显示屏
    type_of_display_option_loc = (By.XPATH, '//*[@title="显示屏" and @aria-selected]')
    # 备件类型 --高压箱内附件
    type_of_high_voltage_box_attachment_option_loc = (
        By.XPATH,
        '//*[@title="高压箱内附件" and @aria-selected]',
    )
    # 备件类型 --汇流柜内附件
    type_of_aggregation_cabinet_attachment_option_loc = (
        By.XPATH,
        '//*[@title="汇流柜内附件" and @aria-selected]',
    )
    # 备件类型 --电芯
    type_of_cell_option_loc = (By.XPATH, '//*[@title="电芯" and @aria-selected]')
    # 备件类型 --电池模组内附件
    type_of_battery_module_attachment_option_loc = (
        By.XPATH,
        '//*[@title="电池模组内附件" and @aria-selected]',
    )
    # 备件类型 --液冷系统
    type_of_liquid_cooling_system_option_loc = (
        By.XPATH,
        '//*[@title="液冷系统" and @aria-selected]',
    )
    # 备件类型 --消防系统
    type_of_fire_protection_system_option_loc = (
        By.XPATH,
        '//*[@title="消防系统" and @aria-selected]',
    )
    # 备件类型 --动力线束
    type_of_power_harness_option_loc = (
        By.XPATH,
        '//*[@title="动力线束" and @aria-selected]',
    )
    # 备件类型 --通信线束
    type_of_communication_harness_option_loc = (
        By.XPATH,
        '//*[@title="通信线束" and @aria-selected]',
    )
    # 备件类型 --空调
    type_of_air_conditioner_option_loc = (
        By.XPATH,
        '//*[@title="空调" and @aria-selected]',
    )
    # 备件类型 --集装箱附件
    type_of_container_attachment_option_loc = (
        By.XPATH,
        '//*[@title="集装箱附件" and @aria-selected]',
    )
    # 备件类型 --熔断器
    type_of_fuse_option_loc = (By.XPATH, '//*[@title="熔断器" and @aria-selected]')
    # 备件类型 --采样线束
    type_of_sampling_harness_option_loc = (
        By.XPATH,
        '//*[@title="采样线束" and @aria-selected]',
    )
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
    warehouse_of_shanghai_option_loc = (
        By.XPATH,
        '//*[@title="上海备品仓" and @aria-selected]',
    )
    # 宁夏备品仓
    warehouse_of_nx_option_loc = (
        By.XPATH,
        '//*[@title="宁夏备品仓" and @aria-selected]',
    )

    # 备件名称输入框 id="name"
    fill_data_spare_part_name_input_loc = (By.XPATH, '//*[@id="name"]')
    # 维护备件名称选择框
    maintain_spare_part_name_select_loc = (By.XPATH, '//*[@id="name"]/..')
    # 备件数量 id="stock"
    fill_data_spare_part_number_input_loc = (By.XPATH, '//*[@id="stock"]')
    # 备件备注id="remark"
    fill_data_spare_part_remark_input_loc = (By.XPATH, '//*[@id="remark"]')
    # 入库备注 id="operateRemark"
    fill_data_spare_part_inbound_remark_input_loc = (
        By.XPATH,
        '//*[@id="operateRemark"]',
    )
    # 确认 按钮
    fill_data_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 取消 按钮
    fill_data_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # X 按钮
    fill_data_close_button_loc = (By.XPATH, '//*[@class="ant-modal-close"]')

    # 第一个备件名称 //*[@class="ant-table-tbody"]/tr[2]/td[2]/div
    first_spare_part_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[2]/div',
    )
    # 第二个备件名称
    second_spare_part_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[3]/td[2]/div',
    )

    # 页面提示信息元素
    page_tip_loc = (
        By.XPATH,
        '//*[@class="ant-message-notice-content"]/div/span[last()]',
    )

    # 第一个备件的查看出入库记录按钮  //*[text()="查看出入库记录"]/..
    first_spare_part_view_inbound_record_button_loc = (
        By.XPATH,
        '//*[text()="查看出入库记录"]/..',
    )

    # 出入库记录页面的title //*[ @class="ant-drawer-title" and text()="出入库记录"]
    spare_part_inbound_record_title_loc = (
        By.XPATH,
        '//*[ @class="ant-drawer-title" and text()="出入库记录"]',
    )
    # 出入库记录页面的关闭按钮 //*[@class="ant-drawer-close"]
    spare_part_inbound_record_close_button_loc = (
        By.XPATH,
        '//*[@class="ant-drawer-close"]',
    )

    # 第一个备件的备件领用按钮 //*[text()="备件领用"]/..
    first_spare_part_receive_button_loc = (By.XPATH, '//*[text()="备件领用"]/..')

    # 备件领用的确认按钮
    spare_part_receive_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 备件领用的取消按钮
    spare_part_receive_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # 备件领用的关闭按钮
    spare_part_receive_close_button_loc = (By.XPATH, '//*[@class="ant-modal-close"]')
    # 备件领用页面的title //*[ @class="ant-modal-title" and text()="备件领用"]
    spare_part_receive_title_loc = (
        By.XPATH,
        '//*[ @class="ant-modal-title" and text()="备件领用"]',
    )

    # 备件领用数量输入框
    spare_part_receive_number_input_loc = (By.XPATH, '//*[@id="count"]')
    # 备件领用项目选择框 id="outputProjectId"
    spare_part_receive_project_select_loc = (By.XPATH, '//*[@id="outputProjectId"]/..')
    # 备件领用项目列表 第一个 备件领用项目 //*[@class="rc-virtual-list-holder-inner"]/div
    spare_part_receive_project_first_option_loc = (
        By.XPATH,
        '//*[@class="rc-virtual-list-holder-inner"]/div',
    )
    # 备件领用备注输入框 id="remark"
    spare_part_receive_remark_input_loc = (By.XPATH, '//*[@id="remark"]')
    # 备件领用备注库存数量
    spare_part_receive_stock_number_loc = (By.XPATH, '//*[@id="stock"]')

    # 第二页 //*[@title="2"]
    second_page_loc = (By.XPATH, '//*[@title="2"]')
    # 第一页
    first_page_loc = (By.XPATH, '//*[@title="1"]')
    # 上一页 //*[@title="上一页"]
    previous_page_loc = (By.XPATH, '//*[@title="上一页"]')
    # 下一页 //*[@title="下一页"]
    next_page_loc = (By.XPATH, '//*[@title="下一页"]')
