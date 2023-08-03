import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Driver SetUp

driver = webdriver.Chrome()
 
driver.get("https://www.google.com")

print(driver.title)
# search = driver.find_element(By.ID,"APjFqb")
try :
    search = WebDriverWait(driver , 10).until(
        EC.presence_of_element_located((By.ID,"APjFqb"))
    )
finally:
    # search = driver.find_element(By.ID,"APjFqb")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)
    driver.quit()

# search.send_keys("test")
# search.send_keys(Keys.RETURN)



time.sleep(5)
driver.quit()
