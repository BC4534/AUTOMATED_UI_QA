import allure
import pytest

from common.mylogger import Logger
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


@allure.title("新增账号-勾选第一个账号信息，新增账号，勾选数据不应该被覆盖")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="")
class TestAccountManagement08():
    """
    新增账号-勾选第一个账号信息，新增账号，勾选数据不应该被覆盖
    """

    def test_account_management_08(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            old_first_account = account_management_page.account_management_08(data["account"],
                                                                              data["name"],
                                                                              data["password"],
                                                                              data["phone"],
                                                                              data["area"],
                                                                              data["role"],
                                                                              data["remark"]
                                                                              )
            new_first_account = account_management_page.get_first_account_text()
            assert old_first_account != new_first_account
            assert old_first_account == account_management_page.get_second_account_text()
            logger.info(f"{self.__class__.__name__}执行用例成功")
            account_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
