from actions.base_action import BaseAction
from pages.notification_page import NotificationPage
from utilities.logger import get_logger

logger = get_logger()


class NotificationAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.np = NotificationPage()

    def click_notification(self):
        try:
            self.click(self.np.notification_icon)
            logger.info("Clicked Notification icon successfully")
        except Exception as e:
            logger.error(f"Failed to click notification icon: {str(e)}")
            raise

    def search_notification(self, notification):
        try:
            self.send_keys(self.np.notification_search_field, notification)
            logger.info(f"Searched notification: {notification}")
        except Exception as e:
            logger.error(f"Failed to search notification: {str(e)}")
            raise

    def is_ipd_notification_displayed(self):
        try:
            notification_text = self.get_text(self.np.notification_title)
            logger.info(f"Notification displayed: {notification_text}")
            return "ipd" in notification_text.lower()
        except Exception as e:
            logger.error(f"Failed to verify IPD notification: {str(e)}")
            raise