import allure
from common.loggerhandler import logger
from test_case_page.system_configuration.account_management_page import (
    AccountManagementPage,
)


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
    "remark": "UI自动化账号管理备注",
}


@allure.title("新增账号,重复新增")
@allure.feature("账号管理")
class TestAccountManagement06:
    """
    新增账号，重复新增
    """

    def test_account_management_06(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page.account_management_06(
                data["account"],
                data["name"],
                data["password"],
                data["phone"],
                data["email"],
                data["area"],
                data["role"],
                data["cloud_platform_account"],
                data["remark"],
            )
            assert account_management_page.get_page_tip() == "账号不允许重复"
            logger.info(f"{self.__class__.__name__}执行用例成功")
            account_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
