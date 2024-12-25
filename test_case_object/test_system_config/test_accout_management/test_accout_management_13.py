import allure
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import \
    AccountManagementLocator
from test_case_page.system_configuration.account_management_page import AccountManagementPage


data = {
    "account": "test_account_management_12",
    "name": "test_account_management_12",
    "password": "test_account_management_12",
    "phone": "18711112222",
    "area": "test_account_management_12",
    "email": "management_12@qq.com",
    "role": "",
    "cloud_platform": "",
    "remark": "test_account_management_12"
}
data2 = {
    "account": "test_account_management_12_2",
    "name": "test_account_management_12_2",
    "password": "test_account_management_12_2",
    "phone": "17612201220",
    "area": "test_account_management_12_2",
    "email": "management_12_2@qq.com",
    "role": "",
    "cloud_platform": "",
    "remark": "test_account_management_12_2"
}


@allure.title("验证全选按钮")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="")
class TestAccountManagement13():
    """
    验证全选按钮
    """

    def test_account_management_13(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page.account_management_01()
            account_management_page.account_management_13()
            assert account_management_page.get_batch_delete_button_count()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
