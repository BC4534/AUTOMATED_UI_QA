import time

import allure
import pytest

from common.loggerhandler import Logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import \
    AccountManagementLocator
from test_case_object.conftest import login_driver
from test_case_page.system_configuration.account_management_page import AccountManagementPage

logger = Logger()
# account,name,password,phone,area,role,remark 临时数据 字典
data = {
    "account": "test_account",
    "name": "test_name",
    "password": "test_password",
    "phone": "test_phone",
    "area": "test_area",
    "role": "test_role",
    "remark": "test_remark"
}
data2 = {
    "account": "test_account2",
    "name": "test_name2",
    "password": "test_password2",
    "phone": "test_phone2",
    "area": "test_area2",
    "role": "test_role2",
    "remark": "test_remark2"
}


@allure.title("编辑功能，编辑后点取消，源数据不应该改")
@allure.feature("账号管理")
class TestAccountManagement16():
    """
    编辑功能，编辑后X，源数据不应该改
    """

    def test_account_management_16(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            account_management_page.account_management_01()
            old_first_account_name = account_management_page.get_first_account_name_text()
            account_management_page.account_management_14(data2["name"],
                                                          data2["password"], data2["phone"],
                                                          data2["area"], data2["role"], data2["remark"]
                                                          )
            account_management_page.click_close_button()

            new_first_account_name = account_management_page.get_first_account_name_text()
            assert old_first_account_name == new_first_account_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
