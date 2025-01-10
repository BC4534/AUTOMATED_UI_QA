from selenium.webdriver.common.by import By
from common.loggerhandler import logger
from test_case_locator.project_management.electronic_archives_locator.add_project_locator import (
    AddProjectLocator,
    ImplementationMaintenanceInfoLocator,
)
from test_case_page.project_management.electronic_archives_page.add_project_detail_info_page import (
    AddProjectDetailInfoPage,
)


class AddMaintainImplementInfoManagementPage(AddProjectDetailInfoPage):
    """
    维护实施管理信息
    """

    # 切换至维护实施界面
    def switch_to_maintain_implement_info_management_page(self):
        self.click_element(
            ImplementationMaintenanceInfoLocator.maintain_implement_info_management_page_loc
        )
        self.random_sleep(0.5)

    # 填写实施计划时间
    def _fill_maintain_implement_time(self, maintain_implement_info):
        self.click_element(
            ImplementationMaintenanceInfoLocator.implementation_plan_time_loc
        )
        self.random_sleep(0.5)
        self.click_element(AddProjectLocator.current_month_1_loc)
        self.random_sleep(0.5)
        self.click_element(AddProjectLocator.next_month_1_loc)
        self.random_sleep(0.5)

    # 选择实施负责人
    def _select_maintain_implement_person(self, maintain_implement_person):
        self.click_element(
            ImplementationMaintenanceInfoLocator.implementation_responsible_select_loc
        )
        self.random_sleep(0.5)
        if maintain_implement_person != "":
            try:
                logger.info(f"尝试选择实施负责人：{maintain_implement_person}")
                self.click_element(
                    (
                        By.XPATH,
                        f'//*[@class="rc-virtual-list-holder-inner"]/div[@title="{maintain_implement_person}"]',
                    )
                )
            except:
                self.logger.warning("未找到该实施负责人，默认选择系统管理员")
                self.click_element(
                    ImplementationMaintenanceInfoLocator.implementation_responsible_system_administrator_loc
                )

        else:
            self.click_element(
                ImplementationMaintenanceInfoLocator.implementation_responsible_system_administrator_loc
            )
            self.random_sleep(0.5)

    # 获取实施负责人后面 (!) 的提示文本 并返回
    def _get_maintain_implement_person_tip_text(self):
        self.move_to_element(
            ImplementationMaintenanceInfoLocator.implementation_responsible_tip_loc
        )
        self.random_sleep(0.5)
        a = self.text(
            ImplementationMaintenanceInfoLocator.implementation_responsible_tip_loc
        )
        self.logger.info("获取实施负责人后面 (!) 的提示文本：{}".format(a))
        return a

    # 填写维护实现信息
    def fill_maintain_implement_info(
        self, maintain_implement_info, maintain_implement_person
    ):
        self._fill_maintain_implement_time(maintain_implement_info)
        self._select_maintain_implement_person(maintain_implement_person)

    #  获取实施计划时间必填项
    def get_maintain_implement_time_required_text(self):
        return self.text(
            ImplementationMaintenanceInfoLocator.implementation_plan_time_required_loc
        )

    # 获取实施负责人必填项
    def get_maintain_implement_person_required_text(self):
        return self.text(
            ImplementationMaintenanceInfoLocator.implementation_responsible_required_loc
        )
