import time
import pytest
from pages.yatra_launch_page import launchPage
from pages.search_flights_result_page import searchFlights
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():

    def test_search_flight(self):
        lp = launchPage(self.driver)
        lp.enterDepartFrom("chennai")

        lp.enterArribalCity("new york")
        lp.enterDate("22/04/2023")

        # lp.click_search()
        # lp.page_scroll()
        #
        # fr = searchFlights(self.driver)
        # fr.filterFlightStops()
        # lista_de_textos = fr.metodo_que_devuelve_lista_de_textos()

        # ut = Utils()
        # ut.assert_list_item_text(lista_de_textos, "1 Stop")
