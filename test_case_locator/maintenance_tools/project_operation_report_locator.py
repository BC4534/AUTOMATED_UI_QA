from selenium.webdriver.common.by import By


class ProjectOperationReportLocator:
    # 下载任务列表按钮  //*[@aria-label="arrow-down"]
    download_task_list_button_loc = (By.XPATH, "//*[@aria-label='arrow-down']")
    # 下载任务列表按钮 第一个任务名称 //*[text()="任务列表"]/following::tbody[@class="ant-table-tbody"]/tr/td
    download_task_list_button_first_task_name_loc = (By.XPATH, "//*[text()='任务列表']/following::tbody[@class='ant-table-tbody']/tr/td")
    # 下载任务列表按钮 第二个任务名称
    download_task_list_button_second_task_name_loc = (By.XPATH, "//*[text()='任务列表']/following::tbody[@class='ant-table-tbody']/tr[2]/td")
    # 下载任务列表按钮 第一个任务状态
    download_task_list_button_first_task_status_loc = (By.XPATH, "//*[text()='任务列表']/following::tbody[@class='ant-table-tbody']/tr/td[2]")
    # 下载任务列表按钮 第二个任务状态
    download_task_list_button_second_task_status_loc = (By.XPATH, "//*[text()='任务列表']/following::tbody[@class='ant-table-tbody']/tr[2]/td[2]")
    # 下载任务列表按钮 第一个任务创建时间
    download_task_list_button_first_task_create_time_loc = (By.XPATH, "//*[text()='任务列表']/following::tbody[@class='ant-table-tbody']/tr/td[4]")
    # 下载任务列表按钮 第二个任务创建时间
    download_task_list_button_second_task_create_time_loc = (By.XPATH, "//*[text()='任务列表']/following::tbody[@class='ant-table-tbody']/tr[2]/td[4]")

    # 运维工具页面是否展开
    maintenance_tools_page_expand_loc = (By.XPATH, "//*[text()='运维工具']/../..")
    # 运维工具模块
    maintenance_tools_module_loc = (By.XPATH,"//*[text()='运维工具']")

    # 项目运行报告
    project_operation_report_loc = (By.XPATH,"//*[text()='项目运行报告']/../..")

    # 项目运行日报tab
    project_operation_report_daily_tab_loc = (By.XPATH,"//*[text()='项目运行日报']")

    # 导出查询数据
    export_query_data_button_loc = (By.XPATH,"//*[text()='导出查询数据']/..")
    # 批量导出云平台巡检数据按钮
    batch_export_cloud_platform_inspection_data_button_loc = (By.XPATH, "//*[text()='批量导出云平台巡检数据']")
    # 第一个导出云平台巡检记录按钮
    export_cloud_platform_inspection_record_button_loc = (By.XPATH, "//*[text()='导出云平台巡检记录']")
    # 巡检记录界面title //*[text()='巡检记录导出' and @class="ant-modal-title"]
    inspection_record_title_loc = (By.XPATH, "//*[text()='巡检记录导出' and @class='ant-modal-title']")
    # 巡检记录界面第一个导出按钮 //*[text()='巡检记录导出' and @class="ant-modal-title"]/following::button
    inspection_record_export_button_loc = (By.XPATH, "//*[text()='巡检记录导出' and @class='ant-modal-title']/following::button")
    # 巡检记录界面导出全部文件按钮
    inspection_record_export_all_file_button_loc = (By.XPATH, "//*[text()='导出全部文件']/..")
    # 巡检记录界面 关闭按钮aria-label="close"
    inspection_record_close_button_loc = (By.XPATH, '//*[@aria-label="close"]')
    # 界面 //*[@class="ant-modal-content"]
    content_page_loc = (By.XPATH, "//*[@class='ant-modal-content']")

    # 项目运行日报界面第一条数据名称
    first_data_project_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[2]/td[3]")
    # 项目运行日报界面第一条数据的电站名称
    first_data_station_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[2]/td[4]")
    # 项目运行日报界面第二条数据名称
    second_data_project_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[3]/td[3]")
    # 项目运行日报界面第二条数据的电站名称
    second_data_station_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[3]/td[4]")
    # 项目运行日报界面第一条数据的检测时间
    first_data_check_time_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[2]/td[2]")
    # 项目运行日报界面第二条数据的检测时间
    second_data_check_time_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[3]/td[2]")



    # 第一个数据的导出当日充放原数据
    export_daily_charge_and_discharge_original_data_button_loc = (By.XPATH, "//*[text()='导出当日充放原数据']")
    # 全选复选框 //*[@class="ant-table-thead"]//div[@class="ant-table-selection"]
    select_all_checkbox_loc = (By.XPATH, "//*[@class='ant-table-thead']//div[@class='ant-table-selection']")
    # 项目运行日报界面第一个数据的项目名称

    # 项目名称输入框  //*[text()="项目名称"]/following::input[@type="search"]/../../..
    project_name_input_loc = (By.XPATH, "//*[text()='项目名称']/following::input[@type='search']")
    #电站名称输入框
    station_name_input_loc = (By.XPATH, "//*[text()='电站名称']/following::input[@type='search']")
    # 日报生成时间输入框  //*[text()="日报生成时间"]/following::div
    daily_report_generation_time_input_loc = (By.XPATH, "//*[text()='日报生成时间']/following::div")

    # 下载任务列表任务名称 //*[text()='任务名称']/following::input[@placeholder]
    download_task_list_task_name_loc = (By.XPATH, "//*[text()='任务名称']/following::input[@placeholder]")
    # 下载任务列表任务状态 //*[text()='状态']/following::input[@type="search"]
    download_task_list_task_status_loc = (By.XPATH, "//*[text()='状态']/following::input[@type='search']/../../..")
    # 创建时间
    download_task_list_create_time_loc = (By.XPATH, "//*[text()='创建时间']/following::input[@placeholder]")







