from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# creo que aca vamos a poner los metodos que usa el driver, cosas como exeption handling, login, scroll
class BaseDriver:
    #definir el constructor
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        """Escrollear toda la pagina para que cargue la info en el DOM completa"""
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 15):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))

    def wait_for_presence_of_all_elements(self, type, locator):
        wait = WebDriverWait(self.driver, 10)
        list = wait.until(EC.presence_of_element_located((type, locator)))
        return list

    def wait_until_element_is_clickable(self, type, locator):
        wait = WebDriverWait(self.driver, 10)
        list = wait.until(EC.element_to_be_clickable(type, locator))
        return list
    #juani que gato sos, no te hagas el canchero
