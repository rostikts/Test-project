import unittest
from selenium import webdriver
from settings import desired_cap, choose_browser
from pages.MainPage import MainPage
from pages.SearchHotelPage import SearchHotelPage


URL = 'https://www.booking.com/index.ru.html?label=gen173nr-1DCAEoggI46AdIM1gEaOkBiAEBmAEhuAEZyAEM2AED6AEBiAIBqAIDuALJoJj4BcACAdICJDA5OTVlZGFkLThlZGEtNDFkMC1hZGJiLWQ4ZWMzYzY2N2E2ONgCBOACAQ&sid=7ae9a48d98341ba9693a687021cac40a&click_from_logo=1'


class JustTest(unittest.TestCase):


    def setUp(self):

            self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities= desired_cap[0])
            self.driver.get(URL)
            self.driver.maximize_window()


    def test_scenario_2(self):
        
        city = 'Рига'
        main_page = MainPage(self.driver)
        assert main_page.is_title_matches(), "Title is not matches!"
        main_page.choose_city(city)
        main_page.click_check_prices_button()
        
        search_page = SearchHotelPage(self.driver)
        assert search_page.is_page_opened(city), "Page title is not matches!"
        assert search_page.check_pices_presence() is False, "Prices are shown!"
        assert search_page.check_calendar_presence(), "Calendar is not opened!"
        
        search_page.close_calendar()
        assert search_page.check_calendar_presence() is False, "Calendar is not closed!"

        search_page.click_show_prices_button()
        assert search_page.check_calendar_presence(), "Calendar is not opened!."

        search_page.choose_avaliable_date()
        search_page.click_submit_button()

        assert search_page.check_pices_presence(), "Prices are not shown!"
        assert search_page.check_prices_presence_in_description(), "Prices counter is not equal to hotel articles counter!"


    def test_scenario_1(self):

        main_page = MainPage(self.driver)
        assert main_page.is_title_matches(), "Title is not matches!"

        assert main_page.check_guest_field_presence() is False, "Guest field is opend!"
        main_page.click_on_guest_field()
        assert main_page.check_guest_field_presence(), "Guest field is not opend!"

        main_page.add_children_button(3)
        assert main_page.check_children_counter(), "Counters are not matching!"

        main_page.remove_child_buton(2)
        assert main_page.check_children_counter(), "Counters are not matching!"
    
    def tearDown(self):
        
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
