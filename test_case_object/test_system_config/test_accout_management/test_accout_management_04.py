import allure
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import \
    AccountManagementLocator
from test_case_object.conftest import login_driver
from test_case_page.system_configuration.account_management_page import AccountManagementPage


# account,name,password,phone,area,role,remark 临时数据 字典


@allure.title("新增账号,取消按钮")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="暂未解决")
class TestAccountManagement04():
    """
    新增账号，取消按钮
    """

    def test_account_management_04(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page.account_management_04()
            # ('xpath', '//*[@role="dialog"]') 不可见 页面关闭
            assert account_management_page.add_account_element_visible() == True
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
