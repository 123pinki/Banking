from behave import *
from features.pages.customer_login_page import CustomerLogin


@when("I click on banking")
def step_impl(context):
    CustomerLogin(context.driver).click_on_banking()


@step("Click on customer login")
def step_impl(context):
    CustomerLogin(context.driver).customer_login()


@step("Select name")
def step_impl(context):
    CustomerLogin(context.driver).select_name()


@step("Click on login")
def step_impl(context):
    CustomerLogin(context.driver).login()


@step("Select account number")
def step_impl(context):
    CustomerLogin(context.driver).select_account_number()


@step("Click on logout")
def step_impl(context):
    CustomerLogin(context.driver).logout()


@step("Go to the home page")
def step_impl(context):
    CustomerLogin(context.driver).home()
