from selenium.webdriver.common.by import By


class NotificationPage:

    notification_icon = (By.XPATH, "//i[@class='fa fa-bell']")

    notification_search_field = (
        By.XPATH,
        "//input[@placeholder='Search notifications']"
    )

    notification_title = (
        By.XPATH,
        "//div[@class='sh-notif-item sh-notif-c-info is-unread']//p[@class='ttl']"
    )

