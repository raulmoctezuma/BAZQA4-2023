from behave import fixture, use_fixture
from os.path import dirname, abspath
from dotenv import dotenv_values
from appium import webdriver

# Capacidades del dispositivo
DESIRED_CAPABILITIES = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appName": "Swag Labs Mobile App",
    "appActivity": "com.swaglabsmobileapp.MainActivity",
    "app": "/Users/raul.moctezuma/Downloads/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
}

# URL de Appium
URL = "http://127.0.0.1:4723/wd/hub"

# Importar archivo .env
@fixture
def data(context):
    current_directory = dirname(abspath(__file__))
    context.data = dotenv_values(f'{current_directory}/.env')
    return context.data

# Conexión del dispositivo
@fixture
def driver(context):
    wait_seconds = 5
    context.driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    context.driver.implicitly_wait(wait_seconds)
    yield context.driver
    context.driver.quit()

# Incializar datos y dispositivo
def before_all(context):
    use_fixture(data, context)
    use_fixture(driver, context)
