from selenium.webdriver.common.by import By

class AccountManagementLocator:
    # 系统配置


    cancel_batch_delete_button_loc = (By.XPATH, '//*[text()="取 消"]')
    confirm_batch_delete_button_loc = (By.XPATH, '//*[text()="确 定"]')
    system_config_loc = (By.XPATH,'//*[text()="系统配置"]')
    # 账号管理
    account_management_loc = (By.XPATH, '//*[text()="账号管理"]')

    # 新增账号
    add_account_button_loc = (By.XPATH, '//*[text()="新增账号"]')
    # 批量删除
    batch_delete_button_loc = (By.XPATH, '//*[text()="批量删除"]')
    # 批量删除 后 数量元素
    batch_delete_button_count_loc = (By.XPATH, '//*[text()="批量删除"]/following-sibling::span')
    # 账号输入框 //*[@placeholder="请输入账号"]
    account_input_loc = (By.XPATH, '//*[@placeholder="请输入账号"]')
    # 姓名输入框
    name_input_loc = (By.XPATH, '//*[@placeholder="请输入姓名"]')

    # 编辑按钮
    edit_button_loc = (By.XPATH, '//*[text()="编辑"]')

    # 新增账号 账号字段输入框
    add_account_account_input_loc = (By.XPATH, '//*[@class="ant-form-item-control-input"]//input[@placeholder="请输入账号"]')
    # 新增账号 姓名输入框
    add_account_name_input_loc = (By.XPATH, '//*[@class="ant-form-item-control-input"]//input[@placeholder="请输入姓名"]')
    # 新增账号 密码输入框
    add_account_password_input_loc = (By.XPATH, '//*[@class="ant-form-item-control-input"]//input[@placeholder="请输入密码"]')
    # 新增账号 关联手机号输入框
    add_account_phone_input_loc = (By.XPATH, '//*[@class="ant-form-item-control-input"]//input[@placeholder="请输入关联手机号"]')

    # 新增账号 管辖区域选择框
    add_account_area_select_loc = (By.XPATH, '(//*[@class="ant-select-selection-overflow"])[1]')
    # 新增账号 绑定角色选择框
    add_account_role_select_loc = (By.XPATH, '(//*[@class="ant-select-selection-overflow"])[2]')
    # 新增账号 备注输入框
    add_account_remark_input_loc = (By.XPATH, '//*[@class="ant-form-item-control-input"]//input[@placeholder="请输入备注"]')
    # 新增账号 确认按钮
    add_account_confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 新增账号 取消按钮
    add_account_cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # 新增账号 X按钮
    add_account_close_button_loc = (By.XPATH, '//*[@class="ant-modal-close-x"]')

    # 区域选项 东部、西北、大储运维（宁夏）、南方、海外
    # 东部
    add_account_east_area_option_loc = (By.XPATH, '//*[@title="东部"]')
    # 西北
    add_account_northwest_area_option_loc = (By.XPATH, '//*[@title="西北"]')
    # 大储运维（宁夏）
    add_account_north_area_option_loc = (By.XPATH, '//*[@title="大储运维（宁夏）"]')
    # 南方
    add_account_south_area_option_loc = (By.XPATH, '//*[@title="南方"]')
    # 海外
    add_account_overseas_area_option_loc = (By.XPATH, '//*[@title="海外"]')

    # 角色选项
    account_role_option_loc = (By.XPATH, '//*[@title="系统管理员"]')


    # 新增账号页面
    add_account_page_loc = (By.XPATH, '//*[@class="ant-modal-content"]')

    # 第一个账号
    first_account_loc = (By.XPATH, '//*[@class="ant-table-tbody"]//td[@class="ant-table-cell"]')
    # 第二个账号
    second_account_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[2]')
    # 第一个账号的姓名
    first_account_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]//td[@class="ant-table-cell"][2]')
    # 第一个账号的绑定角色
    first_account_role_loc = (By.XPATH, '//*[@class="ant-table-tbody"]//td[@class="ant-table-cell"][5]')
    # 第一个账号管辖区域""
    first_account_area_loc = (By.XPATH, '//*[@class="ant-table-tbody"]//td[@class="ant-table-cell"][4]')
    # 页面提示弹窗
    page_tip_loc = (By.XPATH, '//*[@class="ant-message-notice-content"]//span[2]')

    # 请输入账号 必填项提示语
    account_required_tip_loc = (By.XPATH, '//*[text()="请输入账号"]')
    # 请输入姓名 必填项提示语
    name_required_tip_loc = (By.XPATH, '//*[text()="请输入姓名"]')

    # 请输入密码 必填项提示语
    password_required_tip_loc = (By.XPATH, '//*[text()="请输入密码"]')

    # 请输入关联手机号 必填项提示语
    phone_required_tip_loc = (By.XPATH, '//*[text()="请输入关联手机号"]')
    # 请选择管辖区域 必填项提示语
    area_required_tip_loc = (By.XPATH, '//*[text()="请选择管辖区域"]')

    # # 新增账号页面 关闭定位元素
    add_account_close_loc = (By.XPATH, '//*[@class="ant-modal-wrap"]')

    # 全选账号复选框
    all_account_checkbox_loc = (By.XPATH, '//*[@class="ant-checkbox-wrapper css-1hzb5nd"]')
    # 第一个复选框
    # first_account_checkbox_loc = (By.XPATH, '(//*[@class="ant-checkbox ant-wave-target css-1hzb5nd"])[2]')
    first_account_checkbox_loc = (By.XPATH, '(//*[@class="ant-checkbox-wrapper css-1hzb5nd"])[2]')
    # first_account_checkbox_loc = (By.XPATH, '(//*[@type="checkbox"])[2]')

    #  第二个复选框
    second_account_check_box_loc = (By.XPATH, '(//*[@class="ant-checkbox-wrapper css-1hzb5nd"])[3]')

    # 搜索相关
    # 账号输入框
    search_account_input_loc = (By.XPATH, '//*[@placeholder="请输入账号"]')
    # 姓名输入框
    search_name_input_loc = (By.XPATH, '//*[@placeholder="请输入姓名"]')
    # 绑定角色
    search_role_select_loc = (By.XPATH, '//*[@class="ant-select-selection-search"]')
    # 管辖区域
    search_area_select_loc = (By.XPATH, '(//*[@class="ant-select-selection-search"])[2]')
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')


