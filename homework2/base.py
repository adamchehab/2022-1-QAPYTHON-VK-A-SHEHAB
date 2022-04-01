import os

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.profile_page import ProfilePage


class BaseCase:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.base_page: BasePage = request.getfixturevalue("base_page")
        self.login_page: LoginPage = request.getfixturevalue("login_page")
        self.profile_page: ProfilePage = request.getfixturevalue("profile_page")

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            driver.get_screenshot_as_file(screenshot_path)
