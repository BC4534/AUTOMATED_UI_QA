import allure
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import \
    AccountManagementLocator
from test_case_object.conftest import login_driver
from test_case_page.system_configuration.account_management_page import AccountManagementPage


# account,name,password,phone,area,role,remark 临时数据 字典
data = {
    "account": "UI自动化测试账号",
    "name": "UI自动化测试名称",
    "password": "123456",
    "phone": "18988889999",
    "email": "123456@qq.com",
    "area": "东部",
    "role": "系统管理员",
    "cloud_platform_account": "",
    "remark": "UI自动化账号管理备注"
}

@allure.title("新增账号,编辑后新增，新增界面不应该有值")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="新增账号，编辑后新增，新增界面不应该有值")
class TestAccountManagement07():
    """
    新增账号,先点编辑，再点新增，新增界面不应该有值
    """

    def test_account_management_07(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page.account_management_07()
            assert account_management_page.get_add_account_account_input_text() == ""
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.error(f"断言失败：{account_management_page.get_add_account_account_input_text()} != '' ")
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
