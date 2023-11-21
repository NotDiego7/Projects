import requests
# import undetected_chromedriver

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

GOOGLE_FORM_LINK = 'https://forms.gle/XJBJMEh6whWZQDNF8'

# ---------------------------- Get HTML from site ---------------------------- #
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": "PHPSESSID=242a10656e1779cac246145de54684aa",
}

endpoint_response_markup = requests.get(url= 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D', headers= headers).content

# ----------------- Use BeautifulSoup to get 3 lists of data ----------------- #
soup = BeautifulSoup(markup= endpoint_response_markup, features= 'html.parser')

zillow_properties_urls_list = soup.select(selector= 'div.StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0.bKpguY.property-card-data a.property-card-link')

zillow_properties_prices_list = soup.select(selector= 'span.PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1.iMKTKr')

zillow_properties_address_list = soup.select(selector= 'a.StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0.jnnxAW.property-card-link address')
# print(zillow_properties_urls_list[0]['href'])
# ------------------------- Zip all 3 lists into one ------------------------- #
zipped_data = list(zip(zillow_properties_urls_list, zillow_properties_prices_list, zillow_properties_address_list))

# --------------------------- Initialize Webdriver --------------------------- #
service = ChromeService(executable_path= 'C:/Dev/chromedriver.exe')
driver_control = webdriver.Chrome(service= service)
driver_control.maximize_window()

# ------------ For i in zipped_data, fill in a form with that data ----------- #
for i in zipped_data:
    driver_control.get(GOOGLE_FORM_LINK)
    sleep(4.5)
    # ---------------------- Find input Xpaths to work with ---------------------- #
    property_url_input = driver_control.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price_input = driver_control.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address_input = driver_control.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # -------------------------------- Fill in url ------------------------------- #
    if i[0]['href'][0] == '/': # At times, only the suffix of the url, hence conditioning
        property_link = f"https://www.zillow.com/{i[0]['href']}"
        property_url_input.send_keys(property_link)
    else:
        property_link = i[0]['href']
        property_url_input.send_keys(property_link)
    # ------------------------------ Fill in prices ------------------------------ #
    property_price_input.send_keys(i[1].text[0:6])
    # ------------------------------ Fill in address ----------------------------- #
    property_address_input.send_keys(i[2].text)
    # ---------------------------------- Submit ---------------------------------- #
    driver_control.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()


driver_control.quit()
