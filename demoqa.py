
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
login_url = "https://demoqa.com/automation-practice-form"
driver.get(login_url)
firstname_field = driver.find_element(By.ID, "firstName").send_keys("Nirjala")
lastname_field = driver.find_element(By.ID, "lastName").send_keys("Dahal")
email_field = driver.find_element(By.ID, "userEmail").send_keys("nirjaladahal123@gmail.com")
gender_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
driver.find_element(By.ID, "userNumber").send_keys("1234567890")
# Enter date of birth
driver.find_element(By.ID, "dateOfBirthInput").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select").send_keys("April")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select").send_keys("2001")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--015").click()
# Enter subjects
subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("Maths")
subjects_input.send_keys(Keys.RETURN)
# Select hobbies
hobbies_checkbox_1 = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
driver.execute_script("arguments[0].click();", hobbies_checkbox_1)
hobbies_checkbox_2 = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
driver.execute_script("arguments[0].click();", hobbies_checkbox_2)
# driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()
# driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()
# Upload picture
driver.find_element(By.ID, "uploadPicture").send_keys(r"c:\Users\gac\Desktop\as\shah-rukh-khan-indian-actor-bollywood-hd-wallpaper-preview.jpg")
# Enter current address
driver.find_element(By.ID, "currentAddress").send_keys("Banepa,Nala-Nepal")
# Select state and city
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
 
 