from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginLocator:
    """
    登录界面的元素定位表达式值
    (By.ID, "name"):登录界面用户名输入框
    (By.ID, "pwd")：登录界面密码输入框
    (By.ID, "login")：登录界面登录按钮
    """

    # 登录界面用户名,密码,登录按钮
    login_username_loc = (By.ID, "username")
    login_password_loc = (By.ID, "password")
    login_submit_loc = (By.XPATH, "//*[@type='submit']")

    sermatec_lco = (By.XPATH, "//h2[contains(text(),'采日运维管理系统')]")

    login_fail_loc = (By.XPATH, "//*[contains(text(),'用户名或密码错误')]")

    # 用户必填提示语 [id="username_help"]/div
    username_null_loc = (By.XPATH, "//*[@id='username_help']/div")
    # 密码必填提示语
    password_null_loc = (By.XPATH, "//*[@id='password_help']/div")

    # 明文掩码按钮
    mask_button_loc = (By.XPATH, "//*[@class='ant-input-suffix']/span")

    # 账号显示框//*[@class="ant-avatar ant-avatar-lg ant-avatar-circle css-1hzb5nd"]
    username_display_loc = (By.XPATH, '//*[contains(@class,"ant-dropdown-trigger")]')
    # 退出登录按钮
    logout_button_loc = (By.XPATH, "//*[text()='登出']")


if __name__ == "__main__":
    from common.base_method import BasePage

    driver = webdriver.Chrome()
    page = BasePage(driver)
    page.get("http://192.168.1.82:3322/")
    page.maximize_window()
    username_ele = page.visibility_of_element_located(LoginLocator.login_username_loc)
    username_ele.send_keys("admin")
    pwd_ele = page.visibility_of_element_located(LoginLocator.login_password_loc)
    pwd_ele.send_keys("sermatec2023")
    page.click_element(LoginLocator.login_submit_loc)
    text = "采日运维管理系统"
    assert page.text(LoginLocator.sermatec_lco) == text
