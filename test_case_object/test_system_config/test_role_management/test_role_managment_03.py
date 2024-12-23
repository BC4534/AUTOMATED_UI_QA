import allure

from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import Logger


logger = Logger()

data = {
    "name": "测试角色",
    "remark": "测试角色备注"
}

@allure.title("角色管理-新增角色：必填项效验")
@allure.feature("角色管理")
class TestRoleManagment03():
    """
    角色管理-新增角色：必填项效验
    """
    
    def test_role_management_03(self, login_driver):
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page = RoleManagementPage(login_driver)
            role_management_page.role_management_03()
            assert role_management_page.get_add_role_name_required() == "请输入角色名称"
            assert role_management_page.get_add_role_remark_required() == "请输入角色说明"
            logger.info(f"{self.__class__.__name__}执行用例成功")

        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
