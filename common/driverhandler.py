from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from common.all_file_path import webdriver_path

class DriverHandler():
    def __init__(self, config_dict):
        self.config = config_dict

    def get_value(self, section, key):
        return self.config.get(section, {}).get(key, None)

def get_driver():
    # 示例配置字典
    config_dict = {
        "driver": {
            "driver_object": "chrome",
            "driver_path": webdriver_path,
            "driver_headless": "false"
        }
    }
    driver_handler = DriverHandler(config_dict)  # 正确实例化MyConfig类
    driver_value = driver_handler.get_value("driver", "driver_object")
    driver_path = driver_handler.get_value("driver", "driver_path")
    driver_headless = driver_handler.get_value("driver", "driver_headless")

    if driver_value == "chrome":
        opt = ChromeOptions()
        # opt.add_argument('--start-maximized')
        # opt.add_argument('--start-fullscreen')
        if driver_headless == "false":
            return webdriver.Chrome(executable_path=driver_path, options=opt)
        else:
            opt.add_argument('--headless')
            return webdriver.Chrome(executable_path=driver_path, options=opt)
    elif driver_value == "firefox":
        opt = FirefoxOptions()
        if driver_headless == "true":
            opt.add_argument('--headless')
        return webdriver.Firefox(executable_path=driver_path, options=opt)
    else:
        raise ValueError("Unsupported browser type")

