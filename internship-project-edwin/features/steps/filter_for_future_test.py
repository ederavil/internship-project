from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page.')
def open_reely_log_in(context):
    context.app.main_page.open_reely()


@when('Log in to the page.')
def user_log_in(context):
    context.app.main_page.login_reely()


@then('Verify the right page opens.')
def verify_off_plan_open(context):
    context.app.off_plan.verify_off_plan_page()


@then('Filter by sale status of “Future Launch”.')
def filter_for_future(context):
    context.app.off_plan.filter_for_future_launch()


@then('Verify each product contains the Future Launch tag.')
def verify_future_tags(context):
    context.app.off_plan.verify_future_launch_tags()
