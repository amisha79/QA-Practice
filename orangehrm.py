import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



# Example wait
username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

#username=driver.find_element(By.NAME,'username')
username.send_keys('Admin')
password=driver.find_element(By.NAME,'password')
password.send_keys('admin123')

login=driver.find_elements(By.CLASS_NAME,'orangehrm-login-button')
login=login[0]
login.click()

time.sleep(5)


# Locate the link by its name attribute or any other locator
link = driver.find_elements(By.CLASS_NAME, 'oxd-main-menu-item')  
link=link[0]
# Open link in new tab
ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])


