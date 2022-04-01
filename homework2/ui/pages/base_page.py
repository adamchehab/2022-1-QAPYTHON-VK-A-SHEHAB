import allure
from ui.locators import basic_locators as BL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    LOC = BL.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Filling field | FIELD: {locator} | DATA: {text}')
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

    @allure.step('Clicking on locator | LOCATOR: {locator}')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
