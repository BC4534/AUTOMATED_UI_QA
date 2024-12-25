import allure
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import \
    AccountManagementLocator
from test_case_page.system_configuration.account_management_page import AccountManagementPage


@allure.title("删除账号，不勾选数据，直接点击删除按钮")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="")
class TestAccountManagement09():
    """
    删除账号，不勾选数据，直接点击删除按钮
    """

    def test_account_management_09(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            account_management_page.account_management_09()
            assert account_management_page.get_page_tip() == '请先勾选需要删除的数据'
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
