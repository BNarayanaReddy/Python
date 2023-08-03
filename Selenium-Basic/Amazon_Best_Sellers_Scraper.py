from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as re
import pandas as pd
from PIL import Image
from io import BytesIO

# Driver Setup
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/gp/bestsellers/electronics/")


dicti = {"Product Name" : [],"Image" : [],"Price" : []}


pNames = driver.find_elements(By.XPATH,"//div[contains(@class,'_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')]")

# Product Names
i = 0
for pName in pNames:
    
    dicti["Product Name"].append(pName.text)
    i+=1
    if (i==25):
        break

# Product price

prices = driver.find_elements(By.XPATH,"//span[contains(@class,'_cDEzb_p13n-sc-price_3mJ9Z')]")
j = 0
for price in prices:
    dicti["Price"].append(price.text)
    j+=1
    if(j==i):
        break

# Image

k = 0
images = driver.find_elements(By.TAG_NAME,"img")
for img in images:
    src = img.get_attribute("src")
    if src.startswith("http"):
        response = re.get(src)
        image = Image.open(BytesIO(response.content))
        if image.mode == 'P' or image.mode == 'RGBA':
            image = image.convert('RGB')
        image_path = "output"+str(k)+".jpg"
        
        image.save(image_path)
        dicti["Image"].append(image_path)
    k+=1
    if (k==i):
        break

# print(dicti)
print(len(dicti["Product Name"]))
print(len(dicti["Price"]))
print(len(dicti["Image"]))

df = pd.DataFrame(dicti)
df.to_excel("DataSheet.xlsx")
    

time.sleep(20)

    


