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
