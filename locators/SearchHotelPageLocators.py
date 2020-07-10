from selenium.webdriver.common.by import By

class SearchHotelPageLocators(object):

    CALENDAR_BAR_1 = (By.XPATH, '//*[@id="frm"]/div[3]/div/div[1]/div[1]/div/div/div[2]')
    CALENDAR_BAR_2 = (By.XPATH, '//*[@id="frm"]/div[3]/div/div[2]/div/div')
    CALENDAR_BAR_1_LABEL = (By.XPATH, '//*[@id="frm"]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]')
    CALENDAR_BAR_2_LABEL = (By.XPATH, '//*[@id="frm"]/div[3]/div/div[2]/div/div/div[4]')
    CALENDAR_FIELD = (By.XPATH, '//*[@id="frm"]/div[3]/div/div[1]/div[1]/div/div/div[1]')
    SHOW_PRICES_BUTTONS = (By.CLASS_NAME, 'bui-button__text')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="frm"]/div[5]/div[2]/button')
    HOTEL_LIST = (By.ID,'hotellist_inner')
    HOTEL_ARTICLE = (By.CLASS_NAME, 'room_details ')
    PRICE_ELEMENT = (By.CLASS_NAME, 'bui-u-sr-only')
    CHECK_IN_DATE_1 = (By.XPATH, '//*[@id="frm"]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr[1]/td[7]/span')
    CHECK_IN_DATE_2 = (By.XPATH, '//*[@id="frm"]/div[3]/div/div[2]/div/div/div[3]/div[2]/table/tbody/tr[1]/td[7]')
    
