from behave import *
from features.pages.transaction_page import Transaction


@step("Click on reset")
def step_impl(context):
    Transaction(context.driver).reset()


@step("Click on back")
def step_impl(context):
    Transaction(context.driver).back()
