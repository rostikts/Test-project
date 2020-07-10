from selenium.webdriver.common.by import By

class MainPageLocators(object):
    
    SEARCH_FIELD = (By.ID, 'ss')
    DATE_FIELD = (By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[1]')
    GUESTS_FIELD = (By.XPATH, '//*[@id="frm"]/div[1]/div[3]')
    CHECK_PRICES_BUTTON = (By.XPATH, '//*[@id="frm"]/div[1]/div[4]/div[2]')
    ADD_CHILD_BUTTON = (By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[2]')
    REMOVE_CHILD_BUTTON = (By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[1]')
    CHILDREN_COUNTER = (By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/span[1]')
    AVALIABLE_DATE = (By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/table/tbody/tr[1]/td[6]')
    CHILD_AGE_INPUT = (By.NAME, 'age')
    GUEST_INPUT_CONTAINER = (By.ID, 'xp__guests__inputs-container')
    CALENDAR_TITLE = (By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[4]')
    GUESTS_FIELD_ROOM_LABEL = (By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[3]/div/div[1]/label')
    CALENDAR_AVALIABLE_DAYS = (By.CLASS_NAME, 'bui-calendar__date')
    TODAY_DATE = (By.CLASS_NAME, 'bui-calendar__date bui-calendar__date--today')