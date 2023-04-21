import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class launchPage(BaseDriver):

    #definir el constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ORIGIN_CITY = "//input[@id='BE_flight_origin_city']"
    ARRIVAL_CITY = "//input[@id='BE_flight_arrival_city']"
    DATE_PICKER = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']"
    SEARCH_BUTTON = "//input[@id='BE_flight_flsearch_btn']"

    def get_origin_city(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ORIGIN_CITY)

    def get_arrival_city(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ARRIVAL_CITY)

    def get_date_picker(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DATE_PICKER)

    def get_all_dates(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def get_search_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON)

    def enterDepartFrom(self, location):
        self.get_origin_city().click()
        self.get_origin_city().send_keys(location)
        self.get_origin_city().send_keys(Keys.ENTER)

    def enter_arribalCity(self, location):
        self.get_arrival_city().click()
        self.get_arrival_city().send_keys(location)
        self.get_arrival_city().send_keys(Keys.ENTER)

    def enter_date(self, date):
        self.get_date_picker().click()
        all_dates = self.get_all_dates().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == date:
                date.click()
                break

    def click_search(self):
        self.get_search_button().click()



