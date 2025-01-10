import time
import allure
from selenium.webdriver.common.by import By
from common.base_method import BasePage
from common.loggerhandler import logger
from test_case_locator.system_configuration.account_management_locator.account_management_locator import (
    AccountManagementLocator,
)


class AccountManagementPage(BasePage):
    def get_system_config_module_class_attributes(self):
        # system_config_module_class_attributes_loc = (By.XPATH, '//*[text()="系统配置"]/../..')
        return self.get_attribute(
            AccountManagementLocator.system_config_module_class_attributes_loc, "class"
        )  #

    # 账号管理-账号管理页面跳转
    def account_management_01(self):
        if (
            self.get_system_config_module_class_attributes()
            == "ant-menu-submenu ant-menu-submenu-inline"
        ):
            self.click_system_config()
        self.click_account_management()

    # 页面跳转断言  使用新增账号按钮的文本
    def assert_account_management_01(self):
        return self.get_add_account_button_text()

    # 账号管理-新增账号
    def account_management_02(
        self, account, name, password, phone, email, area, role, cloud_platform, remark
    ):
        self.click_add_account_button()
        self.fill_add_account_data(
            account, name, password, phone, email, area, role, cloud_platform, remark
        )
        self.click_confirm_button()
        time.sleep(1.5)

    # 删除用例新增的数据
    def test_case_data_recover(self):
        self.refresh()
        time.sleep(1)
        self.check_the_first_account_checkbox()

        self.click_batch_delete_button()
        time.sleep(0.5)
        self.click_confirm_batch_delete_button()
        time.sleep(3)

    # 新增账号，必填项效验证
    def account_management_03(self):
        self.account_management_01()
        self.click_add_account_button()
        self.click_confirm_button()

    # 新增账号，效验取消按钮
    def account_management_04(self):
        self.account_management_01()
        self.click_add_account_button()
        self.click_cancel_button()
        time.sleep(2)

    # 判断新增账号界面元素是否可见
    def add_account_element_visible(self):
        return self.invisibility_of_element_located(
            AccountManagementLocator.add_account_element_loc
        )

    # 新增账号，效验X按钮
    def account_management_05(self):
        self.account_management_01()
        self.click_add_account_button()
        self.click_close_button()
        time.sleep(2)

    # 新增账号，重复新增
    # 不依赖已有数据，完全重来
    def account_management_06(
        self, account, name, password, phone, email, area, role, cloud_platform, remark
    ):
        self.account_management_01()
        self.account_management_02(
            account, name, password, phone, email, area, role, cloud_platform, remark
        )
        self.click_add_account_button()
        self.fill_add_account_data(
            account, name, password, phone, email, area, role, cloud_platform, remark
        )
        self.click_confirm_button()

    # 先点击编辑，再点新增，新增框不应该有值
    def account_management_07(self):
        self.account_management_01()
        self.click_first_edit_button()
        self.click_cancel_button()
        self.click_add_account_button()

    # 新增账号-勾选第一个账号信息，新增账号，勾选数据不应该被覆盖
    def account_management_08(
        self, account, name, password, phone, email, area, role, cloud_platform, remark
    ):
        self.account_management_01()
        first_account = self.get_first_account_text()
        # 勾选第一个复选框
        self.check_the_first_account_checkbox()
        self.account_management_02(
            account, name, password, phone, email, area, role, cloud_platform, remark
        )
        time.sleep(1)
        self.refresh()
        return first_account

    def account_management_09(self):
        self.account_management_01()
        self.click_batch_delete_button()
        time.sleep(1)

    def account_management_10(self):
        self.account_management_01()
        self.click_add_account_button()
        self.fill_add_account_data(
            "UI自动化测试账号",
            "UI自动化测试名称",
            "123456",
            "18988889999",
            "123456@qq.com",
            "东部",
            "系统管理员",
            "",
            "UI自动化账号管理备注",
        )
        self.click_confirm_button()
        time.sleep(1)
        self.refresh()
        time.sleep(1)
        self.check_the_first_account_checkbox()

        self.click_batch_delete_button()
        time.sleep(0.5)
        self.click_confirm_batch_delete_button()

    def account_management_11(self):
        self.check_the_first_account_checkbox()
        self.click_batch_delete_button()
        time.sleep(0.5)
        self.click_cancel_batch_delete_button()

    def account_management_12(self):
        self.refresh()
        time.sleep(3)
        self.check_the_first_account_checkbox()
        time.sleep(0.5)
        self.check_the_first_account_checkbox()
        time.sleep(0.5)
        self.click_batch_delete_button()
        time.sleep(0.5)
        self.click_confirm_batch_delete_button()

    def account_management_13(self):
        self.check_all_account_checkbox()

    def account_management_14(
        self, name, password, phone, email, area, role, cloud_platform, remark
    ):
        time.sleep(1)
        self.click_first_edit_button()
        self.fill_edit_account_data(
            name=name,
            password=password,
            phone=phone,
            email=email,
            area=area,
            role=role,
            cloud_platform=cloud_platform,
            remark=remark,
        )
        # self.click_add_account_confirm_button()

    def account_management_17_1(self, account):
        self.click_reset_button()
        self._select_account_data_by_account(account)
        self.click_search_button()
        time.sleep(3)
        return self.get_first_account_text()

    def account_management_17_2(self, name):
        self.click_reset_button()
        self._select_account_data_by_name(name)
        self.click_search_button()
        time.sleep(3)
        return self.get_first_account_name_text()

    def account_management_17_3(self, role):
        self.click_reset_button()
        self._select_account_data_by_role(role)
        self.click_search_button()
        time.sleep(3)
        return self.get_first_account_role_text()

    def account_management_17_4(self, area):
        self.click_reset_button()
        self._select_account_data_by_area(area)
        self.click_search_button()
        time.sleep(3)
        return self.get_first_account_area_text()

    def test_account_management_17_reset(self, account, name, role, area):
        self.click_reset_button()
        time.sleep(0.5)
        self._select_account_data_by_account(account)
        time.sleep(0.5)
        self._select_account_data_by_name(name)
        time.sleep(0.5)
        self._select_account_data_by_role(role)
        time.sleep(0.5)
        self._select_account_data_by_area(area)
        time.sleep(0.5)
        self.click_reset_button()
        time.sleep(0.5)
        return self.text(AccountManagementLocator.search_account_input_loc)

    # 账号管理界面，通过账号所搜索。
    def _select_account_data_by_account(self, account):
        self.send_keys_by_clear(
            AccountManagementLocator.search_account_input_loc, account
        )

    # 账号管理界面，通过姓名搜索。
    def _select_account_data_by_name(self, name):
        self.send_keys_by_clear(AccountManagementLocator.search_name_input_loc, name)

    # 账号管理界面，通过绑定角色搜索
    def _select_account_data_by_role(self, role):
        self.click_element(AccountManagementLocator.search_role_select_loc)
        self.click_element(AccountManagementLocator.account_role_option_loc)

    # 账号管理界面，通通过管辖区域搜索
    def _select_account_data_by_area(self, area):
        self.click_element(AccountManagementLocator.search_area_select_loc)
        self.click_element((By.XPATH, f'//*[@title="{area}"]'))

    # 点击搜索按钮
    def click_search_button(self):
        self.click_element(AccountManagementLocator.search_button_loc)

    # 点击重置按钮""
    def click_reset_button(self):
        self.click_element(AccountManagementLocator.reset_button_loc)

    # 读取第一个账号的姓名
    def get_first_account_name_text(self):
        return self.text(AccountManagementLocator.first_account_name_loc)

    # 获取批量删除按钮后数量
    def get_batch_delete_button_count(self):
        return self.text(AccountManagementLocator.batch_delete_button_count_loc)

    # 点击全选按钮
    def check_all_account_checkbox(self):
        self.click_element(AccountManagementLocator.all_account_checkbox_loc)

    # 勾选第一个复选框。
    @allure.step("勾选第一个复选框")
    def check_the_first_account_checkbox(self):

        self.click_element_by_js(AccountManagementLocator.first_account_checkbox_loc)

    # 勾选第二个复选框
    def check_the_second_account_checkbox(self):
        self.click_element(AccountManagementLocator.second_account_check_box_loc)

    # 读取新增账号，账号输入框文本
    def get_add_account_account_input_text(self):
        return self.text(AccountManagementLocator.add_account_account_input_loc)

    # 新增账号填写数据步骤
    def fill_add_account_data(
        self, account, name, password, phone, email, area, role, cloud_platform, remark
    ):
        # 账号 姓名 密码 关联手机号 管辖区域 绑定角色 备注
        self.send_keys(AccountManagementLocator.add_account_account_input_loc, account)
        time.sleep(0.5)
        self.send_keys(AccountManagementLocator.add_account_name_input_loc, name)
        time.sleep(0.5)
        self.send_keys(
            AccountManagementLocator.add_account_password_input_loc, password
        )
        time.sleep(0.5)
        self.send_keys(AccountManagementLocator.add_account_phone_input_loc, phone)
        time.sleep(0.5)
        if email != "":
            self.send_keys(AccountManagementLocator.add_account_email_input_loc, email)
            time.sleep(0.5)
        if area != "":
            self.click_element(AccountManagementLocator.add_account_area_select_loc)
            time.sleep(0.5)
            if area == "大储运维（宁夏）":
                self.click_element(
                    AccountManagementLocator.add_account_north_area_option_loc
                )
                time.sleep(0.5)
            elif area == "东部":
                self.click_element(
                    AccountManagementLocator.add_account_east_area_option_loc
                )
                time.sleep(0.5)
            elif area == "西北":
                self.click_element(
                    AccountManagementLocator.add_account_northwest_area_option_loc
                )
                time.sleep(0.5)
            elif area == "海外":
                self.click_element(
                    AccountManagementLocator.add_account_overseas_area_option_loc
                )
                time.sleep(0.5)
            else:
                logger.error("账号区域填写错误")
        self.click_element(
            AccountManagementLocator.add_account_element_text_loc
        )  # 点击页面 关闭选项框
        time.sleep(0.5)
        time.sleep(1)
        self.click_element(AccountManagementLocator.add_account_role_select_loc)
        time.sleep(0.5)
        # 点击系统管理员
        if role != "":
            if role == "系统管理员":
                self.click_element(AccountManagementLocator.account_role_option_loc)
                time.sleep(0.5)
            else:  # //*[@class="ant-modal-content"] 根据输入的角色信息进行选择
                self.click_element((By.XPATH, f"//*[@title={role}]"))
                time.sleep(0.5)
        else:
            self.click_element(AccountManagementLocator.account_role_option_loc)
            logger.warning("未选择角色,选择了系统管理员")

        self.click_element(
            AccountManagementLocator.add_account_element_text_loc
        )  # 点击页面 关闭选项框
        if cloud_platform != "":
            self.click_element(
                AccountManagementLocator.account_cloud_platform_select_loc
            )
            # 根据输入的云平台信息进行选择
            self.click_element((By.XPATH, f'//*[@title="{cloud_platform}" and @id]'))

        self.send_keys(AccountManagementLocator.add_account_remark_input_loc, remark)

    # 编辑账号信息步骤
    def fill_edit_account_data(
        self, name, password, phone, email, area, role, cloud_platform, remark
    ):
        if name != "":
            self.send_keys_by_clear(
                AccountManagementLocator.add_account_name_input_loc, name
            )
        if password != "":
            self.send_keys_by_clear(
                AccountManagementLocator.add_account_password_input_loc, password
            )
        if phone != "":
            self.send_keys_by_clear(
                AccountManagementLocator.add_account_phone_input_loc, phone
            )
        if email != "":
            self.send_keys_by_clear(
                AccountManagementLocator.add_account_email_input_loc, email
            )
        if area != "":
            # 选择管辖区域
            self.click_element(AccountManagementLocator.add_account_area_select_loc)
            # 点击
            # self.click_element((By.XPATH, f'//*[@title="{area}"]))
            self.click_element((By.XPATH, f'//*[@title="{area}"]'))
            self.click_element(AccountManagementLocator.add_account_page_loc)
        if cloud_platform != "":
            self.click_element(
                AccountManagementLocator.account_cloud_platform_select_loc
            )
            # 根据输入的云平台信息进行选择
            self.click_element((By.XPATH, f'//*[@title="{cloud_platform}" and @id]'))
        if role != "":
            self.click_element(AccountManagementLocator.add_account_role_select_loc)
            # 点击系统管理员
            self.click_element(AccountManagementLocator.account_role_option_loc)
            self.click_element(AccountManagementLocator.add_account_page_loc)
        if remark != "":
            self.send_keys_by_clear(
                AccountManagementLocator.add_account_remark_input_loc, remark
            )

    # 点击确认按钮
    def click_confirm_button(self):
        try:
            logger.info("点击新增账号确认按钮")
            self.click_element(AccountManagementLocator.add_account_confirm_button_loc)
        except Exception as e:
            logger.error("点击新增账号确认按钮失败")
            raise e

    # 点击 新增账号 取消按钮
    def click_cancel_button(self):
        try:
            logger.info("点击新增账号取消按钮")
            self.click_element(AccountManagementLocator.add_account_cancel_button_loc)
        except Exception as e:
            logger.error("点击新增账号取消按钮失败")
            raise e

    # 点击新增账号关闭按钮
    def click_close_button(self):
        try:
            logger.info("点击新增账号关闭按钮")
            self.click_element_by_js(
                AccountManagementLocator.add_account_close_button_loc
            )
        except Exception as e:
            logger.error("点击新增账号关闭按钮失败")
            raise e

    # 获取页面提示信息
    def get_page_tip(self):
        try:
            logger.info("获取页面提示信息")
            return self.text(AccountManagementLocator.page_tip_loc)
        except Exception as e:
            logger.error("获取页面提示信息失败")
            raise e

    # 读取新增的第一个账号的账号文本
    def get_first_account_text(self):
        try:
            logger.info("读取新增的第一个账号的账号文本")
            return self.text(AccountManagementLocator.first_account_loc)
        except Exception as e:
            logger.error("读取新增账号的账号文本失败")
            raise e

    # 读取第二个账号的账号文本
    def get_second_account_text(self):
        try:
            logger.info("读取第二个账号的账号文本")
            return self.text(AccountManagementLocator.second_account_loc)
        except Exception as e:
            logger.error("读取新增账号的账号文本失败")
            raise e

    # 获取第一个账号数据的绑定角色信息
    def get_first_account_role_text(self):
        try:
            logger.info("读取第一个账号的绑定角色文本")
            return self.text(AccountManagementLocator.first_account_role_loc)
        except Exception as e:
            logger.error("读取新增账号的绑定角色文本失败")
            raise e

    # 获取第一个账号对应的管辖区信息
    def get_first_account_area_text(self):
        try:
            logger.info("读取第一个账号的管辖区域文本")
            return self.text(AccountManagementLocator.first_account_area_loc)
        except Exception as e:
            logger.error("读取新增账号的管辖区域文本失败")
            raise e

    # 读取新增账号按钮文本
    def get_add_account_button_text(self):
        try:
            logger.info("读取新增账号按钮文本")
            return self.text(AccountManagementLocator.add_account_button_loc)
        except Exception as e:
            logger.error("读取新增账号按钮文本失败")
            raise e

    # 点击系统配置
    def click_system_config(self):
        try:
            logger.info("点击系统配置")
            self.click_element(AccountManagementLocator.system_config_loc)
            return AccountManagementPage(self.driver)
        except Exception as e:
            logger.error("点击系统配置失败")
            raise e

    # 点击账号管理
    def click_account_management(self):
        try:
            logger.info("点击账号管理")
            self.click_element_by_js(AccountManagementLocator.account_management_loc)
            # return AccountManagementPage(self.driver)
        except Exception as e:
            logger.error("点击账号管理失败")
            raise e

    # 点击新增账号
    def click_add_account_button(self):
        try:
            logger.info("点击新增账号")
            self.click_element(AccountManagementLocator.add_account_button_loc)
            # return AccountManagementPage(self.driver)
        except Exception as e:
            logger.error("点击新增账号失败")
            raise e

    # 点击批量删除
    def click_batch_delete_button(self):
        try:
            logger.info("点击批量删除")
            self.click_element(AccountManagementLocator.batch_delete_button_loc)
            # return AccountManagementPage(self.driver)
        except Exception as e:
            logger.error("点击批量删除失败")
            raise e

    # 点击确认按钮按钮
    def click_confirm_batch_delete_button(self):
        try:
            logger.info("点击确认删除按钮")
            self.click_element(AccountManagementLocator.confirm_batch_delete_button_loc)
        except Exception as e:
            logger.error("点击确认删除按钮失败")
            raise e

    # 点击取消删除按钮
    def click_cancel_batch_delete_button(self):
        try:
            logger.info("点击取消删除按钮")
            self.click_element(AccountManagementLocator.cancel_batch_delete_button_loc)
            # return AccountManagementPage(self.driver)
        except Exception as e:
            logger.error("点击取消删除按钮失败")
            raise e

    # 点击搜索按钮
    def click_search_button(self):
        try:
            logger.info("点击搜索按钮")
            self.click_element(AccountManagementLocator.search_button_loc)
            # return AccountManagementPage(self.driver)
        except Exception as e:
            logger.error("点击搜索按钮失败")
            raise e

    # 点击重置按钮
    def click_reset_button(self):
        try:
            logger.info("点击重置按钮")
            self.click_element(AccountManagementLocator.reset_button_loc)
            return AccountManagementPage(self.driver)
        except Exception as e:
            logger.error("点击重置按钮失败")
            raise e

    # 点击编辑按钮 (第一个)
    def click_first_edit_button(self):
        try:
            logger.info("点击第一个账号的编辑按钮")
            self.click_element(AccountManagementLocator.edit_button_loc)
        except Exception as e:
            logger.error("点击编辑按钮失败")
            raise e

    # 获取，请输入账号必填项提示信息：请输入账号
    def get_account_required_tip(self):
        try:
            logger.info("获取，请输入账号必填项提示信息：请输入账号")
            return self.text(AccountManagementLocator.account_required_tip_loc)
        except Exception as e:
            logger.error("获取，请输入账号必填项提示信息：请输入账号失败")
            raise e

    # 获取，请输入姓名必填项提示信息：请输入姓名
    def get_name_required_tip(self):
        try:
            logger.info("获取，请输入姓名必填项提示信息：请输入姓名")
            return self.text(AccountManagementLocator.name_required_tip_loc)
        except Exception as e:
            logger.error("获取，请输入姓名必填项提示信息：请输入姓名失败")
            raise e

    # 获取，请输入密码必填项提示信息：请输入密码
    def get_password_required_tip(self):
        try:
            logger.info("获取，请输入密码必填项提示信息：请输入密码")
            return self.text(AccountManagementLocator.password_required_tip_loc)
        except Exception as e:
            logger.error("获取，请输入密码必填项提示信息：请输入密码失败")
            raise e

    # 获取，请输入关联手机号必填项提示信息：请输入关联手机号
    def get_phone_required_tip(self):
        try:
            logger.info("获取，请输入关联手机号必填项提示信息：请输入关联手机号")
            return self.text(AccountManagementLocator.phone_required_tip_loc)
        except Exception as e:
            logger.error("获取，请输入关联手机号必填项提示信息：请输入关联手机号失败")
            raise e

    # 获取 请选择管辖区域 必填项提示信息 : 请选择管辖区域
    def get_area_required_tip(self):
        try:
            logger.info("获取 请选择管辖区域 必填项提示信息 : 请选择管辖区域")
            return self.text(AccountManagementLocator.area_required_tip_loc)
        except Exception as e:
            logger.error("获取 请选择管辖区域 必填项提示信息 : 请选择管辖区域失败")
            raise e

    # 获取 绑定角色 必填项提示信息 : 绑定角色
    def get_role_required_tip(self):
        try:
            logger.info("获取 绑定角色 必填项提示信息 : 绑定角色")
            return self.text(AccountManagementLocator.role_required_tip_loc)
        except Exception as e:
            logger.error("获取 绑定角色 必填项提示信息 : 绑定角色失败")
            raise e
