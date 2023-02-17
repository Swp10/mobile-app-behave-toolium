from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from toolium.pageelements import *
from toolium.pageobjects.mobile_page_object import MobilePageObject


class BaseDashboardPageObject(MobilePageObject):
    def wait_until_loaded(self):
        self.portfolio.wait_until_visible(60)
        return self


class AndroidDashboardPageObject(BaseDashboardPageObject):
    home_menu = Text(By.ID, 'com.example.path:id/largeLabel')
    portfolio = Text(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Portfolio value")')


class IosDashboardPageObject(BaseDashboardPageObject):
    home_menu = Button(MobileBy.ACCESSIBILITY_ID, 'Home')
    portfolio = Text(MobileBy.IOS_PREDICATE, 'label == "Portfolio value"')
