from selenium.webdriver.common.by import By


class BasePageLocators:
    pass
    # Categories
    # # В main page положить это и логаут или не надо? тк я буду юзать отсюда их
    # SEGMENTS_PAGE = (By.XPATH, "//a[@href='/segments']")
    # STATISTICS_PAGE = (By.XPATH, "//a[@href='/statistics']")


class LoginPageLocators(BasePageLocators):
    # Login
    LOGIN_BTN = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    LOGIN_NAME_FIELD = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_SUBMIT_BTN = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
