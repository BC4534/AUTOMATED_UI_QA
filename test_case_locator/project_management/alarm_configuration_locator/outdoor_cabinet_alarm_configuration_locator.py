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
