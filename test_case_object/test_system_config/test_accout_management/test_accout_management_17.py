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
    "account": "admin",
    "name": "系统管理员",
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


@allure.title("账号管理，搜索组件")
@allure.feature("账号管理")
class TestAccountManagement17:
    """
    搜索组件，账号、姓名、绑定角色、管辖区域、搜索、重置
    实现思路，基于已有账号信息，执行搜索操作，
    搜索系统管理员信息，新增账号在最前面
    """

    # 通过账号搜索
    def test_account_management_17_1(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.test_account_management_17_1.__name__}开始执行用例")
            account_management_page.account_management_01()
            first_account = account_management_page.account_management_17_1(
                data["account"]
            )
            assert data["account"] in first_account
            logger.info(f"{self.test_account_management_17_1.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.test_account_management_17_1.__name__}执行用例失败")
            account_management_page.get_screenshot_png(
                f"{self.test_account_management_17_1.__name__}"
            )
            raise e

    # 通过姓名搜索
    def test_account_management_17_2(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.test_account_management_17_2.__name__}开始执行用例")
            account_management_page.account_management_01()
            first_name = account_management_page.account_management_17_2(data["name"])
            assert data["name"] in first_name
            logger.info(f"{self.test_account_management_17_2.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.test_account_management_17_2.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 通过绑定角色搜索
    def test_account_management_17_3(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.test_account_management_17_3.__name__}开始执行用例")
            account_management_page.account_management_01()
            first_role = account_management_page.account_management_17_3(data["role"])
            assert data["role"] in first_role
            logger.info(f"{self.test_account_management_17_3.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.test_account_management_17_3.__name__}执行用例失败")
            account_management_page.get_screenshot_png(
                f"{self.test_account_management_17_3.__name__}"
            )
            raise e

    # 通过管辖区域搜索
    def test_account_management_17_4(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.test_account_management_17_4.__name__}开始执行用例")
            account_management_page.account_management_01()
            first_area = account_management_page.account_management_17_4(data["area"])
            assert data["area"] in first_area
            logger.info(f"{self.test_account_management_17_4.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.test_account_management_17_4.__name__}执行用例失败")
            account_management_page.get_screenshot_png(
                f"{self.test_account_management_17_4.__name__}"
            )
            raise e

    # 验证重置按钮
    def test_account_management_17_reset(self, login_driver):
        account_management_page = AccountManagementPage(login_driver)
        try:
            logger.info(f"{self.test_account_management_17_reset.__name__}开始执行用例")
            account_management_page.account_management_01()
            first_account = account_management_page.test_account_management_17_reset(
                data["account"], data["name"], data["role"], data["area"]
            )
            assert first_account == ""
            logger.info(f"{self.test_account_management_17_reset.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.test_account_management_17_reset.__name__}执行用例失败")
            account_management_page.get_screenshot_png(
                f"{self.test_account_management_17_reset.__name__}"
            )
            raise e
