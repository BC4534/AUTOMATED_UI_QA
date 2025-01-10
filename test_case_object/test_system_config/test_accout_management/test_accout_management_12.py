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
    "account": "test_account_management_12",
    "name": "test_account_management_12",
    "password": "test_account_management_12",
    "phone": "18711112222",
    "area": "test_account_management_12",
    "email": "management_12@qq.com",
    "role": "",
    "cloud_platform": "",
    "remark": "test_account_management_12",
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
    "remark": "test_account_management_12_2",
}


@allure.title("删除账号，批量删除")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="")
class TestAccountManagement12:
    """
    批量删除账号，勾选前两个账号，点击删除
    实现思路：为不影响原有数据，先新增两个，再删除
    """

    def test_account_management_12(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page.account_management_01()
            account_management_page.account_management_02(
                account=data["account"],
                name=data["name"],
                password=data["password"],
                phone=data["phone"],
                area=data["area"],
                email=data["email"],
                role=data["role"],
                cloud_platform=data["cloud_platform"],
                remark=data["remark"],
            )
            account_management_page.account_management_02(
                account=data2["account"],
                name=data2["name"],
                password=data2["password"],
                phone=data2["phone"],
                area=data2["area"],
                email=data2["email"],
                role=data2["role"],
                cloud_platform=data2["cloud_platform"],
                remark=data2["remark"],
            )

            account_management_page.account_management_12()
            assert account_management_page.get_page_tip() == "删除成功"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
