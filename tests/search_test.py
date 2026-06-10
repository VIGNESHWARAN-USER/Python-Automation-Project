import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.excel_reader import get_data
from utilities.logger import get_logger
from actions.search_action import SearchAction

@pytest.mark.usefixtures("setup")
class TestSearch:

    @pytest.mark.parametrize("key,product_name", get_data("search_data.xlsx", "ValidSearchKeys"))
    def test_valid_product(self, key, product_name):
        self.sa = SearchAction(self.driver)
        self.sa.search(key)
        assert self.sa.check_if_product_found(product_name)

    @pytest.mark.parametrize("key,message", get_data("search_data.xlsx", "InvalidSearchKeys"))
    def test_invalid_product(self, key, message):
        self.sa = SearchAction(self.driver)
        self.sa.search(key)
        assert self.sa.check_error_message(message)