from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions # This module is especially important


EMAIL = 'diego007lopez@gmail.com'
PASSWORD = ''

service = webdriver.ChromeService(executable_path= 'C:/Dev/chromedriver.exe')
driver = webdriver.Chrome(service= service)

driver.get('https://www.instagram.com/')
driver.implicitly_wait(4.5) # Quick sleep
email_entry_form = driver.find_element(by= By.XPATH, value= '//*[@id="loginForm"]/div/div[1]/div/label/input')
email_entry_form.send_keys(EMAIL)

password_entry_form = driver.find_element(by= By.XPATH, value= '//*[@id="loginForm"]/div/div[2]/div/label/input')
password_entry_form.send_keys(PASSWORD)

password_entry_form.submit()

# ---------------------------------------------------------------------------- #
wait = WebDriverWait(driver, 10.0)
elem = driver.find_element(by= By.XPATH, value= '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]') # Denies notifications popup

wait.until(expected_conditions.visibility_of(element= elem).click()) 

# ---------------------------------------------------------------------------- #


driver.implicitly_wait(5.5) # Quick, quick sleep
search_button = driver.find_element(by= By.XPATH, value= '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]')

search_button.click()
search_button.send_keys('nelkboys')
search_button.submit()



driver.implicitly_wait(17.5)

# Something is wrong with the driver (had issues with the Edge Driver too)
# Leaving it behind