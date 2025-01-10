import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger


@allure.feature("系统配置")
@allure.story("角色管理")
@allure.title("角色管理-新增角色：必填项效验")
class TestRoleManagment03:
    """
    角色管理-新增角色：必填项效验
    """

    @allure.step("角色管理-新增角色：必填项效验")
    def test_role_management_03(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_03()
            assert role_management_page.get_add_role_name_required() == "请输入角色名称"
            assert (
                role_management_page.get_add_role_remark_required() == "请输入角色说明"
            )
            # 点击取消按钮，关闭新增角色弹框
            role_management_page.click_cancel_button()
            logger.info(f"{self.__class__.__name__}执行用例成功")
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
