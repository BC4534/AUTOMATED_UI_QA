import allure

from common.loggerhandler import logger
from test_case_page.project_management.checkitem_configuration_page import (
    CheckItemConfigurationPage,
)

checkitem_data = {
    "checkitem_name": "UI测试新增巡检项",
    "checkitem_type": "UI测试空调系统",
    "checkitem_content": "UI测试新增巡检项描述",
    "checkitem_photo": "是",
    "checkitem_remark": "是",
}


@allure.feature("项目管理")
@allure.story("检查项配置")
@allure.title("新增巡检项")
class TestCheckItemConfiguration02:

    @allure.description("新增巡检项-必填项效验")
    def test_check_item_configuration_02_01(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.click_add_checkitem_button()
            check_item_configuration_page.click_add_checkitem_confirm_button()
            assert (
                check_item_configuration_page.get_add_checkitem_name_required_text()
                == "请输入巡检项名称"
            )
            assert (
                check_item_configuration_page.get_add_checkitem_type_required_text()
                == "请选择巡检项类型"
            )
            assert (
                check_item_configuration_page.get_add_checkitem_content_required_text()
                == "请输入巡检项描述"
            )
            assert (
                check_item_configuration_page.get_add_checkitem_photo_required_text()
                == "请选择是否需要上传拍照信息"
            )
            assert (
                check_item_configuration_page.get_add_checkitem_remark_required_text()
                == "请选择是否需要上传备注"
            )
            check_item_configuration_page.click_add_checkitem_cancel_button()
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("新增巡检项")
            raise e

    @allure.description("新增巡检项-重复新增")
    def test_check_item_configuration_02_02(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            last_name = check_item_configuration_page.get_last_checkitem_name()
            check_item_configuration_page.click_add_checkitem_button()
            check_item_configuration_page.add_checkitem(
                checkitem_name=last_name,
                checkitem_type=checkitem_data["checkitem_type"],
                checkitem_content=checkitem_data["checkitem_content"],
                checkitem_photo=checkitem_data["checkitem_photo"],
                checkitem_remark=checkitem_data["checkitem_remark"],
            )
            check_item_configuration_page.click_add_checkitem_confirm_button()
            assert (
                check_item_configuration_page.get_page_tip_text()
                == "巡检项名称不允许重复"
            )
            check_item_configuration_page.click_add_checkitem_cancel_button()
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("新增巡检项-重复新增")
            raise e

    @allure.description("新增巡检项-新增点击取消")
    def test_check_item_configuration_02_03(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.click_add_checkitem_button()
            check_item_configuration_page.add_checkitem(
                checkitem_name=checkitem_data["checkitem_name"],
                checkitem_type=checkitem_data["checkitem_type"],
                checkitem_content=checkitem_data["checkitem_content"],
                checkitem_photo=checkitem_data["checkitem_photo"],
                checkitem_remark=checkitem_data["checkitem_remark"],
            )
            check_item_configuration_page.click_add_checkitem_cancel_button()
            assert (
                checkitem_data["checkitem_name"]
                not in check_item_configuration_page.get_checkitem_name_list()
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("新增巡检项-新增点击取消")
            raise e

    @allure.description("新增巡检项-新增点击关闭")
    def test_check_item_configuration_02_04(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.click_add_checkitem_button()
            check_item_configuration_page.add_checkitem(
                checkitem_name=checkitem_data["checkitem_name"],
                checkitem_type=checkitem_data["checkitem_type"],
                checkitem_content=checkitem_data["checkitem_content"],
                checkitem_photo=checkitem_data["checkitem_photo"],
                checkitem_remark=checkitem_data["checkitem_remark"],
            )
            check_item_configuration_page.click_add_checkitem_close_button()
            assert (
                checkitem_data["checkitem_name"]
                not in check_item_configuration_page.get_checkitem_name_list()
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("新增巡检项-新增点击取消")
            raise e

    @allure.description("新增巡检项-正常新增")
    def test_check_item_configuration_02_05(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.click_add_checkitem_button()
            check_item_configuration_page.add_checkitem(
                checkitem_name=checkitem_data["checkitem_name"],
                checkitem_type=checkitem_data["checkitem_type"],
                checkitem_content=checkitem_data["checkitem_content"],
                checkitem_photo=checkitem_data["checkitem_photo"],
                checkitem_remark=checkitem_data["checkitem_remark"],
            )
            check_item_configuration_page.click_add_checkitem_confirm_button()
            assert (
                checkitem_data["checkitem_name"]
                in check_item_configuration_page.get_checkitem_name_list()
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("新增巡检项-正常新增")
            raise e

    @allure.description("巡检项-删除巡检项 取消删除")
    def test_check_item_configuration_02_06(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.refresh()
            check_item_configuration_page.check_checkitem_by_name(
                checkitem_data["checkitem_name"]
            )
            check_item_configuration_page.click_delete_checkitem_button()
            check_item_configuration_page.click_delete_checkitem_cancel_button()
            assert (
                checkitem_data["checkitem_name"]
                in check_item_configuration_page.get_checkitem_name_list()
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("巡检项-删除巡检项")
            raise e

    @allure.description("巡检项-删除巡检项")
    def test_check_item_configuration_02_07(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.refresh()
            check_item_configuration_page.check_checkitem_by_name(
                checkitem_data["checkitem_name"]
            )
            check_item_configuration_page.click_delete_checkitem_button()
            check_item_configuration_page.click_delete_checkitem_confirm_button()
            assert (
                checkitem_data["checkitem_name"]
                not in check_item_configuration_page.get_checkitem_name_list()
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("新增巡检项-删除巡检项")
            raise e

    @allure.description("巡检项-编辑巡检项 页面title")
    def test_check_item_configuration_02_08(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.click_first_checkitem_edit_button()
            assert (
                check_item_configuration_page.get_edit_checkitem_title_text()
                == "编辑巡检项"
            )
            check_item_configuration_page.click_add_checkitem_cancel_button()
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("编辑巡检项 页面title")
            raise e

    @allure.description("巡检项-编辑巡检项")
    def test_check_item_configuration_02_09(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            first_name = check_item_configuration_page.get_first_checkitem_name()
            check_item_configuration_page.click_first_checkitem_edit_button()
            check_item_configuration_page.edit_checkitem(
                checkitem_name=first_name + "_UI测试改"
            )
            check_item_configuration_page.click_add_checkitem_confirm_button()
            assert (
                check_item_configuration_page.get_first_checkitem_name()
                == first_name + "_UI测试改"
            )
            check_item_configuration_page.click_first_checkitem_edit_button()
            check_item_configuration_page.edit_checkitem(checkitem_name=first_name)
            check_item_configuration_page.click_add_checkitem_confirm_button()
            assert (
                check_item_configuration_page.get_first_checkitem_name() == first_name
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")

        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png("巡检项-编辑巡检项")
            raise e

    @allure.description("巡检项-编辑巡检项 点击取消")
    def test_check_item_configuration_02_10(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            first_name = check_item_configuration_page.get_first_checkitem_name()
            check_item_configuration_page.click_first_checkitem_edit_button()
            check_item_configuration_page.edit_checkitem(
                checkitem_name=first_name + "_UI测试改"
            )
            check_item_configuration_page.click_add_checkitem_cancel_button()
            assert (
                check_item_configuration_page.get_first_checkitem_name()
                != first_name + "_UI测试改"
            )
            assert (
                check_item_configuration_page.get_first_checkitem_name() == first_name
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png(
                "巡检项-编辑巡检项 点击取消"
            )
            raise e

    @allure.description("巡检项-编辑巡检项 点击关闭")
    def test_check_item_configuration_02_11(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            first_name = check_item_configuration_page.get_first_checkitem_name()
            check_item_configuration_page.click_first_checkitem_edit_button()
            check_item_configuration_page.edit_checkitem(
                checkitem_name=first_name + "_UI测试改"
            )
            check_item_configuration_page.click_add_checkitem_close_button()
            assert (
                check_item_configuration_page.get_first_checkitem_name()
                != first_name + "_UI测试改"
            )
            assert (
                check_item_configuration_page.get_first_checkitem_name() == first_name
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png(
                "巡检项-编辑巡检项 点击关闭"
            )
            raise e

    @allure.description("巡检项-删除巡检项,不勾选数据直接点击删除")
    def test_check_item_configuration_02_12(self, login_driver):
        check_item_configuration_page = CheckItemConfigurationPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            check_item_configuration_page.switch_to_resources_inventory_page()
            check_item_configuration_page.click_delete_checkitem_button()
            assert (
                check_item_configuration_page.get_page_tip_text()
                == "请选择需要删除的巡检项配置"
            )
            logger.error(f"{self.__class__.__name__} 执行用例成功")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 执行用例失败,错误信息为：{e}")
            check_item_configuration_page.get_screenshot_png(
                "巡检项-删除巡检项,不勾选数据直接点击删除"
            )
            raise e
