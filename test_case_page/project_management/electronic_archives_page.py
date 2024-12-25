from common.base_method import BasePage
from test_case_locator.project_management.electronic_archives_locator.electronic_archives_locator import \
    ElectronicArchivesLocator
from common.loggerhandler import logger

class ElectronicArchivesPage(BasePage):

    # 获取项目管理模块class属性
    def get_project_management_module_class(self):

        # ant-menu-submenu ant-menu-submenu-inline
        # ant-menu-submenu ant-menu-submenu-inline ant-menu-submenu-open ant-menu-submenu-active

        b = self.get_attribute(ElectronicArchivesLocator.project_management_module_class_attributes_loc, "class")
        logger.debug("项目管理模块class属性为：" + b)
        return b


    # 切换至电子档案界面
    def switch_to_electronic_archives(self):
        # 'ant-menu-submenu ant-menu-submenu-inline'
        if "ant-menu-submenu ant-menu-submenu-inline" == self.get_project_management_module_class():
            self.click_element(ElectronicArchivesLocator.project_management_loc)
            print(self.get_project_management_module_class())
        self.click_element_by_js(ElectronicArchivesLocator.electronic_archives_loc)
        self.logger.info("切换至电子档案界面")

    # 获取新增项目按钮文本值
    def get_add_project_button_text(self):
        b = self.text(ElectronicArchivesLocator.add_project_button_loc)
        logger.debug("新增项目按钮文本值为：" + b)
        return b

