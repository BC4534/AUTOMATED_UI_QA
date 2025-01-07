from selenium.webdriver.common.by import By


class OutdoorCabinetAlarmConfigurationLocator:
    # 项目管理模块是否展开 //*[text()="项目管理"]/../..
    project_management_is_expand_loc = (By.XPATH, '//*[text()="项目管理"]/../..')
    # 项目管理
    project_management_loc = (By.XPATH, '//*[text()="项目管理"]')
    # 项目告警配置
    project_alarm_configuration_loc = (By.XPATH, '//*[text()="项目告警配置"]/../..')
    # 大储告警配置
    container_alarm_configuration_loc = (By.XPATH, '//*[text()="大储告警配置"]/..')
    # 户外柜告警配置
    outdoor_cabinet_alarm_configuration_loc = (By.XPATH, '//*[text()="户外柜告警配置"]/..')
    # 批量导出按钮
    batch_export_button_loc = (By.XPATH, '//*[text()="批量导出"]/..')
    # 批量更新按钮
    batch_update_button_loc = (By.XPATH, '//*[text()="批量更新"]/..')
    # 批量更新界面的确定按钮
    batch_update_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]/..')
    # 批量更新界面的取消按钮
    batch_update_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]/..')
    # 批量更新界面的关闭按钮
    batch_update_close_button_loc = (By.XPATH, '//*[@aria-label="close"]')
    # 下一页 //*[contains(@class,"ant-pagination-next")and @title="下一页"]
    next_page_loc = (By.XPATH, '//*[contains(@class,"ant-pagination-next")and @title="下一页"]')
    # 上一页 //*[contains(@class,"ant-pagination-prev")and @title="上一页"]
    previous_page_loc = (By.XPATH, '//*[contains(@class,"ant-pagination-prev")and @title="上一页"]')
    # 第二页
    second_page_loc = (By.XPATH, '//*[@title="2"]')
    # 第一页
    first_page_loc = (By.XPATH, '//*[@title="1"]')

    # 第一个告警的编辑按钮
    first_alarm_edit_button_loc = (By.XPATH, '//*[text()="编辑"]/..')
    # 编辑界面的title id=":r1f:"
    edit_title_loc = (By.XPATH, '//*[@id=":r1f:"]')
    # 编辑界面的确定按钮
    edit_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]/..')
    # 编辑界面的取消按钮
    edit_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]/..')
    # 编辑界面的关闭按钮
    edit_close_button_loc = (By.XPATH, '//*[@aria-label="close"]')
    # 编辑界面 - 运维告警类型
    edit_operation_alarm_type_select_loc = (By.XPATH, '//*[@title="运维告警类型"]/following::div[@class="ant-select-selector"]')
    # 运维告警类型必填提示信息 //*[@id="mmsEventClassify_help"]/div
    edit_operation_alarm_type_required_message_loc = (By.XPATH, '//*[@id="mmsEventClassify_help"]/div')
    # 告警类型 内容
    edit_operation_alarm_type_content_loc = (By.XPATH, '//*[@title="运维告警类型"]/following::span[@class="ant-select-selection-item"]')
    # 告警类型 -EMS
    edit_operation_alarm_type_ems_loc = (By.XPATH, '//*[@title="EMS"]')
    # 告警类型 -PCS
    edit_operation_alarm_type_pcs_loc = (By.XPATH, '//*[@title="PCS"]')
    # 告警类型 - BMS
    edit_operation_alarm_type_bms_loc = (By.XPATH, '//*[@title="BMS"]')
    # 告警类型-液冷系统
    edit_operation_alarm_type_liquid_cooling_system_loc = (By.XPATH, '//*[@title="液冷系统"]')
    # 告警类型-消防系统
    edit_operation_alarm_type_fire_system_loc = (By.XPATH, '//*[@title="消防系统"]')
    # 告警类型-集装箱类
    edit_operation_alarm_type_container_loc = (By.XPATH, '//*[@title="集装箱类"]')

    # 运维告警等级
    edit_operation_alarm_level_select_loc = (By.XPATH, '//*[@title="运维告警等级"]/following::div[@class="ant-select-selector"]')
    # 告警等级 一级
    edit_operation_alarm_level_first_loc = (By.XPATH, '//*[@title="一级"]')
    # 告警等级 二级
    edit_operation_alarm_level_second_loc = (By.XPATH, '//*[@title="二级"]')
    # 告警等级 三级
    edit_operation_alarm_level_third_loc = (By.XPATH, '//*[@title="三级"]')
    # 告警等级 四级
    edit_operation_alarm_level_fourth_loc = (By.XPATH, '//*[@title="四级"]')
    # 运维告警描述 输入框 id="mmsEventDesc"
    edit_operation_alarm_description_input_loc = (By.XPATH, '//*[@id="mmsEventDesc"]')
    # 是否告警-是//*[@class="ant-radio-input" and @value="true"]
    edit_is_alarm_yes_radio_loc = (By.XPATH, '//*[@class="ant-radio-input" and @value="true"]')

    # 是否告警-否//*[@class="ant-radio-input" and @value="false"]
    edit_is_alarm_no_radio_loc = (By.XPATH, '//*[@class="ant-radio-input" and @value="false"]')

    # 是否自动生成工单 是
    edit_is_auto_generate_work_order_yes_radio_loc = (By.XPATH, '(//*[@class="ant-radio-input" and @value="true"])[2]')
    # 是否自动生成工单 否
    edit_is_auto_generate_work_order_no_radio_loc = (By.XPATH, '(//*[@class="ant-radio-input" and @value="false"])[2]')

    # 查询相关 =============================================================================================
    # 第一个告警的设备名称  //*[@class="ant-table-body"]//tr[2]/td
    first_alarm_device_name_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[1]')
    # 第二个告警的设备名称
    second_alarm_device_name_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[3]/td[1]')
    # 第一个告警的户外柜规格
    first_alarm_outdoor_cabinet_specification_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[2]')
    # 第二个告警的户外柜规格
    second_alarm_outdoor_cabinet_specification_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[3]/td[2]')
    # 第一个告警的告警名称
    first_alarm_alarm_name_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[3]')
    # 第二个告警的告警名称
    second_alarm_alarm_name_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[3]/td[3]')
    # 第一个告警的告警描述
    first_alarm_alarm_description_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[5]')
    # 第二个告警的告警描述
    second_alarm_alarm_description_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[3]/td[5]')
    # 第一个告警的告警类型
    first_alarm_alarm_type_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[6]')
    # 第二个告警的告警类型
    second_alarm_alarm_type_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[3]/td[6]')
    # 第一个告警的告警等级
    first_alarm_alarm_level_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[7]')
    # 第二个告警的告警等级
    second_alarm_alarm_level_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[3]/td[7]')
    # 第一个告警的告警是否自动生成工单
    first_alarm_is_auto_create_work_order_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[9]')
    # 第一个告警的最后修改人
    first_alarm_last_modifier_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[10]')
    # 第二个告警的最后修改人
    second_alarm_last_modifier_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[3]/td[10]')
    # 第一个是否告警
    first_alarm_is_alarm_loc = (By.XPATH, '//*[@class="ant-table-body"]//tr[2]/td[8]')
    # 查询
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]/..')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]/..')
    # 设备名称输入框
    search_device_name_input_loc = (By.XPATH, '//*[@placeholder="请输入设备名称"]')
    # 户外柜规格选择框
    search_outdoor_cabinet_specification_select_loc = (By.XPATH, '//*[text()="请选择户外柜规格"]/..')
    # 户外柜规格 215户外柜国标1.0 //*[@title="215户外柜国标1.0"]
    search_outdoor_cabinet_specification_215_1_loc = (By.XPATH, '//*[@title="215户外柜国标1.0"]')
    # 户外柜规格 215户外柜国标2.0 //*[@title="215户外柜国标2.0"]
    search_outdoor_cabinet_specification_215_2_loc = (By.XPATH, '//*[@title="215户外柜国标2.0"]')
    # 户外柜规格 232户外柜
    search_outdoor_cabinet_specification_232_loc = (By.XPATH, '//*[@title="232户外柜"]')
    #  户外柜规格 372户外柜
    search_outdoor_cabinet_specification_372_loc = (By.XPATH, '//*[@title="372户外柜"]')
    # 告警名称查询条件输入框
    search_alarm_name_input_loc = (By.XPATH, '//*[@placeholder="请输入告警名称"]')
    # 告警描述查询条件输入框
    search_alarm_description_input_loc = (By.XPATH, '//*[@placeholder="请输入运维告警描述"]')
    # 运维告警类型选择框
    search_alarm_type_select_loc = (By.XPATH, '//*[text()="请选择运维告警类型"]/..')
    # 告警类型-EMS
    search_alarm_type_ems_loc = (By.XPATH, '//*[@title="EMS"]')
    # 告警类型-PCS
    search_alarm_type_pcs_loc = (By.XPATH, '//*[@title="PCS"]')
    # 告警类型-BMS
    search_alarm_type_bms_loc = (By.XPATH, '//*[@title="BMS"]')
    # 告警类型-液冷系统
    search_alarm_type_liquid_cooling_system_loc = (By.XPATH, '//*[@title="液冷系统"]')
    # 告警类型-消防系统
    search_alarm_type_fire_system_loc = (By.XPATH, '//*[@title="消防系统"]')
    # 告警类型-集装箱类
    search_alarm_type_container_loc = (By.XPATH, '//*[@title="集装箱类"]')

    # 运维告警等级选择框
    search_alarm_level_select_loc = (By.XPATH, '//*[text()="请选择运维告警等级"]/..')
    # 告警等级-一级
    search_alarm_level_first_loc = (By.XPATH, '//*[@title="一级"]')
    # 告警等级-二级
    search_alarm_level_second_loc = (By.XPATH, '//*[@title="二级"]')
    # 告警等级-三级
    search_alarm_level_third_loc = (By.XPATH, '//*[@title="三级"]')
    # 告警等级-四级
    search_alarm_level_fourth_loc = (By.XPATH, '//*[@title="四级"]')

    # 是否告警 选择框
    search_is_alarm_select_loc = (By.XPATH, '//*[text()="请选择是否告警"]/..')
    # 是否告警-是
    search_is_alarm_yes_loc = (By.XPATH, '//*[@title="是"]')
    # 是否告警-否
    search_is_alarm_no_loc = (By.XPATH, '//*[@title="否"]')

    # 是否自动生成工单 选择框
    search_is_auto_create_work_order_select_loc = (By.XPATH, '//*[text()="请选择是否自动生成工单"]/..')
    # 是否自动生成工单-是
    # search_is_auto_create_work_order_yes_loc = (By.XPATH, '//*[@id="rc_select_64_list"]/following::div[@title="是"]')
    # search_is_auto_create_work_order_yes_loc = (By.XPATH, '//*[@id="rc_select_64_list_0"')
    search_is_auto_create_work_order_yes_loc = (By.XPATH, '(//*[@title="是"])[2]')
    # 是否自动生成工单-否
    # search_is_auto_create_work_order_no_loc = (By.XPATH, '//*[@title="否"]')
    search_is_auto_create_work_order_no_loc = (By.XPATH, '(//*[@title="否"])[2]')
    # search_is_auto_create_work_order_no_loc = (By.XPATH, '//*[@id="rc_select_64_list"]/following::div[@title="否"]')

    # 最后修改人输入框
    search_last_modifier_input_loc = (By.XPATH, '//*[@placeholder="请输入最后修改人"]')
