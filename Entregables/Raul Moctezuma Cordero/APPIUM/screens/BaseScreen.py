class BaseScreen:
    # Constructor de la clase base.
    # Define la variable de clase self.drive y le asigna el parametro driver.
    def __init__(self, driver):
        self.driver = driver

    # Localicar elementos en la aplicación
    def get_locator(self, *locator):
        return self.driver.find_element(*locator)
