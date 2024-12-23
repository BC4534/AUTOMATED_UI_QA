import allure
import pytest

from common.loggerhandler import Logger
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


@allure.title("新增账号")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="暂不执行")
class TestAccountManagement02():
    """
    +--------------+-------------------+------------+-----------------------------------+--------+---------------------------------------+--------------------------------------+
    | 功能模块     | 测试点           | 用例ID       | 测试描述                           | 优先级 | 预置条件                             | 测试步骤                             | 预期结果                                      |
    +==============+===================+============+===================================+========+=======================================+======================================+==============================================+
    | 新增账号     | 新增账号页面弹窗   | 24XT03592    | 验证弹出“新增账号”界面功能正常       | 高     | 1.已进入系统的账号管理界面           | 1.点击新增按钮                       | 弹出“新增账号”界面                           |
    | 新增账号     | 界面显示         | 24XT03593    | 验证新增账号界面显示正常             | 高     | 1.已进入新增账号界面                 | 观察“新增账号”界面                   | 文字正确，该有的按钮和控件齐全，输入框和选择框有输入提示 |
    +--------------+-------------------+------------+-----------------------------------+--------+---------------------------------------+--------------------------------------+
     """

    def test_account_management_02(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            account_management_page.account_management_01()
            account_management_page.account_management_02(account=data["account"],
                                                          name=data["name"],
                                                          password=data["password"],
                                                          phone=data["phone"],
                                                          area=data["area"],
                                                          role=data["role"],
                                                          remark=data["remark"]
                                                          )
            assert account_management_page.get_page_tip() == "操作成功"
            logger.info(f"{self.__class__.__name__}执行用例成功")
            account_management_page.test_case_data_recover()

        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
