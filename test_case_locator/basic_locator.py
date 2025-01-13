from selenium.webdriver.common.by import By


class BasicLocator(object):
    """
    This class is used to locate elements on the web page.
    """

    # 当前年 //*[@class="ant-picker-header-view"]/button[1]
    current_year_value_loc = (
        By.XPATH,
        '//*[@class="ant-picker-header-view"]/button[1]',
    )
    # 当前月 //*[@class="ant-picker-header-view"]/button[2]
    current_month_value_loc = (
        By.XPATH,
        '//*[@class="ant-picker-header-view"]/button[2]',
    )
    # 前一年按钮 //*[@class="ant-picker-header-super-prev-btn"]
    previous_year_button_loc = (
        By.XPATH,
        '//*[@class="ant-picker-header-super-prev-btn"]',
    )
    # 后一年按钮 class="ant-picker-header-super-next-btn"
    next_year_button_loc = (By.XPATH, '(//*[@class="ant-picker-header-super-next-btn"])[last()]')
    # 前一月按钮 //*[@class="ant-picker-header-prev-btn"]
    previous_month_button_loc = (By.XPATH, '//*[@class="ant-picker-header-prev-btn"]')
    # 后一月按钮 //*[@class="ant-picker-header-next-btn"]
    next_month_button_loc = (By.XPATH, '(//*[@class="ant-picker-header-next-btn"])[last()]')

    #
    # 页面提示信息元素
    page_tip_loc = ( By.XPATH,'//*[@class="ant-message-notice-content"]/div/span[last()]')


    # 查询相关
    # 搜索按钮 //*[text()="搜 索"]/..
    search_button_loc = (By.XPATH,'(//*[text()="搜 索"]/..)[last()]')
    # 重置按钮 //*[text()="重 置"]/..
    reset_button_loc = (By.XPATH,'(//*[text()="重 置"]/..)[last()]')

    # 界面关闭按钮 //*[@aria-label="close"]
    close_button_loc = (By.XPATH,'//*[@aria-label="close"]')

    # 下一页 //*[contains(@class,"ant-pagination-next")and @title="下一页"]
    next_page_loc = (
        By.XPATH,
        '//*[contains(@class,"ant-pagination-next")and @title="下一页"]',
    )
    # 上一页 //*[contains(@class,"ant-pagination-prev")and @title="上一页"]
    previous_page_loc = (
        By.XPATH,
        '//*[contains(@class,"ant-pagination-prev")and @title="上一页"]',
    )
    # 第二页
    second_page_loc = (By.XPATH, '//*[@title="2"]')
    # 第一页
    first_page_loc = (By.XPATH, '//*[@title="1"]')
