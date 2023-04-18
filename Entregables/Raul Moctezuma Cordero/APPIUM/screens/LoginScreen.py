from appium.webdriver.common.appiumby import AppiumBy as By
from screens.BaseScreen import BaseScreen


class LoginScreen(BaseScreen):
    # Componentes
    TXT_USERNAME = (By.ACCESSIBILITY_ID, 'test-Username')

    def __init__(self, driver):
        super().__init__(driver)
