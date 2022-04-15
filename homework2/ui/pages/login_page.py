from ui.pages.base_page import BasePage
from ui.locators import basic_locators as BL


class LoginPage(BasePage):

    LOC = BL.LoginPageLocators()

    def login(self, login, password):
        self.click(self.LOC.LOGIN_BTN)
        self.fill_field(self.LOC.LOGIN_NAME_FIELD, login)
        self.fill_field(self.LOC.LOGIN_PASSWORD_FIELD, password)
        self.click(self.LOC.LOGIN_SUBMIT_BTN)
