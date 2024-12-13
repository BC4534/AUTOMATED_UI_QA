from selenium.webdriver.common.by import By


class AbnormalStatisticLocator:
    # 工单管理
    work_order_management_loc = (By.XPATH, '//*[text()="工单管理"]')
    # 异常复盘
    abnormal_review_loc = (By.XPATH, '//*[text()="异常复盘"]')
    # 异常统计
    abnormal_statistic_loc = (By.XPATH, '//*[text()="异常统计"]')
    # 异常明细
    abnormal_detail_loc = (By.XPATH, '//*[text()="异常明细"]')

    # 产品类型选择框
    product_type_select_loc = (By.XPATH, '//*[@class="ant-select-selector"]')
    # 产品类型-集装箱
    product_type_container_loc = (By.XPATH, '//*[text()="集装箱"]')
    # 产品类型-户外柜
    product_type_outdoor_loc = (By.XPATH, '//*[text()="户外柜"]')
    # 产品类型-非系统
    product_type_non_system_loc = (By.XPATH, '//*[text()="非系统"]')
    # 产品类型文本值
    product_type_text_loc = (By.XPATH, '(//*[@class="ant-select-selection-item"])[1]')
    # 产品类型清除按钮 //*[@class="ant-select-clear"]
    product_type_clear_loc = (By.XPATH, '//*[@class="ant-select-clear"]')
    # 场景类型选择框未选择状态
    scene_type_select_unselected_loc = (By.XPATH, '//*[text()="请选择产品类型"]')
    # 场景类型选择框
    scene_type_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[2]')
    # 场景类型-部件
    scene_type_part_loc = (By.XPATH, '//*[text()="部件"]')
    # 场景类型-厂商
    scene_type_vendor_loc = (By.XPATH, '//*[text()="厂商"]')
    # 场景类型文本值
    scene_type_text_loc = (By.XPATH, '(//*[@class="ant-select-selection-item"])[1]')
    # 场景类型清除按钮 //*[@class="ant-select-clear"]
    scene_type_clear_loc = (By.XPATH, '(//*[@class="ant-select-clear"])')
    # 时间维度选择框
    time_dimension_select_loc = (By.XPATH, '(//*[@class="ant-select-selector"])[3]')
    # 时间维度-年
    time_dimension_year_loc = (By.XPATH, '//*[text()="年"]')
    # 时间维度-月
    time_dimension_month_loc = (By.XPATH, '//*[text()="月"]')
    # 时间维度文本值
    time_dimension_text_loc = (By.XPATH, '(//*[@class="ant-select-selection-item"])[2]')

    # 年月选择框
    year_month_select_loc = (By.XPATH, '//*[@class="ant-picker-input"]')
    # 上一年、上一个月
    year_month_previous_loc = (By.XPATH, '//*[@class="ant-picker-header-super-prev-btn"]')
    # 下一年、下一个月
    year_month_next_loc = (By.XPATH, '//*[@class="ant-picker-header-super-next-btn"]')


