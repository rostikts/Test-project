from pages.BasePage import BasePage
from locators.MainPageLocators import MainPageLocators
from elements import *


class MainPage(BasePage):
    
    def is_title_matches(self):
        
        return 'Booking.com | Официальный сайт | Лучшие отели и другое жилье' in self.driver.title

    def click_on_date_field(self):

        date_field_button = Button(self.driver, *MainPageLocators.DATE_FIELD)
        date_field_button.click_button()
 
    def click_on_guest_field(self):
        
        guest_field_button = Button(self.driver, *MainPageLocators.GUESTS_FIELD)
        guest_field_button.click_button()


    def choose_city(self, city):

        search_field = TextField(self.driver, *MainPageLocators.SEARCH_FIELD)
        search_field.enter_value(city)

    def click_check_prices_button(self):

        check_prices_button = Button(self.driver, *MainPageLocators.CHECK_PRICES_BUTTON)
        check_prices_button.click_button()


    def add_children_button(self, value):

        add_child_button = Button(self.driver, *MainPageLocators.ADD_CHILD_BUTTON)
        add_child_button.click_multible_times(value)

    def remove_child_buton(self, value):

        remove_child_buton = Button(self.driver, *MainPageLocators.REMOVE_CHILD_BUTTON)
        remove_child_buton.click_multible_times(value)

    def choose_today_date(self):

        choose_date = Calendar(self.driver, *MainPageLocators.CALENDAR_AVALIABLE_DAYS)
        choose_date.choose_current_day()

    def check_children_counter(self):

        children_counter = self.driver.find_element(*MainPageLocators.CHILDREN_COUNTER).text
        child_age_inputs = self.driver.find_elements(*MainPageLocators.CHILD_AGE_INPUT)

        if int(children_counter) == len(child_age_inputs):
            return True
        else:
            return False


    def check_guest_field_presence(self):

        try:
            label = self.driver.find_element(*MainPageLocators.GUESTS_FIELD_ROOM_LABEL)
            label.click()
            return True

        except:
            return False


    def check_calendar_presence(self):
    
        try:
            element = self.driver.find_element(*MainPageLocators.CALENDAR_TITLE)
            element.click()
            return True

        except:
            return False





    
    
