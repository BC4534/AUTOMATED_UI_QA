import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger


data = {"name": "测试角色", "remark": "测试角色备注"}


@allure.title(
    "角色管理-新增角色：勾选第一条角色数据，正常填写新增数据，第一条数据不应该被覆盖"
)
@allure.feature("角色管理")
class TestRoleManagment07:
    """
    角色管理-新增角色：勾选第一条角色数据，正常填写新增数据，第一条数据不应该被覆盖
    断言： 通过判断操作前第一个数据是不是与操作后的第二个数据一致
    """

    def test_role_management_07(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_01()
            first_role_name = role_management_page.get_first_role_name()
            role_management_page.role_management_07(data["name"], data["remark"])
            second_role_name = role_management_page.get_second_role_name()
            assert first_role_name == second_role_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
            role_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
