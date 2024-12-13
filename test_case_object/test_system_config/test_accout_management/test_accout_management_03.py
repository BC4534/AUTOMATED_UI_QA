import allure
import pytest

from common.mylogger import Logger
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


@allure.title("新增账号,必填项效验")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="暂不执行")
class TestAccountManagement03():
    """
    新增账号，必填项效验
    请输入账号，请输入密码，请输入姓名，请输入关联手机号，请选择绑定的角色
    """

    def test_account_management_03(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            account_management_page.account_management_03()
            assert account_management_page.get_account_required_tip() == "请输入账号"
            assert account_management_page.get_password_required_tip() == "请输入密码"
            assert account_management_page.get_name_required_tip() == "请输入姓名"
            assert account_management_page.get_phone_required_tip() == "请输入关联手机号"
            assert account_management_page.get_area_required_tip() == "请选择管辖区域"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
