from selenium.webdriver.common.by import By


class ProjectOperationOverviewLocator:
    # 运维工具页面是否展开
    maintenance_tools_page_expand_loc = (By.XPATH, "//*[text()='运维工具']/../..")
    # 运维工具模块
    maintenance_tools_module_loc = (By.XPATH,"//*[text()='运维工具']")

    # 项目运行报告
    project_operation_report_loc = (By.XPATH,"//*[text()='项目运行报告']/../..")

    # 项目运行总览
    project_operation_overview_loc = (By.XPATH,"//*[text()='项目运行总览']")

    # 导出查询数据按钮
    export_query_data_button_loc = (By.XPATH,"//*[text()='导出查询数据']/..")

    # 项目名称输入框  //*[text()="项目名称"]/following::input[@type="search"]/../../..
    project_name_input_loc = (By.XPATH, "//*[text()='项目名称']/following::input[@type='search']")
    # 电站名称输入框
    station_name_input_loc = (By.XPATH, "//*[text()='电站名称']/following::input[@type='search']")

    # 项目运行日报界面第一条数据名称
    first_data_project_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[2]/td[1]")
    # 项目运行日报界面第一条数据的电站名称
    first_data_station_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[2]/td[2]")
    # 项目运行日报界面第二条数据名称
    second_data_project_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[3]/td[1]")
    # 项目运行日报界面第二条数据的电站名称
    second_data_station_name_loc = (By.XPATH, "//*[@class='ant-table-tbody']/tr[3]/td[2]")