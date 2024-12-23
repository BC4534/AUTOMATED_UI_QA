import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger


data = {
    "name": "测试角色",
    "remark": "测试角色备注"
}


@allure.title("角色管理-新增角色：重复新增")
@allure.feature("角色管理")
class TestRoleManagment10():
    """
    角色管理-新增角色：重复新增
    断言： 名称不允许重复
    """

    def test_role_management_10(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_10(data["name"], data["remark"])
            assert role_management_page.get_page_tip() == "名称不允许重复"
            logger.info(f"{self.__class__.__name__}执行用例成功")
            role_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

