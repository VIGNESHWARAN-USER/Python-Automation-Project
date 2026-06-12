import logging
from actions.base_action import BaseAction
from pages.dashboard_page import DashboardPage
from pages.profile_page import ProfilePage

logger = logging.getLogger(__name__)

class ProfileAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.dp = DashboardPage(driver)
        self.pp = ProfilePage(driver)

    def click_profile_icon(self):
        logger.info("Clicking profile icon")
        self.click(self.dp.profile_icon)

    def get_role(self):
        logger.info("Getting role")
        return self.get_text(self.pp.role)

    def click_profile_button(self):
        logger.info("Clicking profile button")
        self.click(self.pp.profile_button)

    def click_leave_button(self):
        logger.info("Clicking leave button")
        self.click(self.pp.leave_button)

    def is_leave_table(self):
        logger.info("Checking table is not empty")
        return len(self.driver.find_elements(*self.pp.leave_table)) > 0