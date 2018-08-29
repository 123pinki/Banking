from behave import *
from features.pages.customer_page import Customer


@step("Search customer name")
def step_impl(context):
    Customer(context.driver).search_customer_name()


@step("Delete customer name")
def step_impl(context):
    Customer(context.driver).delete_customer()
