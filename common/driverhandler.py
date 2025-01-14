from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from common.all_file_path import webdriver_path


class DriverHandler:
    def __init__(self, config_dict):
        self.config = config_dict

    def get_value(self, section, key):
        return self.config.get(section, {}).get(key, None)


def setup_headless_mode(options, headless):
    if headless.lower() == "true":
        options.add_argument("--headless")
    else:
        options.add_argument("--no-headless")


def set_download_prefs(options, download_dir):
    prefs = {
        "download.default_directory": download_dir,  # 指定下载目录
        "download.prompt_for_download": True,  # 弹出保存对话框
        "directory_upgrade": True,  # 允许覆盖
        "safebrowsing.enabled": True,  # 禁用安全浏览功能
    }
    options.add_experimental_option("prefs", prefs)


def get_driver():
    config_dict = {
        "driver": {
            "driver_object": "chrome",
            "driver_headless": "false",
            "download.default_directory": r"D:\CODE\SERMATER_YWGLXT\output",
            "driver_path": webdriver_path,
        }
    }
    driver_handler = DriverHandler(config_dict)
    driver_value = driver_handler.get_value("driver", "driver_object")
    driver_path = driver_handler.get_value("driver", "driver_path")
    driver_headless = driver_handler.get_value("driver", "driver_headless")
    download_dir = driver_handler.get_value("driver", "download.default_directory")

    if driver_value == "chrome":
        opt = ChromeOptions()
        opt.add_argument("--disable-gpu")
        setup_headless_mode(opt, driver_headless)
        set_download_prefs(opt, download_dir)
        # return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
        return webdriver.Chrome(executable_path=driver_path, options=opt)
    elif driver_value == "firefox":
        opt = FirefoxOptions()
        setup_headless_mode(opt, driver_headless)
        # Firefox 不支持通过 prefs 设置下载行为，需要使用不同的方法
        # return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opt)
        return webdriver.Firefox(executable_path=driver_path, options=opt)
    else:
        raise ValueError("Unsupported browser type")