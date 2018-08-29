from behave import *
from features.pages.deposit_page import Deposit


@step("Select the {option}")
def step_impl(context, option):
    Deposit(context.driver).select_option(option)


@step("Enter the amount {amount}")
def step_impl(context, amount):
    Deposit(context.driver).enter_deposit_amount(amount)


@step("Click on deposit/withdraw")
def step_impl(context):
    Deposit(context.driver).click_on_deposit()
