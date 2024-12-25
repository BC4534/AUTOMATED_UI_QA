from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from common.all_file_path import webdriver_path

class DriverHandler():
    def __init__(self, config_dict):
        self.config = config_dict

    def get_value(self, section, key):
        return self.config.get(section, {}).get(key, None)

def setup_headless_mode(options, headless):
    if headless.lower() == "true":
        options.add_argument('--headless')
    else:
        options.add_argument('--no-headless')

def get_driver():
    config_dict = {
        "driver": {
            "driver_object": "chrome",
            "driver_path": webdriver_path,
            "driver_headless": "false"
        }
    }
    driver_handler = DriverHandler(config_dict)
    driver_value = driver_handler.get_value("driver", "driver_object")
    driver_path = driver_handler.get_value("driver", "driver_path")
    driver_headless = driver_handler.get_value("driver", "driver_headless")

    if driver_value == "chrome":
        opt = ChromeOptions()
        opt.add_argument('--disable-gpu')
        setup_headless_mode(opt, driver_headless)
        return webdriver.Chrome(executable_path=driver_path, options=opt)
    elif driver_value == "firefox":
        opt = FirefoxOptions()
        setup_headless_mode(opt, driver_headless)
        return webdriver.Firefox(executable_path=driver_path, options=opt)
    else:
        raise ValueError("Unsupported browser type")

