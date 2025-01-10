from selenium.webdriver.common.by import By


class ProjectAlarmConfigurationLocator(object):

    # 系统配置
    system_config_loc = (By.XPATH, '//*[text()="系统配置"]')

    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[text()="搜 索"]')
    # 重置按钮
    reset_button_loc = (By.XPATH, '//*[text()="重 置"]')
    # 巡检项名称输入框
    inspection_item_name_input_loc = (By.XPATH, '//*[@placeholder="请输入巡检项名称"]')
