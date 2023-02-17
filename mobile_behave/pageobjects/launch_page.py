from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from toolium.pageelements import *
from toolium.pageobjects.mobile_page_object import MobilePageObject
from mobile_behave.pageobjects.create_account_page import BaseCreateAccountPageObject
from mobile_behave.pageobjects.login_page import BaseLoginPageObject


class BaseLaunchPageObject(MobilePageObject):
    def wait_until_loaded(self):
        """ Wait until page loaded
        :returns: initial page object
        """
        self.create_account_btn.wait_until_visible(20)
        return self


class AndroidLaunchPageObject(BaseLaunchPageObject):
    login_btn = Button(By.ID, "com.example.path:id/btn_log_in")
    create_account_btn = Button(By.ID, "com.example.path:id/action")

    def login_with_existing_account(self):
        """Go to login page
        :return: login page object
        """
        self.login_btn.click()
        return BaseLoginPageObject()

    def create_new_account(self):
        """Go to create account page
        :return: create account page object
        """
        self.create_account_btn.click()
        return BaseCreateAccountPageObject()


class IosLaunchPageObject(BaseLaunchPageObject):
    login_btn = Button(MobileBy.IOS_PREDICATE,
                       'label == "Log in" AND '
                       'name == "Log in" AND '
                       'type == "XCUIElementTypeButton"')
    create_account_btn = Button(MobileBy.IOS_PREDICATE,
                                'label == "Create account" AND '
                                'name == "Create account" AND '
                                'type == "XCUIElementTypeButton"')

    def login_with_existing_account(self):
        """Go to login page
        :return: login page object
        """
        self.login_btn.click()
        return BaseLoginPageObject()

    def create_new_account(self):
        """Go to create account page
        :return: create account page object
        """
        self.create_account_btn.click()
        return BaseCreateAccountPageObject()
