
from behave import given,when,then


@given('open app')
def step_impl(context):
    print("open app")


@when('user is pointing url abcde')
def step_impl(context):
    print("user is pointing url abcde")


@then('user opens the app')
def step_impl(context):
    print("user opens the app")


@given('open app again')
def step_impl(context):
    print('open app again')


@when('user logs in')
def step_impl(context):
    print('user logs in')


@then('user is logged in')
def step_impl(context):
    print('user is logged in')
    assert False
