from selenium.webdriver.common.by import By



class KnowledgeBaseLocator:
    # 知识库
    knowledge_base_loc = (By.XPATH, '//*[text()="知识库"]')

    #---------搜索相关元素
    # 搜索
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')

    # -----------界面元素
    # 新增知识按钮
    add_knowledge_button_loc = (By.XPATH, '//*[text()="新增知识"]')
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
    # 知识类型
    knowledge_type_loc = (By.XPATH, '//*[@title="问题总结"]')
    # 知识标题
    title_input_loc = (By.XPATH, '//*[@placeholder="请输入标题"]')
    # 关联项目
    project_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[2]')
    # 关联设备类型
    device_type_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[3]')
    # 异常环节
    abnormal_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[4]')
    # 知识内容
    content_input_loc = (By.XPATH, '//*[@id="w-e-textarea-1"]')
    # 提交按钮
    # submit_button_loc = (By.XPATH, '//*[text()="提 交"]')
    # submit_button_loc = (By.XPATH, '//*[@class="ant-btn css-1hzb5nd ant-btn-primary"]')
    submit_button_loc = (By.XPATH, '(//*[@class="ant-space-item"])[3]')
    # 保存按钮
    save_button_loc = (By.XPATH, '//*[text()="保 存"]')
    # 返回按钮
    back_button_loc = (By.XPATH, '//*[text()="返 回"]')

    # 关联设备信息 215选项
    device_215_option_loc = (By.XPATH, '//*[@title="215"]')
    # 232选项
    device_232_option_loc = (By.XPATH, '//*[@title="232"]')
    # 372选项
    device_372_option_loc = (By.XPATH, '//*[@title="372"]')
    # 集装箱选项
    device_container_option_loc = (By.XPATH, '//*[@title="集装箱"]')

    # 关联项目下的第一个选项
    first_project_option_loc = (By.XPATH, '(//*[@class="rc-virtual-list-holder-inner"])[2]/div')
    # 知识类型
    # 问题总结选项
    problem_summary_option_loc = (By.XPATH, '//*[@title="问题总结"]')
    # 规则制度选项
    rule_regulation_option_loc = (By.XPATH, '//*[@title="规章制度"]')
    # 行业标准选项
    industry_standard_option_loc = (By.XPATH, '//*[@title="行业标准"]')
    # 项目资料选项
    project_material_option_loc = (By.XPATH, '//*[@title="项目资料"]')
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




