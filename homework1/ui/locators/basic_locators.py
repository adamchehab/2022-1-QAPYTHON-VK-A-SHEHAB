from selenium.webdriver.common.by import By


# Login
LOGIN_BTN = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
LOGIN_NAME_FIELD = (By.XPATH, "//input[@name='email']")
LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
LOGIN_SUBMIT_BTN = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")

# Logout
PROFILE_BTN = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
LOGOUT_BTN = (By.XPATH, "//a[@href='/logout']")
PAGE_CONTENT = (By.XPATH, "//div[contains(@class, 'instruction-module-container')]")

# Edit credentials
PROFILE_PAGE_BTN = (By.XPATH, "//a[@href='/profile']")
CREDENTIALS_FIELD = (By.XPATH, "//div[@data-name='fio']//input")
PHONE_NUMBER_FIELD = (By.XPATH, "//div[@data-name='phone']//input")
SAVE_BTN = (By.XPATH, "//button[contains(@class, 'button button_submit')]")

# Categories
SEGMENTS_PAGE = (By.XPATH, "//a[@href='/segments']")
SEGMENTS_PAGE_CONTENT = (By.XPATH, "//div[@class = 'segments-list']")
STATISTICS_PAGE = (By.XPATH, "//a[@href='/statistics']")
STATISTICS_PAGE_CONTENT = (By.XPATH, "//a[@href='/statistics/summary']")
