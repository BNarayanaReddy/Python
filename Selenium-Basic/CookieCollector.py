from selenium import webdriver #type:ignore
from selenium.webdriver.common.action_chains import ActionChains #type:ignore
from selenium.webdriver.common.by import By #type:ignore

import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

lang = driver.find_element(By.ID,"langSelect-EN")
lang.click()

driver.implicitly_wait(20)

cookie = driver.find_element(By.ID,"bigCookie")
cookie_cout = driver.find_element(By.ID,"cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(4,-1,-1)]

for i in  range(5000):
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    cout = cookie_cout.text
    print(cout)
    # time.sleep(1)
    

time.sleep(100)
driver.quit()