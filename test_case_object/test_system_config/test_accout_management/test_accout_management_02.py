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


@allure.title("新增账号,正常新增")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="暂不执行")
class TestAccountManagement02:
    """
    +--------------+-------------------+------------+-----------------------------------+--------+---------------------------------------+--------------------------------------+
    | 功能模块     | 测试点           | 用例ID       | 测试描述                           | 优先级 | 预置条件                             | 测试步骤                             | 预期结果                                      |
    +==============+===================+============+===================================+========+=======================================+======================================+==============================================+
    | 新增账号     | 新增账号页面弹窗   | 24XT03592    | 验证弹出“新增账号”界面功能正常       | 高     | 1.已进入系统的账号管理界面           | 1.点击新增按钮                       | 弹出“新增账号”界面                           |
    | 新增账号     | 界面显示         | 24XT03593    | 验证新增账号界面显示正常             | 高     | 1.已进入新增账号界面                 | 观察“新增账号”界面                   | 文字正确，该有的按钮和控件齐全，输入框和选择框有输入提示 |
    +--------------+-------------------+------------+-----------------------------------+--------+---------------------------------------+--------------------------------------+
    """

    def test_account_management_02(self, login_driver):
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
            assert account_management_page.get_page_tip() == "操作成功"
            logger.info(f"{self.__class__.__name__}执行用例成功")
            account_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
