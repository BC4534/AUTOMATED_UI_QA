# Version: 1.0.0
# Last modified: 2024-09-04
# 用于记录存储所有文件路径


import os

# 工程路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# webdriver路径
webdriver_path = os.path.join(project_path, "config", "webdriver", "chromedriver.exe")

# excel文件路径

# config.yaml文件路径
config_yaml_path = os.path.join(project_path, "config", "config.yaml")

# 截图文件路径
screenshot_path = os.path.join(project_path, "output", "screenshots")
# 日志文件路径
log_path = os.path.join(project_path, "output", "logs")
#  allure报告绝对路径
allure_results_path = os.path.join(project_path, "output", "allure_results")
# allure 报告项目路径
allure_report_relative_path = "AUTOMATED_UI_QA/output/allure_report/report/index.html"
# allure report path
allure_report_path = os.path.join(project_path, "output", "allure_report")

# 配置项
# 飞书机器人webhook
feishu_webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/f0c97e2c-f0a7-4ba4-b5bc-d454718c9c20'
# allure report链接
report_link_path = 'http://localhost:63342/AUTOMATED_UI_QA/output/allure_report/report/index.html'

if __name__ == '__main__':
    # print(allure_report_path)
    pass
