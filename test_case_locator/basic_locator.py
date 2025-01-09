from selenium.webdriver.common.by import By


class BasicLocator(object):
    """
    This class is used to locate elements on the web page.
    """
    # 当前年 //*[@class="ant-picker-header-view"]/button[1]
    current_year_value_loc = (By.XPATH, '//*[@class="ant-picker-header-view"]/button[1]')
    # 当前月 //*[@class="ant-picker-header-view"]/button[2]
    current_month_value_loc = (By.XPATH, '//*[@class="ant-picker-header-view"]/button[2]')
    # 前一年按钮 //*[@class="ant-picker-header-super-prev-btn"]
    previous_year_button_loc = (By.XPATH, '//*[@class="ant-picker-header-super-prev-btn"]')
    # 后一年按钮 class="ant-picker-header-super-next-btn"
    next_year_button_loc = (By.XPATH, '//*[@class="ant-picker-header-super-next-btn"]')
    # 前一月按钮 //*[@class="ant-picker-header-prev-btn"]
    previous_month_button_loc = (By.XPATH, '//*[@class="ant-picker-header-prev-btn"]')
    # 后一月按钮 //*[@class="ant-picker-header-next-btn"]
    next_month_button_loc = (By.XPATH, '//*[@class="ant-picker-header-next-btn"]')
