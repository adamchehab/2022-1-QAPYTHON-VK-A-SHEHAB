import pytest
from base import BaseCase
from ui.locators import basic_locators as BL


LOGIN_DATA = ["adamchehab@gmail.com", "password123"]


class TestExample(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.login(LOGIN_DATA)
        assert self.find(BL.PAGE_CONTENT)

    @pytest.mark.UI
    def test_logout(self):
        self.login(LOGIN_DATA)
        assert self.find(BL.PAGE_CONTENT)
        self.logout()
        assert self.find(BL.LOGIN_BTN)

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
        "page_btn_locator, locator",
        [
            pytest.param(BL.SEGMENTS_PAGE, BL.SEGMENTS_PAGE_CONTENT),
            pytest.param(BL.STATISTICS_PAGE, BL.STATISTICS_PAGE_CONTENT),
        ],
    )
    def test_page_switch(self, page_btn_locator, locator):
        self.login(LOGIN_DATA)
        self.click(page_btn_locator)
        assert self.find(locator)
