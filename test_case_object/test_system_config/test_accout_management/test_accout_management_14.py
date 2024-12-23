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


@allure.title("编辑账号，正常编辑")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="编辑的sendkesy有点问题，后面看")
class TestAccountManagement14():
    """
    编辑功能，正常编辑
    """

    def test_account_management_14(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            account_management_page.account_management_01()
            account_management_page.account_management_02(data["account"], data["name"],
                                                          data["password"], data["phone"],
                                                          data["area"], data["role"], data["remark"])

            account_management_page.account_management_14(data2["name"],
                                                          data2["password"], data2["phone"],
                                                          data2["area"], data2["role"], data2["remark"]
                                                          )
            account_management_page.click_confirm_button()

            assert account_management_page.get_page_tip() == "操作成功"
            logger.info(f"{self.__class__.__name__}执行用例成功")
            account_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
