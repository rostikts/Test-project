from selenium import webdriver
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))


driver = webdriver.Chrome("/home/rostik/autotest/webdriver/chromedriver")
driver.get("https://suninjuly.github.io/execute_script.html")

x = float(driver.find_element_by_id('input_value').text)

element = driver.find_element_by_id('answer')
element.send_keys(str(calc(x)))

driver.execute_script('button = document.getElementById("robotCheckbox"); button.scrollIntoView(true);')
driver.find_element_by_css_selector('#robotCheckbox').click()
driver.execute_script("""button = document.getElementById("robotsRule"); 
                        button.scrollIntoView(true);""")
driver.find_element_by_css_selector('#robotsRule').click()

driver.execute_script("""button = document.getElementsByTagName("button")[0]; 
                        button.scrollIntoView(true);""")

time.sleep(1)
driver.find_element_by_css_selector('.btn.btn-primary').click()

time.sleep(50)
driver.quit()