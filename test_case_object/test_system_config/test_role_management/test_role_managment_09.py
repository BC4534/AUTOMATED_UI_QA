import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger


data = {"name": "测试角色", "remark": "测试角色备注"}


@allure.title("角色管理-删除角色")
@allure.feature("角色管理")
class TestRoleManagment09:
    """
    角色管理-删除角色
    实现思路 ： 先自己新增一条 再删掉
    断言 ： 新增前的第一条 和删除后的第一条数据一致

    """

    def test_role_management_09(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_01()
            old_first_role_name = role_management_page.get_first_role_name()
            role_management_page.role_management_09(data["name"], data["remark"])
            new_first_role_name = role_management_page.get_first_role_name()
            assert old_first_role_name == new_first_role_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
