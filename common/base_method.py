import time
import os
import pyautogui
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.loggerhandler import logger
from selenium import webdriver
from test_case_locator.login_locator import LoginLocator
from common import all_file_path


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.logger = logger

    # 打开url
    def get(self, url):
        self.logger.info(f"准备打开url:{url}")
        try:
            self.driver.get(url)
            self.logger.info(f"打开url成功:{url}")
        except Exception as e:
            self.logger.error(f"打开url失败:{e}")
            raise

    # 退出浏览器
    def quit(self):
        self.logger.info("准备退出浏览器")
        try:
            self.driver.quit()
            self.logger.info("退出浏览器成功")
        except Exception as e:
            self.logger.error(f"退出浏览器失败:{e}")
            raise

    # 关闭浏览器
    def close(self):
        self.logger.info("准备关闭浏览器")
        try:
            self.driver.close()
            self.logger.info("关闭浏览器成功")
        except Exception as e:
            self.logger.error(f"关闭浏览器失败:{e}")
            raise

    # 执行js
    def execute_script(self, script,element ):
        self.logger.info(f"准备执行js:{script}")
        try:
            self.driver.execute_script(script,element)
            self.logger.info(f"执行js成功:{script}")
        except Exception as e:
            self.logger.error(f"执行js失败:{e}")
            raise

    # 显示等待
    def visibility_of_element_located(self, loc, timeout=5, frequency=1):
        """等待元素可见"""
        self.logger.info(f"等待{loc}元素可见")
        try:
            timeout = int(timeout)
            frequency = int(frequency)
            element = WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            self.logger.info(f"{loc}元素可见成功")
            return element
        except TimeoutException:
            self.logger.error(f"等待元素可见超时")
            raise
        except Exception as e:
            self.logger.error(f"等待元素可见失败:{e}")
            raise

    # 判断元素不可见
    def invisibility_of_element_located(self, loc, timeout=5, frequency=1):
        """等待元素不可见"""
        self.logger.info(f"等待{loc}元素不可见")
        try:
            timeout = int(timeout)
            frequency = int(frequency)
            WebDriverWait(self.driver, timeout, frequency).until(EC.invisibility_of_element_located(loc))
            self.logger.info(f"{loc}元素不可见成功")
            return True
        except TimeoutException:
            self.logger.error(f"等待元素不可见超时")
            return False
        except Exception as e:
            self.logger.error(f"等待元素不可见失败:{e}")
            raise


    # 截图
    def get_screenshot_png(self, filename=None):
        self.logger.info("准备截图")
        # 获取当前日期
        today = time.strftime("%Y%m%d")
        # 构建截图保存路径
        screenshot_path = os.path.join(all_file_path.screenshot_path, today)
        if filename is None:
            filename = f"{screenshot_path}/{time.strftime('%Y%m%d%H%M%S')}.png"
        else:
            filename = f"{screenshot_path}/{filename}.png"
            print(filename)

        # 判断日期文件夹是否存在，不存在则创建
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        try:
            self.driver.save_screenshot(filename)
            self.logger.info(f"截图成功:{filename}")
        except Exception as e:
            self.logger.error(f"截图失败:{e}")
            raise

    # def test_screenshot_png(self, filename=None):
    #     self.logger.info(f"准备截图:{filename}")
    #     filename = filename or "../output/screenshots/%s.png" % time.strftime("%Y%m%d%H%M%S")
    #     # 判断截图文件夹是否存在,不存在则创建一个
    #     if not os.path.exists("../output/screenshots"):
    #         os.mkdir("../output/screenshots")
    #
    #
    #     try:
    #         self.driver.save_screenshot(filename)
    #         self.logger.info(f"截图成功:{filename}")
    #     except Exception as e:
    #         self.logger.error(f"截图失败:{e}")
    #         raise

    # 窗口左上角相对于屏幕左上角的横纵坐标。
    def get_window_position(self):
        self.logger.info("准备获取窗口位置")
        try:
            position = self.driver.get_window_position()
            self.logger.info(f"获取窗口位置成功:{position}")
            return position
        except Exception as e:
            self.logger.error(f"获取窗口位置失败:{e}")
            raise

    # 设置窗口左上角相对于屏幕左上角的横纵坐标。
    def set_window_position(self, y, x):
        self.logger.info(f"准备设置窗口位置:y={y},x={x}")
        try:
            self.driver.set_window_position(y, x)
            self.logger.info(f"设置窗口位置成功:y={y},x={x}")
        except Exception as e:
            self.logger.error(f"设置窗口位置失败:{e}")
            raise

    # 获取窗口大小
    def get_window_size(self):
        self.logger.info("准备获取当前窗口的大小")
        try:
            size = self.driver.get_window_size()
            self.logger.info(f"获取当前窗口大小成功:{size}")
            return size
        except Exception as e:
            self.logger.error(f"获取当前窗口大小失败:{e}")
            raise

    # 设置窗口大小
    def set_window_size(self, width: int, height: int):
        self.logger.info(f"准备设置窗口大小:width={width},height={height}")
        try:
            self.driver.set_window_size(width, height)
            self.logger.info(f"设置当前窗口大小成功:width={width},height={height}")
        except Exception as e:
            self.logger.error(f"设置当前窗口大小失败:{e}")
            raise

    # 获取title
    def get_title(self):
        self.logger.info("准备获取当前页面的title")
        try:
            title = self.driver.title
            self.logger.info(f"获取当前页面的title成功:{title}")
            return title
        except Exception as e:
            self.logger.error(f"获取当前页面的title失败:{e}")
            raise

    # 获取当前页面的url
    def get_current_url(self):
        self.logger.info("准备获取当前页面的url")
        try:
            url = self.driver.current_url
            self.logger.info(f"获取当前页面的url成功:{url}")
            return url
        except Exception as e:
            self.logger.error(f"获取当前页面的url失败:{e}")
            raise

    # 页面最大化
    def maximize_window(self):
        self.logger.info("准备最大化当前页面")
        try:
            self.driver.maximize_window()
            self.logger.info("最大化当前页面成功")
        except Exception as e:
            self.logger.error(f"最大化当前页面失败:{e}")
            raise

    # 页面最小化
    def minimize_window(self):
        self.logger.info("准备最小化当前页面")
        try:
            self.driver.minimize_window()
            self.logger.info("最小化当前页面成功")
        except Exception as e:
            self.logger.error(f"最小化当前页面失败:{e}")
            raise

    # 页面刷新
    def refresh(self):
        self.logger.info("准备刷新当前页面")
        try:
            self.driver.refresh()
            self.logger.info("刷新当前页面成功")
        except Exception as e:
            self.logger.error(f"刷新当前页面失败:{e}")
            raise

    # 页面前进
    def forward(self):
        self.logger.info("准备前进到下一个页面")
        try:
            self.driver.forward()
            self.logger.info("前进到下一个页面成功")
        except Exception as e:
            self.logger.error(f"前进到下一个页面失败:{e}")
            raise

    # 页面后退
    def back(self):
        self.logger.info("准备后退到上一个页面")
        try:
            self.driver.back()
            self.logger.info("后退到上一个页面成功")
        except Exception as e:
            self.logger.error(f"后退到上一个页面失败:{e}")
            raise

    # 获取当前页面的源码
    def get_page_source(self):
        self.logger.info("准备获取当前页面的源码")
        try:
            source = self.driver.page_source
            self.logger.info(f"获取当前页面的源码成功:{source}")
            return source
        except Exception as e:
            self.logger.error(f"获取当前页面的源码失败:{e}")
            raise

    # 输入框输入内容
    def send_keys(self, loc, value):
        self.logger.info(f"准备输入内容:{value}")
        try:
            ele = self.visibility_of_element_located(loc)
            ele.send_keys(value)
            self.logger.info(f"输入内容成功:{value}")
        except Exception as e:
            self.logger.error(f"输入内容失败:{e}")
            raise
    # 清除并输入内容
    def send_keys_by_clear(self, loc, value):
        self.logger.info(f"准备清除并输入内容:{value}")
        try:
            ele = self.visibility_of_element_located(loc)
            ele.clear()
            time.sleep(0.1)
            ele.click()
            time.sleep(0.5)
            ele.send_keys(value)
            self.logger.info(f"清除并输入内容成功:{value}")
        except Exception as e:
            self.logger.error(f"清除并输入内容失败:{e}")
            raise

    # 清除
    def clear(self, loc):
        self.logger.info("准备清除")
        try:
            ele = self.visibility_of_element_located(loc)
            ele.clear()
            self.logger.info("清除成功")
        except Exception as e:
            self.logger.error(f"清除失败:{e}")
            raise

    # 点击
    def click_element(self, loc):
        self.logger.info("准备点击")
        try:
            ele = self.visibility_of_element_located(loc)
            ele.click()
            self.logger.info("点击成功")
        except Exception as e:
            self.logger.error(f"点击失败:{e}")
            raise

    # js点击
    def click_element_by_js(self, loc):
        self.logger.info("准备点击")
        try:
            ele = self.visibility_of_element_located(loc)
            self.execute_script("arguments[0].click();", ele)
            self.logger.info("点击成功")
        except Exception as e:
            self.logger.error(f"点击失败:{e}")
            raise


    # 双击
    def double_click(self, loc):
        self.logger.info("准备双击")
        try:
            ele = self.visibility_of_element_located(loc)
            ActionChains(self.driver).double_click(ele).perform()
            self.logger.info("双击成功")
        except Exception as e:
            self.logger.error(f"双击失败:{e}")
            raise

    # 右键点击
    def context_click(self, loc):
        self.logger.info("准备右键点击")
        try:
            ele = self.visibility_of_element_located(loc)
            ActionChains(self.driver).context_click(ele).perform()
            self.logger.info("右键点击成功")
        except Exception as e:
            self.logger.error(f"右键点击失败:{e}")
            raise

    # 获取元素文本信息
    def text(self, loc):
        self.logger.info("准备获取元素文本信息")
        try:
            ele = self.visibility_of_element_located(loc)
            text = ele.text
            self.logger.info(f"获取元素文本信息成功:{text}")
            return text
        except Exception as e:
            self.logger.error(f"获取元素文本信息失败:{e}")
            raise

    # 获取元素属性信息
    def get_attribute(self, loc, name):
        self.logger.info("准备获取元素属性信息")
        try:
            ele = self.visibility_of_element_located(loc)
            attr = ele.get_attribute(name)
            self.logger.info(f"获取元素属性信息成功:{attr}")
            return attr
        except Exception as e:
            self.logger.error(f"获取元素属性信息失败:{e}")
            raise

    # 键盘操作 全选
    def select_all(self, loc):
        self.logger.info("准备全选")
        try:
            ele = self.visibility_of_element_located(loc)
            ele.send_keys(Keys.CONTROL, 'a')
            self.logger.info("全选成功")
        except Exception as e:
            self.logger.error(f"全选失败:{e}")
            raise
    # 键盘操作 delete
    def delete(self, loc):
        self.logger.info("准备删除")
        try:
            ele = self.visibility_of_element_located(loc)
            ele.send_keys(Keys.DELETE)
            self.logger.info("删除成功")
        except Exception as e:
            self.logger.error(f"删除失败:{e}")
            raise

    # 鼠标移入
    def move_to_element(self, loc):
        self.logger.info("准备鼠标移入")
        try:
            ele = self.visibility_of_element_located(loc)
            ActionChains(self.driver).move_to_element(ele).perform()
            self.logger.info("鼠标移入成功")
        except Exception as e:
            self.logger.error(f"鼠标移入失败:{e}")
            raise
    # 浏览器放大缩小
    def zoom_page(self, zoom_factor=1):
        """
        调整整个页面的缩放比例
        :param zoom_factor: 缩放比例因子，大于1时放大页面，0到1之间时缩小页面
        """
        try:
            self.logger.info("准备调整页面缩放")
            # 获取当前缩放比例，如果未设置过，则默认为1
            current_zoom = self.driver.execute_script("return document.body.style.zoom || 1;")
            # 计算新的缩放比例
            new_zoom = float(current_zoom) * zoom_factor
            # 设置新的缩放比例，确保缩放比例不会低于0
            if new_zoom > 0:
                self.driver.execute_script(f"document.body.style.zoom = '{new_zoom}';")
                self.logger.info("页面缩放调整成功")
            else:
                self.logger.error("缩放比例因子无效，必须大于0")
                raise ValueError("缩放比例因子必须大于0")
        except Exception as e:
            self.logger.error(f"页面缩放调整失败: {e}")
            raise
    #
    def scroll_element_by_pixel(self, element, direction, pixels):
        """
        滚动元素到指定方向的位置。

        该方法通过接收方向和像素值，计算元素的新位置，并使用ActionChains执行鼠标移动操作以实现滚动。

        参数:
        - driver: Selenium WebDriver对象，用于执行浏览器操作。
        - element: WebElement对象，需要滚动的元素。
        - direction: 字符串，滚动方向，可以是'up'、'down'、'right'、'left'。
        - pixels: 整数，滚动的像素值。

        注意: 此方法不返回值，其主要作用是执行滚动操作。
        """

        # 获取元素的当前位置和大小
        location = element.location
        size = element.size

        # 初始化ActionChains对象，用于执行复杂鼠标操作
        action = ActionChains(self.driver)

        # 根据滚动方向计算新的坐标，并执行相应的滚动操作
        if direction == 'up':
            # 计算新的y坐标
            new_y = location['y'] - pixels
            action.click(element).move_by_offset(xoffset=0, yoffset=-new_y + location['y'])
        elif direction == 'down':
            # 计算新的y坐标
            new_y = location['y'] + pixels
            action.click(element).move_by_offset(xoffset=0, yoffset=new_y - location['y'])
        elif direction == 'right':
            # 计算新的x坐标
            new_x = location['x'] + pixels
            action.click(element).move_by_offset(xoffset=new_x - location['x'], yoffset=0)
        elif direction == 'left':
            # 计算新的x坐标
            new_x = location['x'] - pixels
            action.click(element).move_by_offset(xoffset=-new_x + location['x'], yoffset=0)

        # 执行滚动操作
        action.perform()
    # 鼠标滚动
    def scroll(self, amount):
        self.logger.info(f"准备滚动鼠标滚轮 ({amount})")
        try:
            pyautogui.scroll(amount)
            self.logger.info("滚动鼠标滚轮成功")
        except Exception as e:
            self.logger.error(f"滚动鼠标滚轮失败: {e}")
            raise

    # 封装AcitonChains 点击操作
    def action_chains_click(self, loc):
        self.logger.info("准备点击元素")
        try:
            ele = self.visibility_of_element_located(loc)
            ActionChains(self.driver).click(ele).perform()
            self.logger.info("点击元素成功")
        except Exception as e:
            self.logger.error(f"点击元素失败:{e}")
            raise
    # 封装AcitonChains mouseDown操作
    def action_chains_mouse_down(self, loc):
        self.logger.info("准备鼠标左键按下")
        try:
            ele = self.visibility_of_element_located(loc)
            ActionChains(self.driver).click_and_hold(ele).perform()
            self.logger.info("鼠标左键按下成功")
        except Exception as e:
            self.logger.error(f"鼠标左键按下失败:{e}")
            raise

if __name__ == '__main__':
    driver = webdriver.Chrome()
    basepage = BasePage(driver)
    basepage.get("http://192.168.1.82:3322/")

    time.sleep(2)

    # basepage.quit()
    basepage.maximize_window()
    time.sleep(2)
    # basepage.get_screenshot_png("截图")
    # print(basepage.get_window_size())
    # basepage.set_window_size(100,100)
    # time.sleep(2)
    # print(basepage.get_title())
    # basepage.get_current_url()
    # time.sleep(2)
    # print(basepage.get_window_position())
    # basepage.set_window_position(200,200)
    # time.sleep(2)
    # print(basepage.get_page_source())
    print(basepage.get_title())
    print(basepage.get_current_url())
    basepage.send_keys(LoginLocator.login_username_loc, "admin")
    time.sleep(2)
    basepage.send_keys(LoginLocator.login_password_loc, "123456")
    basepage.clear(LoginLocator.login_username_loc)
    time.sleep(2)
    basepage.click_element(LoginLocator.login_submit_loc)

    basepage.close()
