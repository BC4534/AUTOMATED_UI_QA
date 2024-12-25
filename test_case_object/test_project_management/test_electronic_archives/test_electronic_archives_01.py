from test_case_page.project_management.electronic_archives_page import ElectronicArchivesPage
from common.loggerhandler import logger


class TestElectronicArchives01:

    def test_electronic_archives_01(self, login_driver):
        electronic_archives_page = ElectronicArchivesPage(login_driver)
        try:
            logger.info(f"{self.__class__.__name__} 开始执行用例")
            electronic_archives_page.switch_to_electronic_archives()
            assert electronic_archives_page.get_add_project_button_text() == "新增项目"
        except Exception as e:
            logger.error(f"{self.__class__.__name__} 测试用例执行失败，错误信息为：{e}")
            electronic_archives_page.get_screenshot_png(f"{self.__class__.__name__}")

