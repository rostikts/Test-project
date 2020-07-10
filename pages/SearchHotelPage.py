from locators.SearchHotelPageLocators import SearchHotelPageLocators
from pages.BasePage import BasePage
from elements import *


class SearchHotelPage(BasePage):

    def is_page_opened(self, city):

        return 'Booking.com: Отели по направлению {0}.'.format(city) in self.driver.title

    def check_calendar_1(self):
        try:
            WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element(*SearchHotelPageLocators.CALENDAR_BAR_1_LABEL))
            self.driver.find_element(*SearchHotelPageLocators.CALENDAR_BAR_1_LABEL).click()
            return True
        except:
            return False
    
    def check_calendar_2(self):
        try:
            WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element(*SearchHotelPageLocators.CALENDAR_BAR_2_LABEL))
            self.driver.find_element(*SearchHotelPageLocators.CALENDAR_BAR_2_LABEL).click()
            return True
        except:
            return False


    def check_calendar_presence(self):

        if self.check_calendar_1() is True or self.check_calendar_2() is True:
            return True
        else:
            return False

    def close_calendar(self):

        element = Button(self.driver, *SearchHotelPageLocators.CALENDAR_FIELD)
        element.click_button()

    def choose_avaliable_date(self):

        try:

            element = Button(self.driver, *SearchHotelPageLocators.CHECK_IN_DATE_1)
            element.click_button()
        except:

            element = Button(self.driver, *SearchHotelPageLocators.CHECK_IN_DATE_2)
            element.click_button()



    def click_submit_button(self):
        
        element = Button(self.driver, *SearchHotelPageLocators.SUBMIT_BUTTON)
        element.click_button()


    def check_pices_presence(self):

        try:
            prices = self.driver.find_elements(*SearchHotelPageLocators.PRICE_ELEMENT)
            if len(prices) > 0:
                return True
            else:
                return False

        except:
            return False


    def check_prices_presence_in_description(self):
        try:
            articles = self.driver.find_elements(*SearchHotelPageLocators.HOTEL_ARTICLE)
            prices = self.driver.find_elements(*SearchHotelPageLocators.PRICE_ELEMENT)
            prices = prices[::2]
            if len(prices) == len(articles):
                return True
            else:
                return False

        except:
            return False


    def click_show_prices_button(self):

        element = Button(self.driver,*SearchHotelPageLocators.SHOW_PRICES_BUTTONS)
        element.click_button()

    def choose_today_date(self):

        calendar = Calendar(self.driver, *SearchHotelPageLocators.CALENDAR_AVALIABLE_DAYS)
        calendar.choose_current_day()