from selenium.webdriver.support.ui import WebDriverWait

class BaseElement(object):

    def __init__(self, driver, by, locator):
        
        self.driver = driver
        self.by = by
        self.locator = locator

    def get_element(self):

        WebDriverWait(self.driver, 3).until(
            lambda driver: self.driver.find_element(self.by, self.locator)
        )
        return self.driver.find_element(self.by, self.locator)

    def get_elements(self):

        WebDriverWait(self.driver, 3).until(
            lambda driver: self.driver.find_elements(self.by, self.locator)
        )
        return self.driver.find_elements(self.by, self.locator)

    def get_xpath_of_element(self, element, class_locator):

        xpath = ''
        while True:
            for elem in element:
                if class_locator in elem.get_attribute('class'):
                    xpath = self.driver.execute_script("""gPt=function(c){
                                        if(c.id!==''){
                                            return'//*[@id="'+c.id+'"]'
                                        } 
                                        if(c===document.body){
                                            return c.tagName
                                        }
                                        var a=0;
                                        var e=c.parentNode.childNodes;
                                        for(var b=0;b<e.length;b++){
                                            var d=e[b];
                                            if(d===c){
                                                return gPt(c.parentNode)+'/'+c.tagName+'['+(a+1)+']'
                                            }
                                            if(d.nodeType===1&&d.tagName===c.tagName){
                                                a++
                                            }
                                        }
                                    };
                                    return gPt(arguments[0]).toLowerCase();""", elem)
            break
        return xpath

class Button(BaseElement):


    def click_button(self):
        
        self.get_element().click()

    def click_multible_times(self, num):

        for i in range(0, num):
            self.get_element().click()



class TextField(BaseElement):

    def enter_value(self, value):

        self.get_element().clear()
        self.get_element().send_keys(value)

    def clear_text_field(self):

        self.get_element().clear()



class Calendar(BaseElement):

    def get_current_month_dates(self):

        return self.get_elements()[:33]
    
    def choose_current_day(self):

        month = self.get_current_month_dates()
        current_day_xpath = self.get_xpath_of_element(month, 'date--today')
        self.driver.find_element_by_xpath(current_day_xpath).click()
        
    def click_on_calendar_element(self, by, locator):

        title_label = self.driver.find_element(by, locator)
        title_label.click()


        

        
