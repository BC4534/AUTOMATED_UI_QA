import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger

data = {"name": "UI测试新增不保存角色", "remark": "UI测试新增不保存角色"}


@allure.feature("系统配置")
@allure.story("角色管理")
@allure.title("角色管理-新增角色：正常填写新增数据，后点关闭")
class TestRoleManagment04:
    """
    角色管理-新增角色：正常填写新增数据，后点关闭
    断言： 通过判断操作前后，第一个角色是否一致
    """

    @allure.description("角色管理-新增角色：正常填写新增数据，后点关闭")
    def test_role_management_04(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_01()
            old_first_role_name = role_management_page.get_first_role_name()
            role_management_page.role_management_04(data["name"], data["remark"])
            new_first_role_name = role_management_page.get_first_role_name()
            assert old_first_role_name == new_first_role_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
