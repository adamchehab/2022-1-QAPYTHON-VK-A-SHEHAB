import random
import string
import pytest
from base import BaseCase

# from ui.locators import basic_locators as BL
# from selenium.webdriver.support import expected_conditions as EC


LOGIN_DATA = ["adamchehab@gmail.com", "password123"]


@pytest.mark.UI
class TestLoginNegative(BaseCase):
    def test_wrong_name(self):
        self.login_page.login(
            "".join(random.choice(string.ascii_letters) for i in range(10)) + "@mail.ru",
            LOGIN_DATA[1],
        )
        assert "https://target.my.com/dashboard" not in self.driver.current_url

    def test_wrong_password(self):
        self.login_page.login(
            LOGIN_DATA[0],
            "".join(random.choice(string.ascii_letters) for i in range(10)),
        )
        assert "https://target.my.com/dashboard" not in self.driver.current_url
