from behave import *
from features.pages.open_account_page import OpenAccount


@step("Select currency")
def step_impl(context):
    OpenAccount(context.driver).currency()


@step("Click on process")
def step_impl(context):
    OpenAccount(context.driver).process()
