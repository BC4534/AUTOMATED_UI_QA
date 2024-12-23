import allure
from test_case_page.system_configuration.role_management_page import RoleManagementPage
from common.loggerhandler import logger



data = {
    "name": "测试角色",
    "remark": "测试角色备注"
}
data2 = {
    "name": "测试角色2",
    "remark": "测试角色备注2"
}


@allure.title("角色管理-编辑角色")
@allure.feature("角色管理")
class TestRoleManagment13():
    """
    角色管理-删除角色批量删除
    实现思路 ： 先自己新增1条 再编辑
    断言 ：

    """
    # 编辑后确认
    def test_role_management_13_1(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_01()
            role_management_page.role_management_11(data["name"], data["remark"])
            old_first_role_name = role_management_page.get_first_role_name()
            role_management_page.role_management_13(data2["name"], data2["remark"])
            role_management_page.click_confirm_button()
            new_first_role_name = role_management_page.get_first_role_name()
            assert old_first_role_name != new_first_role_name
            assert new_first_role_name == data2["name"]
            logger.info(f"{self.__class__.__name__}执行用例成功")
            role_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
    # 编辑后取消
    def test_role_management_13_2(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_11(data["name"], data["remark"])
            old_first_role_name = role_management_page.get_first_role_name()
            role_management_page.role_management_13(data2["name"], data2["remark"])
            role_management_page.click_cancel_button()
            new_first_role_name = role_management_page.get_first_role_name()
            assert old_first_role_name == new_first_role_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
            role_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    # 编辑后关闭
    def test_role_management_13_3(self, login_driver):
        role_management_page = RoleManagementPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__}开始执行用例")
            role_management_page.role_management_11(data["name"], data["remark"])
            old_first_role_name = role_management_page.get_first_role_name()
            role_management_page.role_management_13(data2["name"], data2["remark"])
            role_management_page.click_close_button()
            new_first_role_name = role_management_page.get_first_role_name()
            assert old_first_role_name == new_first_role_name
            logger.info(f"{self.__class__.__name__}执行用例成功")
            role_management_page.test_case_data_recover()
        except Exception as e:
            logger.info(f"{self.__class__.__name__}执行用例失败")
            role_management_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e