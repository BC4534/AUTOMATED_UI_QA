import time

from common.base_method import BasePage
import allure
from test_case_locator.login_locator import LoginLocator


class LoginPage(BasePage):

    def login(self,url, username, password):
        with allure.step("登录运维管理系统"):
            self.get(url)
            self.maximize_window()
            self.send_keys(LoginLocator.login_username_loc, username)
            self.send_keys(LoginLocator.login_password_loc, password)
            self.click_element(LoginLocator.login_submit_loc)

    def mask_login(self,url, username, password):
        with allure.step("登录运维管理系统"):
            self.get(url)
            self.maximize_window()
            self.send_keys(LoginLocator.login_username_loc, username)
            self.send_keys(LoginLocator.login_password_loc, password)
            # print("read_password_value"+self.read_password_value())
            # print("read_password_text"+self.read_password_text())
            time.sleep(1)
            self.click_element(LoginLocator.mask_button_loc)
            time.sleep(1)

    def logout(self):
        with allure.step("退出登录"):
            self.click_element(LoginLocator.username_display_loc)
            self.click_element(LoginLocator.logout_button_loc)

    # 登录成功断言
    def login_assert(self):
        with allure.step("登录成功断言"):
            return self.text(LoginLocator.sermatec_lco)

    # 登录失败断言
    def login_fail_assert(self):
        with allure.step("登录失败断言"):
            return self.text(LoginLocator.login_fail_loc)
    # 登录页面 采日运维管理系统 标识
    def sermatec_assert(self):
        with allure.step("登录页面 采日运维管理系统 标识"):
            return self.text(LoginLocator.sermatec_lco)

    # 用户名必填提示
    def username_null_assert(self):
        with allure.step("用户名必填提示"):
            return self.text(LoginLocator.username_null_loc)
    # 密码必填提示
    def password_null_assert(self):
        with allure.step("密码必填提示"):
            return self.text(LoginLocator.password_null_loc)

    # 点击掩码按钮
    def click_mask_button(self):
        with allure.step("点击掩码按钮"):
            self.click_element(LoginLocator.mask_button_loc)
    # 读取密码输入框文本内容
    def read_password_text(self):
        with allure.step("读取密码输入框文本内容"):
            return self.text(LoginLocator.login_password_loc)

    # 读取密码输入框value属性值
    def read_password_value(self):
        with allure.step("读取密码输入框value属性值"):
            return self.get_attribute(LoginLocator.login_password_loc, "value")
    # 点击账号头像按钮
    def click_username_display(self):
        with allure.step("点击账号头像按钮"):
            self.click_element(LoginLocator.username_display_loc)
    # 点击退出按钮
    def click_logout_button(self):
        with allure.step("点击退出按钮"):
            self.click_element(LoginLocator.logout_button_loc)
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.login("http://192.168.1.82:3322/login", "admin", "*sermatecroot24")