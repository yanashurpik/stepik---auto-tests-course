from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

time = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
button = browser.find_element_by_id('book').click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text

y = calc(x)

input = browser.find_element_by_id('answer').send_keys(y)
button2 = browser.find_element_by_id('solve').click()