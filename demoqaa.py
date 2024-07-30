import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
 

driver=webdriver.Chrome()


driver.get("https://demoqa.com/automation-practice-form")

firstname_field = driver.find_element(By.ID, "firstName").send_keys("Amisha")
lastname_field = driver.find_element(By.ID, "lastName").send_keys("Subedi")
email_field = driver.find_element(By.ID, "userEmail").send_keys("amishasubedi79@gmail.com")
gender_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()

driver.find_element(By.ID, "userNumber").send_keys("4534567890")
driver.find_element(By.ID, "dateOfBirthInput").click()

driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select").send_keys("August")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select").send_keys("2002")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--022").click()
subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("English")
subjects_input.send_keys(Keys.RETURN)
hobbies_checkbox_1 = driver.find_element(By.ID, "hobbies-checkbox-1")
hobbies_checkbox_1.click()

driver.find_element(By.ID, "uploadPicture").send_keys(r"c:\Users\gac\Desktop\as\shah-rukh-khan-indian-actor-bollywood-hd-wallpaper-preview.jpg")

driver.find_element(By.ID, "currentAddress").send_keys("devdaha,Nepal")



driver.find_element(By.ID, "state").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "state"))).click()
driver.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()
driver.find_element(By.ID, "city").click()
driver.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()
WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "state"))).click()
driver.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()
driver.find_element(By.ID, "city").click()
driver.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()
# Submit the form
driver.find_element(By.ID, "submit").click()
 
 

