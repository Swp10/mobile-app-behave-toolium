from behave import *
from mobile_behave.pageobjects.envconfig_page import BaseEnvConfigPageObject
from mobile_behave.pageobjects.launch_page import BaseLaunchPageObject
from mobile_behave.pageobjects.dashboard_page import BaseDashboardPageObject

@given("I select preprod environment")
def select_environment(context):
    context.current_page = BaseEnvConfigPageObject().wait_until_loaded()
    context.current_page = context.current_page.select_environment()

@when("I am on Login page")
def open_login_page(context):
    context.current_page = BaseLaunchPageObject().wait_until_loaded()
    context.current_page = context.current_page.login_with_existing_account()

@step("I login to account")
def login_with_email_and_password(context):
    context.current_page = context.current_page.login_with_email_and_password()

@then("I shall land on dashboard")
def verify_dashboard_page_open(context):
    context.current_page = BaseDashboardPageObject().wait_until_loaded()
    assert context.current_page.portfolio.text =='Portfolio value'

