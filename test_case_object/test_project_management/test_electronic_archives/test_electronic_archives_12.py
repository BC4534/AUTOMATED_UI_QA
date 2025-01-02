import allure

from test_case_locator.project_management.electronic_archives_locator.supplier_maintenance_locator import \
    SupplierMaintenanceLocator
from test_case_page.project_management.electronic_archives_page.add_operation_maintenance_management_info_page import \
    AddOperationMaintenanceManagementInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_basic_info_page import \
    AddProjectBaseInfoPage
from test_case_page.project_management.electronic_archives_page.add_project_detail_info_page import \
    AddProjectDetailInfoPage
from test_case_page.project_management.electronic_archives_page.electronic_archives_page import ElectronicArchivesPage
from common.loggerhandler import logger
from test_case_page.project_management.electronic_archives_page.supplier_maintenance_page import SupplierMaintenancePage


@allure.feature("项目管理模块")
@allure.story("电子档案功能")
@allure.title("供应商维护")
class TestElectronicArchives12:

    @allure.description("进入供应商维护界面,查看界面标题，及通过点击X按钮，关闭界面")
    def test_electronic_archives_12_1(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.get_supplier_maintenance_title() == "供应商维护"
            supplier_maintenance_page.supplier_maintenance_click_close_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面,查看界面标题，及通过点击取消按钮，关闭界面")
    def test_electronic_archives_12_2(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.get_supplier_maintenance_title() == "供应商维护"
            supplier_maintenance_page.supplier_maintenance_click_cancel_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，新增供应商必填项效验")
    def test_electronic_archives_12_3(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.supplier_maintenance_add_supplier_required_item_validation()
            assert supplier_maintenance_page.supplier_maintenance_get_supplier_name_required_text() == "供应商名称 是必填的!!"
            assert supplier_maintenance_page.supplier_maintenance_get_supplier_type_required_text() == "供货范围 是必填的!!"
            supplier_maintenance_page.supplier_maintenance_click_cancel_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，正常新增供应商信息，保存")
    def test_electronic_archives_12_4(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.test_electronic_archives_12_4("UI_TEST_supplier_name", "BMS")
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_name() == "UI_TEST_supplier_name"
            supplier_maintenance_page.supplier_maintenance_click_delete_button()
            supplier_maintenance_page.supplier_maintenance_click_confirm_delete_button()
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，新增供应商姓名重复")
    def test_electronic_archives_12_5(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.test_electronic_archives_12_5("UI_TEST_supplier_name", "BMS")
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
            assert "名称重复" in supplier_maintenance_page.get_page_tip_text()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，删除供应商信息")
    def test_electronic_archives_12_6(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            name = supplier_maintenance_page.temp_supplier_maintenance()
            supplier_maintenance_page.delete_supplier_maintenance()
            supplier_maintenance_page.supplier_maintenance_click_confirm_delete_button()
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_name() != name
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，删除供应商信息,点击删除，点击取消删除")
    def test_electronic_archives_12_7(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            name = supplier_maintenance_page.temp_supplier_maintenance()
            supplier_maintenance_page.delete_supplier_maintenance()
            supplier_maintenance_page.supplier_maintenance_click_cancel_delete_button()
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_name() == name
            supplier_maintenance_page.delete_temp_supplier_maintenance()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，删除供应商信息,点击删除，点击确认删除，但是没有点击最后的确认按钮")
    def test_electronic_archives_12_8(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            name = supplier_maintenance_page.temp_supplier_maintenance()
            supplier_maintenance_page.delete_supplier_maintenance()
            supplier_maintenance_page.supplier_maintenance_click_confirm_delete_button()
            supplier_maintenance_page.supplier_maintenance_click_cancel_button()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_name() == name
            supplier_maintenance_page.supplier_maintenance_click_cancel_button()
            supplier_maintenance_page.delete_temp_supplier_maintenance()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            if supplier_maintenance_page.visibility_of_element_located(
                    SupplierMaintenanceLocator.supplier_maintenance_title_loc):
                supplier_maintenance_page.supplier_maintenance_click_cancel_button()
            supplier_maintenance_page.delete_temp_supplier_maintenance()
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，清空供应商信息 ")
    def test_electronic_archives_12_10(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            supplier_maintenance_page.supplier_maintenance_click_clear_button()
            supplier_maintenance_page.supplier_maintenance_click_confirm_delete_button()
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_name() == ""
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_type() == ""
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
            assert "供货范围不能为空" in supplier_maintenance_page.get_page_tip_text()
            supplier_maintenance_page.supplier_maintenance_click_cancel_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，编辑供应商信息 取消操作")
    def test_electronic_archives_12_11(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            old_name = supplier_maintenance_page.supplier_maintenance_edit_supplier_name("UI测试临时供应商")
            supplier_maintenance_page.supplier_maintenance_click_cancel_button()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_name() == old_name
            supplier_maintenance_page.supplier_maintenance_click_cancel_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，编辑供应商信息 确认操作")
    def test_electronic_archives_12_12(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            old_name = supplier_maintenance_page.supplier_maintenance_edit_supplier_name("UI测试临时供应商")
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            assert supplier_maintenance_page.supplier_maintenance_get_first_supplier_name() == "UI测试临时供应商"
            supplier_maintenance_page.switch_to_supplier_maintenance()
            _ = supplier_maintenance_page.supplier_maintenance_edit_supplier_name(old_name)
            supplier_maintenance_page.supplier_maintenance_click_confirm_button()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e

    @allure.description("进入供应商维护界面，连续点击添加按钮")
    def test_electronic_archives_12_13(self, login_driver):
        supplier_maintenance_page = SupplierMaintenancePage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            supplier_maintenance_page.switch_to_electronic_archives()
            supplier_maintenance_page.switch_to_supplier_maintenance()
            supplier_maintenance_page.supplier_maintenance_click_add_button()
            supplier_maintenance_page.supplier_maintenance_click_add_button()
            assert supplier_maintenance_page.get_page_tip_text() == "当前在编辑状态，不可操作"
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            supplier_maintenance_page.get_screenshot_png(f"{self.__class__.__name__}")
            raise e
