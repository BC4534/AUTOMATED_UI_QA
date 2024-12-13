import time

from common.base_method import BasePage
from test_case_locator.project_management.spare_parts_management_locator.spare_part_management_locator import \
    SparePartManagementLocator


class SparePartManagementPage(BasePage):

    # 切换至备件管理界面
    def switch_to_spare_part_management_page(self):
        self.click_element(SparePartManagementLocator.project_management_loc)
        self.click_element(SparePartManagementLocator.spare_part_management_loc)
        time.sleep(0.5)

    # 获取备件入库按钮文本
    def get_spare_part_inbound_button_text(self):
        return self.text(SparePartManagementLocator.spare_part_inbound_button_loc)
