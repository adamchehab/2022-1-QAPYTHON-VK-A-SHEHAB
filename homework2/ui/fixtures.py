import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.profile_page import ProfilePage


@pytest.fixture()
def driver(temp_dir):
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.maximize_window()
    # TODO
    browser.get("https://target.my.com")
    yield browser
    browser.quit()


@pytest.fixture()
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture()
def profile_page(driver):
    return ProfilePage(driver=driver)
