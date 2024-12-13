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


@allure.title("角色管理-删除角色,删除防御")
@allure.feature("角色管理")
class TestRoleManagment12():
    """
    角色管理-删除角色批量删除 删除防御
    实现思路 ： 全选删除
    断言 ： 界面提示：系统管理员为受保护角色, 不允许删除!
                    [项目中心执行角色]]在使用中无法删除

    """

    def test_role_management_12(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page = RoleManagementPage(login_driver)
            role_management_page.role_management_12()
            assert role_management_page.get_page_tip() in ["系统管理员为受保护角色, 不允许删除!","在使用中无法删除"]
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

