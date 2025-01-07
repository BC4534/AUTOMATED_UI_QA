# 大储告警配置
from selenium.webdriver.common.by import By


class ContainerAlarmConfigurationLocator:

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
    # 页面提示信息元素
    page_tip_loc = (By.XPATH, '//*[@class="ant-message-notice-content"]/div/span[last()]')

    # 批量更新弹框的 仅支持.xlsx、.xls后缀名文件元素
    batch_update_file_format_loc = (By.XPATH, '//*[text()="仅支持.xlsx、.xls后缀名文件"]')