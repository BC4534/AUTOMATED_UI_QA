from selenium.webdriver.common.by import By

class RoleManagementLocator:
    # 系统配置


    system_config_loc = (By.XPATH,'//*[text()="系统配置"]')
    # 账号管理
    role_management_loc = (By.XPATH, '//*[text()="角色管理"]')
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')
    # 查询角色姓名输入框
    select_role_name_input_loc = (By.XPATH, '//*[@placeholder="请输入角色名称"]')

    # 新增角色
    add_role_button_loc = (By.XPATH, '//*[text()="新增角色"]')
    # 批量删除
    batch_delete_button_loc = (By.XPATH, '//*[text()="批量删除"]')
    # 确认批量删除
    confirm_batch_delete_button_loc = (By.XPATH, '//*[@type="button" and @class="ant-btn css-1r287do ant-btn-primary"] ')
    # 取消批量删除
    cancel_batch_delete_button_loc = (By.XPATH, '//*[text()="取 消"]')

    # --- 新增角色界面元素---------
    # 新增角色 名称输入框
    add_role_name_input_loc = (By.XPATH, '//*[@id="basic_name"]')
    # 新增角色 备注输入框
    add_role_remark_input_loc = (By.XPATH,'//*[@id="basic_remark"]' )
    # 权限配置 选择框
    # 运维工作台权限
    permission_config_operation_loc = (By.XPATH, '//*[@class="ant-tree-checkbox-inner"]')
    # 工单管理权限
    permission_config_work_order_loc = (By.XPATH, '(//*[@class="ant-tree-checkbox-inner"])[2]')
    # 项目管理权限
    permission_config_project_loc = (By.XPATH, '(//*[@class="ant-tree-checkbox-inner"])[3]')
    # 运维工具权限
    permission_config_tool_loc = (By.XPATH, '(//*[@class="ant-tree-checkbox-inner"])[4]')
    # 知识库权限
    permission_config_knowledge_loc = (By.XPATH, '(//*[@class="ant-tree-checkbox-inner"])[5]')
    # 系统配置权限
    permission_config_system_loc = (By.XPATH, '(//*[@class="ant-tree-checkbox-inner"])[6]')

    # 确定按钮
    confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 取消按钮
    cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # 关闭按钮
    close_button_loc = (By.XPATH, '//*[@aria-label="Close"]')

    # 页面弹窗提示
    page_tip_loc = (By.XPATH, '//*[@class="ant-message-notice-content"]//span[2]')

    # 第一个角色复选框
    first_role_checkbox_loc = (By.XPATH, '(//*[@class="ant-checkbox-wrapper css-1hzb5nd"])[2]')
    # 第一个角色名称
    first_role_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]//td[@class="ant-table-cell"]')
    # 第一个角色编辑按钮
    first_role_edit_button_loc = (By.XPATH, '//*[text()="编辑"]')
    # 第二个角色名称
    second_role_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[2]')
    # 第二个角色复选框
    second_role_checkbox_loc = (By.XPATH, '(//*[@class="ant-checkbox-wrapper css-1hzb5nd"])[3]')
    # 新增角色必填项
    add_role_name_required_loc = (By.XPATH, '//*[text()="请输入角色名称"]')
    add_role_remark_required_loc=  (By.XPATH, '//*[text()="请输入角色说明"]')

    # 新增角色界面关闭断言元素
    role_page_assert_loc = (By.XPATH, '//*[@class="ant-modal-wrap"]')
    # 全选按钮
    all_role_checkbox_loc = (By.XPATH, '//*[@class="ant-checkbox-wrapper css-1hzb5nd"]')

    # 新增、编辑展开页面标识元素
    page_name_loc = (By.XPATH, '//*[@style="font-size: 20px; font-family: PingFangSemiblod;"]')
