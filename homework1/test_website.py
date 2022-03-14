import pytest
from base import BaseCase
from ui.locators import basic_locators as BL
from selenium.webdriver.support import expected_conditions as EC


LOGIN_DATA = ["adamchehab@gmail.com", "password123"]


class TestExample(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.login(LOGIN_DATA)
        assert self.driver.current_url == "https://target.my.com/dashboard"

    @pytest.mark.UI
    def test_logout(self):
        self.login(LOGIN_DATA)
        assert self.driver.current_url == "https://target.my.com/dashboard"
        self.logout()
        assert self.driver.current_url == "https://target.my.com/"

    @pytest.mark.UI
    def test_edit_profile_info(self):
        self.login(LOGIN_DATA)
        self.edit_profile()

        assert self.find(BL.CREDENTIALS_FIELD).get_attribute("value") == "TEST_CREDENTIALS"
        assert self.find(BL.PHONE_NUMBER_FIELD).get_attribute("value") == "TEST_PHONE"

        self.fill_field(BL.CREDENTIALS_FIELD, "blank")
        self.fill_field(BL.PHONE_NUMBER_FIELD, "blank")
        self.click(BL.SAVE_BTN)

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "page_btn_locator, page_url",
        [
            pytest.param(BL.SEGMENTS_PAGE, "https://target.my.com/segments/segments_list"),
            pytest.param(BL.STATISTICS_PAGE, "https://target.my.com/statistics/summary"),
        ],
    )
    def test_page_switch(self, page_btn_locator, page_url):
        self.login(LOGIN_DATA)
        self.click(page_btn_locator)
        self.wait().until(EC.url_matches(page_url))
        assert self.driver.current_url == page_url
