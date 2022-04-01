from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators(BasePageLocators):
    # Login
    LOGIN_BTN = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    LOGIN_NAME_FIELD = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_SUBMIT_BTN = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
