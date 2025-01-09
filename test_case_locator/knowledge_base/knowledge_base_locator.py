from selenium.webdriver.common.by import By



class KnowledgeBaseLocator:
    # 知识库
    knowledge_base_loc = (By.XPATH, '//*[text()="知识库"]/../..')

    #---------搜索相关元素
    # 搜索
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]/..')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]/..')

    # -----------界面元素
    # 新增知识按钮
    add_knowledge_button_loc = (By.XPATH, '//*[text()="新增知识"]/..')
    # 删除知识按钮
    delete_knowledge_button_loc = (By.XPATH, '//*[text()="删除知识"]')
    # 审核按钮
    audit_button_loc = (By.XPATH, '//*[text()="审核"]')
    # 详情按钮
    detail_button_loc = (By.XPATH, '//*[text()="详情"]')

    # ---------详情界面
    # 确认按钮
    confirm_button_loc = (By.XPATH, '//*[text()="确 定"]')
    # 取消按钮
    cancel_button_loc = (By.XPATH, '//*[text()="取 消"]')
    # 关闭按钮
    close_button_loc = (By.XPATH, '//*[@aria-label="Close"]')


    # ---------新增知识界面
    # 知识类型选择框  //*[@title="知识类型"]/following::div[@class="ant-select-selector"]
    knowledge_type_select_loc = (By.XPATH, '//*[@title="知识类型"]/following::div[@class="ant-select-selector"]')
    # 知识标题
    title_input_loc = (By.XPATH, '//*[@placeholder="请输入标题"]')
    # 关联项目选择框
    project_select_loc = (By.XPATH, '//*[@title="关联项目"]/following::div[@class="ant-select-selector"]')
    # 关联设备类型选择框
    device_type_select_loc = (By.XPATH, '//*[text()="关联设备类型"]/following::div[@class="ant-select-selector"]')
    # 异常环节选择框
    abnormal_select_loc = (By.XPATH, '//*[@title="异常环节"]/following::div[@class="ant-select-selector"]')
    # 知识内容
    content_input_loc = (By.XPATH, '//*[@class="w-e-text-container"]/div[3]/div')
    # 提交按钮
    submit_button_loc = (By.XPATH, '//*[text()="提 交"]/..')
    # 保存按钮
    save_button_loc = (By.XPATH, '//*[text()="保 存"]/..')
    # 返回按钮
    back_button_loc = (By.XPATH, '//*[text()="返 回"]/..')

    # 关联设备信息 215选项
    device_215_option_loc = (By.XPATH, '//*[@title="215"]')
    # 232选项
    device_232_option_loc = (By.XPATH, '//*[@title="232"]')
    # 372选项
    device_372_option_loc = (By.XPATH, '//*[@title="372"]')
    # 集装箱选项
    device_container_option_loc = (By.XPATH, '//*[@title="集装箱"]')

    # 关联项目下的第一个选项
    first_project_option_loc = (By.XPATH, '//*[@id="projectId_list"]/following::div[@aria-selected]')
    # 知识类型
    # 问题总结选项
    problem_summary_option_loc = (By.XPATH, '//*[@title="问题总结" and @aria-selected]')
    # 规则制度选项
    rule_regulation_option_loc = (By.XPATH, '//*[@title="规章制度"and @aria-selected]')
    # 行业标准选项
    industry_standard_option_loc = (By.XPATH, '//*[@title="行业标准"and @aria-selected]')
    # 项目资料选项
    project_info_option_loc = (By.XPATH, '//*[@title="项目资料" and @aria-selected]')
    # 异常环节下的
    # 储能电池及电池管理系统（BMS） 选项
    abnormal_bms_option_loc = (By.XPATH, '//*[@title="储能电池及电池管理系统（BMS）"]')
    # 储能变流器（PCS）选项
    abnormal_pcs_option_loc = (By.XPATH, '//*[@title="储能变流器（PCS）"]')
    # 电池室或电池仓
    abnormal_battery_room_option_loc = (By.XPATH, '//*[@title="电池室或电池仓"]')
    # 液冷系统
    abnormal_liquid_cooling_system_option_loc = (By.XPATH, '//*[@title="液冷系统"]')
    # 消防系统
    abnormal_fire_system_option_loc = (By.XPATH, '//*[@title="消防系统"]')
    # 空调系统
    abnormal_air_conditioning_system_option_loc = (By.XPATH, '//*[@title="空调系统"]')
    # 汇流柜
    abnormal_mixing_cabinet_option_loc = (By.XPATH, '//*[@title="汇流柜"]')

    # 知识库新增界面
    knowledge_base_page_loc = (By.XPATH, '//*[@class="inContent___BYuNX"]')

    # 第一条知识名称
    first_knowledge_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[3]')
    # 第二条知识名称
    second_knowledge_name_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[3]')
    # 第一条知识状态
    first_knowledge_status_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[2]')
    # 知识标题必填项提示文本 //*[@id="title_help"]/div
    title_required_text_loc = (By.XPATH, '//*[@id="title_help"]/div')
    # 第一条知识的复选框
    first_knowledge_checkbox_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[1]//span')
    # 第二条知识的复选框
    second_knowledge_checkbox_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[3]/td[1]//span')
    # 第三条知识的复选框
    third_knowledge_checkbox_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[4]/td[1]//span')
    # 第一条知识的详情按钮
    first_knowledge_detail_button_loc = (By.XPATH, '//*[text()="详情"]')
    # 第一条知识的编辑按钮
    first_knowledge_edit_button_loc = (By.XPATH, '//*[text()="编辑"]')
    # 详情界面
    detail_page_loc = (By.XPATH, '//*[@data-rc-order="append"]')
    # 详情界面的标题
    detail_page_title_loc = (By.XPATH, '//*[@class="ant-modal-title"]')

    # 查询相关
    # 知识名称输入框 //*[@placeholder="请输入知识名称"]
    knowledge_name_input_loc = (By.XPATH, '//*[@placeholder="请输入知识名称"]')
    # 查询功能知识类型选择框
    query_knowledge_type_select_loc = (By.XPATH, '//*[text()="请选择知识类型"]/../..')
    # 第一条知识类型
    first_knowledge_type_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[4]')
    # 查询功能知识状态选择框
    query_knowledge_status_select_loc = (By.XPATH, '//*[text()="请选择知识状态"]/../..')
    # 草稿
    draft_option_loc = (By.XPATH, '//*[@title="草稿"]')
    # 待修改
    to_be_modified_option_loc = (By.XPATH, '//*[@title="待修改"]')
    # 审核中
    under_review_option_loc = (By.XPATH, '//*[@title="审核中"]')
    # 审核成功
    audit_success_option_loc = (By.XPATH, '//*[@title="审核成功"]')
    # 异常环节选择框
    query_abnormal_select_loc = (By.XPATH, '//*[text()="请选择异常环节"]/../..')
    # 第一个知识的异常环节
    first_knowledge_abnormal_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[9]')
    # 第一个知识的关联设备类型
    first_knowledge_device_type_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[8]')
    # 第一个知识的撰写人
    first_knowledge_writer_loc = (By.XPATH, '//*[@class="ant-table-tbody"]/tr[2]/td[7]')
    # 撰写人选择框
    writer_select_loc = (By.XPATH, '//*[@placeholder="请输入撰写人"]')

    # 第一个审核按钮
    first_audit_button_loc = (By.XPATH, '//*[text()="审核"]')
    # 第二个审核按钮
    second_audit_button_loc = (By.XPATH, '//*[text()="审核"]')
    # 审核界面的审核按钮
    audit_page_audit_button_loc = (By.XPATH, '//*[text()="审 核"]')
    # 审核界面的返回按钮
    audit_page_reject_button_loc = (By.XPATH, '//*[text()="返 回"]')
    # 审核按钮界面的审核通过选项
    audit_pass_option_loc = (By.XPATH, '//*[text()="审核通过"]/preceding-sibling::span')
    # 审核按钮界面的审核拒绝选项
    audit_reject_option_loc = (By.XPATH, '//*[text()="审核拒绝"]/preceding-sibling::span')
    # 审核备注输入框 id="remark"
    audit_remark_input_loc = (By.XPATH, '//*[@id="remark"]')







