from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math


try:
   link = "https://suninjuly.github.io/math.html"
   browser = webdriver.Chrome()
   browser.get(link)


   x_element = browser.find_element(By.ID, "input_value")
   x = int(x_element.text)


   result = math.log(abs(12*math.sin(x)))

   answer_input = browser.find_element(By.ID, "answer")
   answer_input.send_keys(str(result))

   robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
   robot_checkbox.click()

   robot_radio = browser.find_element(By.ID, "robotsRule")
   robot_radio.click()


   submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
   submit_button.click()


finally:
   time.sleep(30)
   browser.quit()
