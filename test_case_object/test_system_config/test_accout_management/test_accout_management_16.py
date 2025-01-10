import time
import allure
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import (
    AccountManagementLocator,
)
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
data2 = {
    "name": "UI自动化测试名称_编辑",
    "password": "123456",
    "phone": "18988889999",
    "email": "123456@qq.com",
    "area": "东部",
    "role": "系统管理员",
    "cloud_platform_account": "",
    "remark": "UI自动化账号管理备注_编辑",
}


@allure.title("编辑功能，编辑后点取消，源数据不应该改")
@allure.feature("账号管理")
class TestAccountManagement16:
    """
    编辑功能，编辑后X，源数据不应该改
    """

    def test_account_management_16(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page.account_management_01()
            old_first_account_name = (
                account_management_page.get_first_account_name_text()
            )
            account_management_page.account_management_14(
                name=data2["name"],
                password=data2["password"],
                email=data2["email"],
                phone=data2["phone"],
                area=data2["area"],
                role=data2["role"],
                cloud_platform=data2["cloud_platform_account"],
                remark=data2["remark"],
            )
            account_management_page.click_close_button()

            new_first_account_name = (
                account_management_page.get_first_account_name_text()
            )
            assert old_first_account_name == new_first_account_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
