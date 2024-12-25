import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger



data = {
    "name": "测试角色",
    "remark": "测试角色备注"
}


@allure.title("角色管理-新增角色：编辑后新增")
@allure.feature("角色管理")
class TestRoleManagment06():
    """
    角色管理-新增角色：角色管理-新增角色：编辑后新增
    断言： 新增界面不应该出现编辑角色的数据
    """

    def test_role_management_06(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            assert role_management_page.role_management_06() == ""
            role_management_page.click_cancel_button() # 点击取消按钮 关闭新增界面
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

