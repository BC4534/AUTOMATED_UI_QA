class SupplierMaintenanceLocator(object):

    # 供应商维护按钮
    supplier_maintenance_button_loc = ("xpath", '//*[text()="供应商维护"]/..')

    # 供应商维护页面标题
    supplier_maintenance_title_loc = (
        "xpath",
        '//*[text()="供应商维护" and @class="ant-modal-title"]',
    )

    # 供应商维护页 新增按钮
    supplier_maintenance_add_button_loc = ("xpath", '//*[text()="新 增"]/..')
    # 供应商维护页 确认按钮
    supplier_maintenance_confirm_button_loc = ("xpath", '//*[text()="确 定"]/..')
    # 供应商维护页 取消按钮
    supplier_maintenance_cancel_button_loc = ("xpath", '//*[text()="取 消"]/..')
    # 供应商维护页 X按钮
    supplier_maintenance_close_button_loc = (
        "xpath",
        '//*[@role="dialog"]//button[@aria-label="Close"]',
    )

    # 供应商维护页 操作-编辑按钮
    supplier_maintenance_edit_button_loc = ("xpath", '//*[text()="编辑" and @type]')
    # 供应商维护页 操作-删除按钮
    supplier_maintenance_delete_button_loc = ("xpath", '//*[text()="删除" and @type]')
    # 供应商维护页 操作-删除 - 确认删除按钮
    supplier_maintenance_delete_confirm_button_loc = (
        "xpath",
        '//*[@class="ant-popconfirm-buttons"]/button[2]',
    )
    # 供应商维护页 操作-删除 - 取消删除按钮
    supplier_maintenance_delete_cancel_button_loc = (
        "xpath",
        '//*[@class="ant-popconfirm-buttons"]/button[1]',
    )

    # 供应商维护页 操作-清空按钮
    supplier_maintenance_clear_button_loc = ("xpath", '//*[text()="清空" and @type]')
    # 供应商维护页 操作-保存按钮
    supplier_maintenance_save_button_loc = ("xpath", '//*[text()="保存" and @type]')

    # 供应商维护页 供应商名输入框
    supplier_maintenance_supplier_name_input_loc = ("xpath", '//*[@id="name"]')
    # 供应商维护页 供应商类型下拉框 id="supplyScope"
    supplier_maintenance_supplier_type_select_loc = (
        "xpath",
        '//*[@id="supplyScope"]/../../../..',
    )
    # 供应商维护页 供应商类型下拉框选项 - EMS //*[@title="EMS" and contains(@class,"ant-select-item ant-select-item-option")]
    supplier_maintenance_supplier_type_ems_option_loc = (
        "xpath",
        '//*[@title="EMS" and contains(@class,"ant-select-item ant-select-item-option")]',
    )

    # 供应商维护页 第一个供应商名称  (//*[@class="ant-table-tbody"])[2]/tr[2]/td[1]
    supplier_maintenance_first_supplier_name_loc = (
        "xpath",
        '(//*[@class="ant-table-tbody"])[2]/tr[2]/td[1]',
    )
    # 供应商维护页 第一个供应商类型  (//*[@class="ant-table-tbody"])[2]/tr[2]/td[2]
    supplier_maintenance_first_supplier_type_loc = (
        "xpath",
        '(//*[@class="ant-table-tbody"])[2]/tr[2]/td[2]',
    )

    # 必填项供应商名
    supplier_maintenance_get_supplier_name_required_loc = (
        "xpath",
        '//*[@id="name_help"]/div',
    )
    # 必填项供应商类型
    supplier_maintenance_get_supplier_type_required_loc = (
        "xpath",
        '//*[@id="supplyScope_help"]/div',
    )
