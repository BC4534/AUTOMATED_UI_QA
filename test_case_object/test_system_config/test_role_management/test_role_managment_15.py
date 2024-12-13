import allure

from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.mylogger import Logger

logger = Logger()

data = {
    "name": "测试角色",
    "remark": "测试角色备注"
}
data2 = {
    "name": "测试角色2",
    "remark": "测试角色备注2"
}


@allure.title("角色管理-新增角色")
@allure.feature("角色管理")
class TestRoleManagment15():
    """
    角色管理-新增角色界面文本信息
    实现思路 ：
    断言 ：

    """

    def test_role_management_15(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page = RoleManagementPage(login_driver)
            assert role_management_page.role_management_15()  == "新增角色"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

