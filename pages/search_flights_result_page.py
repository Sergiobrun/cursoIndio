import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class searchFlights(BaseDriver):

    #definir el constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FILTER_STOPS = "//span[contains(text(),'Stops')]/parent::div//p[contains(text(),'1')]"

    def get_filter_stops(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_STOPS)

    def filter_flight_stops(self):
        self.get_filter_stops().click()

    def metodo_que_devuelve_lista_de_textos(self):
        lista_de_textos = []
        return lista_de_textos
