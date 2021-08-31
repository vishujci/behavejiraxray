
from behave import given,when,then

@given('when i open the app')
def step_impl(context):
    print('when i open the app')

@then('user will start doing something')
def step_impl(context):
    print('user will start doing something')

@given('user comes in')
def step_imp(context):
    print('user comes in')

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


@given('user do something')
def step_impl(context):
    print('user do something')


@when('user see something')
def step_impl(context):
    print('user see something')


@then('user completes this')
def step_impl(context):
    print('user completes this')


@then('user do something')
def step_impl(context):
    print('user do something')


@when('user sees something')
def step_impl(context):
    print('user sees something')