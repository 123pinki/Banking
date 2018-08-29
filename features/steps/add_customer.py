from behave import *
from features.pages.add_customer_page import AddCustomer


@step("Click on {add_customer} section")
def step_impl(context, add_customer):
    AddCustomer(context.driver).select_manager_work(add_customer)


@step("I enter the first name")
def step_impl(context):
    AddCustomer(context.driver).first_name()


@step("I enter the last name")
def step_impl(context):
    AddCustomer(context.driver).last_name()


@step("I enter the postal code")
def step_impl(context):
    AddCustomer(context.driver).postal_code()


@step("Click on add customer")
def step_impl(context):
    AddCustomer(context.driver).submit_detail()
