import random
import string
import allure
import pytest
from ui.locators import basic_locators as BL
from base import BaseCase

LOGIN_DATA = ["adamchehab@gmail.com", "password123"]


@pytest.mark.UI
class TestLoginNegative(BaseCase):
    def test_wrong_name(self):
        with allure.step('Trying to log in with wrong username ...'):
            self.login_page.login(
                "".join(random.choice(string.ascii_letters) for i in range(10)) + "@mail.ru",
                LOGIN_DATA[1],
            )
        with allure.step('Asserting ...'):
            assert self.base_page.find(BL.LoginPageLocators.LOGIN_NAME_FIELD)

    def test_wrong_password(self):
        with allure.step('Trying to log in with wrong password ...'):
            self.login_page.login(
                LOGIN_DATA[0],
                "".join(random.choice(string.ascii_letters) for i in range(10)),
            )
        with allure.step('Asserting ...'):
            assert self.base_page.find(BL.LoginPageLocators.LOGIN_NAME_FIELD)
