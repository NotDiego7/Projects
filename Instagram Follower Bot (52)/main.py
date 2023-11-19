from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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

driver.implicitly_wait(8.5) # Quick Sleep
driver.find_element(by= By.XPATH, value= '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click() # Denies notifications popup


driver.implicitly_wait(5.5) # Quick, quick sleep
search_button = driver.find_element(by= By.CSS_SELECTOR, value= '#mount_0_0_g8 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk > div > div > div > div > div.x1iyjqo2.xh8yej3 > div:nth-child(2) > span > div > a > div')

search_button.click()
search_button.send_keys('nelkboys')
search_button.submit()



driver.implicitly_wait(17.5)