import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 

driver=webdriver.Chrome()


driver.get("https://demo-opencart.com/")

product_thumbs = driver.find_elements(By.CLASS_NAME,"product-thumb")
print(f'elements are {len(product_thumbs)}')

#print the names of menu having class 'nav-item'.\

nav_bar=driver.find_element(By.ID,"menu")
nav_items=nav_bar.find_elements(By.CLASS_NAME,"nav-item")
for each in nav_items:
    print (each.text)

   # Click on 'Tablets' and assert that the page loaded is tablets. (url, title, left navigation, page heading)
time.sleep(5)


link_element=nav_bar.find_element(By.LINK_TEXT,"Tablets")
link_element.click()
current_link=driver.current_url
assert current_link=="https://demo-opencart.com/index.php?route=product/category&language=en-gb&path=57"
#title
content=driver.find_element(By.ID,"content")
title=content.find_element(By.TAG_NAME,"h2")
#print(title.text)
assert title.text=="Tablets"
#navigation
selected_item = driver.find_element(By.CSS_SELECTOR, '.list-group-item.active')
print(selected_item.text)
assert selected_item.text=="Tablets (1)"
#page headin
heading=driver.title
print(heading)
assert heading=="Tablets"
time.sleep(10)

