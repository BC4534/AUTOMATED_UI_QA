import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger


data = {"name": "测试角色", "remark": "测试角色备注"}


@allure.title("角色管理-删除角色-直接点击删除按钮")
@allure.feature("角色管理")
class TestRoleManagment08:
    """
    角色管理-删除角色-直接点击删除按钮
    断言： 界面提示语 请先勾选需要删除的数据
    """

    def test_role_management_08(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_08()
            assert role_management_page.get_page_tip() == "请先勾选需要删除的数据"
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
