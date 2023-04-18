from behave import *
from screens.LoginScreen import LoginScreen


@given('El usuario ingresa las credenciales')
def step_impl(context):
    login = LoginScreen(context.driver)
    login.get_locator(*login.TXT_USERNAME).send_keys(context.data['STANDARD_USER'])
