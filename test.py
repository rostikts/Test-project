import unittest
from selenium import webdriver
import time
from threading import Thread

desired_cap =[]
desired_cap.append({'browserName': 'chrome', 'version': '', 'platform': 'ANY'})
desired_cap.append({'browserName': 'firefox', 'marionette': True, 'acceptInsecureCerts': True})

# print('Browser list:\nGoogle Chrome: 0\nMozilla Firefox: 1')

# browser_index = int(input("Enter browser's index: "))
# assert browser_index < 0 or browser_index>len(desired_cap), 'Invalid index'

URL = 'https://www.google.com.ua/webhp?tab=rw'


class JustTest(unittest.TestCase):


    def setUp(self):

            self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities= desired_cap[browser_index])
            self.driver.get(URL)

    def test_1(self):
        try:
            element = self.driver.find_element_by_name('q')
            element.send_keys('adasd')
            time.sleep(1)
        except:
            time.sleep(5)

    def test_2(self):
        try:
            element = self.driver.find_element_by_name('q')
            element.send_keys('adasd')
            time.sleep(1)
        except:
            time.sleep(5)

    def test_3(self):
        try:
            element = self.driver.find_element_by_name('q')
            element.send_keys('adasd')
            time.sleep(1)
        except:
            time.sleep(5)

    def tearDown(self):
        
        self.driver.close()


def runChrome():
    global browser_index
    browser_index = 0
    unittest.main()
    print('Chrome testing is done')

def runFirefox():
    global browser_index
    browser_index = 1
    unittest.main()
    print('Firefox testing is done') 

if __name__ == "__main__":   

    for i in range(len(desired_cap)):
        browser_index = i
        unittest.main()
