from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from toolium.pageelements import InputText, Button
from toolium.pageobjects.mobile_page_object import MobilePageObject
from mobile_behave.pageobjects.dashboard_page import BaseDashboardPageObject
from resources.credentials import EMAIL, PASSWORD


class BaseLoginPageObject(MobilePageObject):

    def wait_until_loaded(self):
        """Wait until login page is loaded
        :return: login page object
        """
        self.input_email.wait_until_visible(20)
        return self


class AndroidLoginPageObject(BaseLoginPageObject):
    input_email = InputText(By.ID, "com.example.path:id/account_edit")
    continue_btn = Button(By.ID, "com.example.path:id/action")
    input_pwd = InputText(By.ID, "com.example.path:id/password_edit")
    login_btn = Button(By.ID, "com.example.path:id/action")

    def login_with_email_and_password(self):
        if not EMAIL or not PASSWORD:
            raise Exception("No credentials found!")

        self.input_email.text = EMAIL
        self.continue_btn.click()
        self.input_pwd.text = PASSWORD
        self.login_btn.click()

        return BaseDashboardPageObject()


class IosLoginPageObject(BaseLoginPageObject):
    input_email = InputText(MobileBy.IOS_PREDICATE, "value == 'Phone, email or sub account'")
    continue_btn = Button(MobileBy.IOS_PREDICATE, "label == 'Continue' AND "
                                                  "name == 'Continue' AND "
                                                  "type == 'XCUIElementTypeButton'")
    input_pwd = InputText(MobileBy.IOS_PREDICATE, "value == '••••••'")
    login_btn = Button(MobileBy.IOS_PREDICATE, "label == 'Continue' AND "
                                               "name == 'Continue' AND "
                                               "type == 'XCUIElementTypeButton'")

    def login_with_email_and_password(self):
        if not EMAIL or not PASSWORD:
            raise Exception("No credentials found!")

        self.input_email.text = EMAIL
        self.continue_btn.click()
        self.input_pwd.text = PASSWORD
        self.login_btn.click()

        return BaseDashboardPageObject()
