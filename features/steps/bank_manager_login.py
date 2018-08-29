from behave import *
from features.pages.bank_manager_login_page import BankManager


@step("Click on bank manager login")
def step_impl(context):
    BankManager(context.driver).click_on_bank_manager_login()

