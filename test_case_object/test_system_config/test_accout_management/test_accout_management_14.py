import allure
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import (
    AccountManagementLocator,
)
from test_case_page.system_configuration.account_management_page import (
    AccountManagementPage,
)


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


@allure.title("编辑账号，正常编辑")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="编辑的sendkesy有点问题，后面看")
class TestAccountManagement14:
    """
    编辑功能，正常编辑
    实现思路，先正常新增一个，再编辑
    """

    def test_account_management_14(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page.account_management_01()
            account_management_page.account_management_02(
                account=data["account"],
                name=data["name"],
                password=data["password"],
                phone=data["phone"],
                email=data["email"],
                area=data["area"],
                role=data["role"],
                cloud_platform=data["cloud_platform_account"],
                remark=data["remark"],
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
            account_management_page.click_confirm_button()

            assert account_management_page.get_page_tip() == "操作成功"
            logger.info(f"{self.__class__.__name__}执行用例成功")
            account_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
