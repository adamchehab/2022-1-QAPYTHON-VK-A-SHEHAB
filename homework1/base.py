import pytest
from ui.locators import basic_locators as BL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BaseCase:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver

    def fill_field(self, locator, text):
        elem = self.find(locator)
        elem.click()
        elem.clear()
        elem.send_keys(text)
        return elem

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def login(self, login_data):
        self.click(BL.LOGIN_BTN)
        self.fill_field(BL.LOGIN_NAME_FIELD, login_data[0])
        self.fill_field(BL.LOGIN_PASSWORD_FIELD, login_data[1])
        self.click(BL.LOGIN_SUBMIT_BTN)

    def logout(self):
        self.wait().until(EC.visibility_of_element_located(BL.PAGE_CONTENT))
        self.click(BL.PROFILE_BTN)
        right_menu = self.find(BL.LOGOUT_BTN)
        self.driver.execute_script("arguments[0].click()", right_menu)

    def edit_profile(self):
        self.click(BL.PROFILE_PAGE_BTN)
        self.fill_field(BL.CREDENTIALS_FIELD, "TEST_CREDENTIALS")
        self.fill_field(BL.PHONE_NUMBER_FIELD, "TEST_PHONE")
        self.click(BL.SAVE_BTN)
        self.driver.refresh()
