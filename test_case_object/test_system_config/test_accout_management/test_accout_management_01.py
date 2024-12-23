import allure
import pytest
from common.driverhandler import get_driver
from common.loggerhandler import Logger
from test_case_object.conftest import login_driver
from test_case_page.system_configuration.account_management_page import AccountManagementPage

logger = Logger()

@allure.title("账号管理-账号管理界面跳转，页面展示")
@allure.feature("账号管理")
# @pytest.mark.skip(reason="跳过用例")

class TestAccountManagement01():
    """
测试用例信息表：
| 功能模块   | 测试点     | 用例ID     | 预置条件                       | 测试步骤         | 预期结果                   |
|----------|-----------|------------|------------------------------|-----------------|--------------------------|
| 账号管理   | 界面跳转   | 24XT03574  | 1.成功登录系统 2.不在账号管理界面 | 点击账号管理      | 跳转到账号管理界面           |
| 账号管理   | 界面显示   | 24XT03575  | 1.已进入首页界面                | 观察界面显示      | 界面显示正常，与需求文档描述一致|
"""



    def test_account_management_01(self,login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            account_management_page = AccountManagementPage(login_driver)
            account_management_page.account_management_01()
            assert account_management_page.assert_account_management_01() == "新增账号"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            account_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e







