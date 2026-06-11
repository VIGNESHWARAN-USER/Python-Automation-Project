from actions.base_action import BaseAction
from pages.pathalogy_page import PathalogyPage
from pages.sidebar_page import SideBarPage
from utilities.logger import get_logger

logger = get_logger()

class PathalogyAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.pp = PathalogyPage()
        self.sp = SideBarPage()
