import random
import string
import time

import pytest
from base import BaseCase
from selenium.webdriver.common.by import By

# from ui.locators import basic_locators as BL
# from selenium.webdriver.support import expected_conditions as EC


LOGIN_DATA = ["adamchehab@gmail.com", "password123"]


@pytest.mark.UI
@pytest.mark.skip
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


class TestTests(BaseCase):
    def test_load(self):
        self.driver.get('https://www.python.org/downloads/release/python-3104/')
        time.sleep(5)
        self.base_page.click((By.XPATH, "//a[contains(text(),'Windows embeddable package (64-bit)')]"))
        time.sleep(5)
