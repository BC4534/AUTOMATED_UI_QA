# 巡检项配置定位器
from selenium.webdriver.common.by import By


class CheckitemConfigurationLocator:
    # 项目管理模块是否展开 //*[text()="项目管理"]/../..
    project_management_is_expand_loc = (By.XPATH, '//*[text()="项目管理"]/../..')
    # 项目管理
    project_management_loc = (By.XPATH, '//*[text()="项目管理"]')
    # 巡检项配置页面
    checkitem_configuration_loc = (By.XPATH, '//*[text()="巡检项配置"]/../..')

    #  巡检项名称输入框 前面的巡检名称 //*[text()="巡检项名称"]
    checkitem_name_input_tip_loc = (By.XPATH, '//*[text()="巡检项名称"]')

    # 新增巡检项按钮
    add_checkitem_button_loc = (By.XPATH, '//*[text()="新增"]')
    # 新增巡检项界面元素
    # 新增巡检项弹框 确定按钮
    add_checkitem_button_confirm_loc = (By.XPATH, '//*[text()="确 定"]/..')
    # 新增巡检项弹框 取消按钮
    add_checkitem_button_cancel_loc = (By.XPATH, '//*[text()="取 消"]/..')
    # 新增巡检项弹框 X按钮
    add_checkitem_button_close_loc = (By.XPATH, '//*[@aria-label="Close"]')
    # 新增巡检项弹框 巡检项名称输入框 id="basic_name"
    add_checkitem_name_input_loc = (By.XPATH, '//*[@id="basic_name"]')
    # 新增巡检项弹框 巡检项类型选择框
    add_checkitem_type_select_loc = (By.XPATH, '//*[@id="basic_type"]/../..')
    # 巡检项类型- title="储能电池及电池管理系统（BMS）"
    add_checkitem_type_select_option_bms_loc = (
        By.XPATH,
        '//*[@title="储能电池及电池管理系统（BMS）" and @aria-selected]',
    )
    # 巡检项类型-储能变流器（PCS）
    add_checkitem_type_select_option_pcs_loc = (
        By.XPATH,
        '//*[@title="储能变流器（PCS）" and @aria-selected]',
    )
    # 巡检项类型-电池室或电池仓
    add_checkitem_type_select_option_battery_loc = (
        By.XPATH,
        '//*[@title="电池室或电池仓" and @aria-selected]',
    )
    # 巡检项类型-液冷系统
    add_checkitem_type_select_option_liquid_loc = (
        By.XPATH,
        '//*[@title="液冷系统" and @aria-selected]',
    )
    # 巡检项类型- EMS系统
    add_checkitem_type_select_option_ems_loc = (
        By.XPATH,
        '//*[@title="EMS系统" and @aria-selected]',
    )
    # 巡检项类型-消防系统
    add_checkitem_type_select_option_fire_loc = (
        By.XPATH,
        '//*[@title="消防系统" and @aria-selected]',
    )
    # 巡检项类型- 空调系统
    add_checkitem_type_select_option_air_loc = (
        By.XPATH,
        '//*[@title="空调系统" and @aria-selected]',
    )
    # 巡检项类型- 汇流柜
    add_checkitem_type_select_option_hui_loc = (
        By.XPATH,
        '//*[@title="汇流柜" and @aria-selected]',
    )

    # 巡检项内容输入框 id="basic_description"
    add_checkitem_content_input_loc = (By.XPATH, '//*[@id="basic_description"]')
    # 是否需要上传拍照信息 -是 (//input[@class="ant-radio-input"])[1]/..
    add_checkitem_photo_yes_loc = (
        By.XPATH,
        '(//input[@class="ant-radio-input"])[1]/..',
    )
    # 是否需要上传拍照信息 -否 (//input[@class="ant-radio-input"])[2]/..
    add_checkitem_photo_no_loc = (By.XPATH, '(//input[@class="ant-radio-input"])[2]/..')
    # 是否需要上传备注 -是
    add_checkitem_remark_yes_loc = (
        By.XPATH,
        '(//input[@class="ant-radio-input"])[3]/..',
    )
    # 是否需要上传备注 -否
    add_checkitem_remark_no_loc = (
        By.XPATH,
        '(//input[@class="ant-radio-input"])[4]/..',
    )

    # 删除巡检项按钮
    delete_checkitem_button_loc = (By.XPATH, '//*[text()="批量删除"]')
    # 取消删除按钮 //*[@class="ant-modal-confirm-btns"]/button
    delete_checkitem_button_cancel_loc = (
        By.XPATH,
        '//*[@class="ant-modal-confirm-btns"]/button',
    )
    # 确认删除按钮
    delete_checkitem_button_confirm_loc = (
        By.XPATH,
        '//*[@class="ant-modal-confirm-btns"]/button[2]',
    )
    # 第一条巡检项的编辑按钮
    first_checkitem_edit_button_loc = (By.XPATH, '//*[text()="编辑"]/..')
    # 编辑巡检项 页面title
    edit_checkitem_title_loc = (By.XPATH, '//*[text()="编辑巡检项"]')

    # 新增巡检项必填项提示
    # 巡检项名称必填项 class="ant-form-item-explain-error" text()="请输入巡检项名称"
    add_checkitem_name_required_loc = (
        By.XPATH,
        '//*[text()="请输入巡检项名称"and@class="ant-form-item-explain-error"]',
    )
    # 请选择巡检项类型
    add_checkitem_type_required_loc = (
        By.XPATH,
        '//*[text()="请选择巡检项类型"and@class="ant-form-item-explain-error"]',
    )
    # 请输入巡检项内容
    add_checkitem_content_required_loc = (
        By.XPATH,
        '//*[text()="请输入巡检项描述"and@class="ant-form-item-explain-error"]',
    )
    # 请选择是否需要上传拍照信息
    add_checkitem_photo_required_loc = (
        By.XPATH,
        '//*[text()="请选择是否需要上传拍照信息"and@class="ant-form-item-explain-error"]',
    )
    # 请选择是否需要上传备注
    add_checkitem_remark_required_loc = (
        By.XPATH,
        '//*[text()="请选择是否需要上传备注"and@class="ant-form-item-explain-error"]',
    )

    # 当前页最后一个巡检项名称  //*[@class="ant-table-tbody"]/tr[last()]/td[2]/div
    current_page_last_checkitem_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[last()]/td[2]/div',
    )
    # 当前页第一个巡检项名称
    current_page_first_checkitem_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[2]/td[2]/div',
    )
    # 第二个巡检项名称
    second_checkitem_name_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[3]/td[2]/div',
    )
    # 最后一条巡检项的复选框
    last_checkitem_checkbox_loc = (
        By.XPATH,
        '//*[@class="ant-table-tbody"]/tr[last()]/td//span',
    )

    # 下一页 //*[contains(@class,"ant-pagination-next")and @title="下一页"]
    next_page_loc = (
        By.XPATH,
        '//*[contains(@class,"ant-pagination-next")and @title="下一页"]',
    )
    # 上一页 //*[contains(@class,"ant-pagination-prev")and @title="上一页"]
    previous_page_loc = (
        By.XPATH,
        '//*[contains(@class,"ant-pagination-prev")and @title="上一页"]',
    )
    # 页面提示信息元素
    page_tip_loc = (
        By.XPATH,
        '//*[@class="ant-message-notice-content"]/div/span[last()]',
    )

    # 巡检项名称查询输入框
    checkitem_name_input_loc = (By.XPATH, '//*[@placeholder="请输入巡检项名称"]')

    # 查询按钮
    checkitem_search_button_loc = (By.XPATH, '//*[text()="搜 索"]/..')
    # 重置按钮
    checkitem_reset_button_loc = (By.XPATH, '//*[text()="重 置"]/..')
