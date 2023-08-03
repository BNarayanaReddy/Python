from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("https://trytestingthis.netlify.app/")

driver.implicitly_wait(10)
# time.sleep(100)

button = driver.find_element(By.CLASS_NAME,"pop-up-alert")
button.click()

alert = Alert(driver)

alert.accept()




time.sleep(10)












