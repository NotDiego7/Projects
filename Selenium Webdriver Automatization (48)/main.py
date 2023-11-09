from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
from time import sleep
import time

# ------------------------------ Trying Selenium ----------------------------- #
# service = webdriver.ChromeService(executable_path="C:\Dev\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get(url="https://google.com/")

# # element = driver.find_element(by=By.CLASS_NAME, value="pHiOh")

# # print(element.get_attribute(name= "href"))
# # print(element.text)

# element = driver.find_element(by= By.TAG_NAME, value="head")


# print(element.find_element(by= By.TAG_NAME, value= "title").text)


# driver.quit()

# ------------------------------------ 2nd ----------------------------------- #
# service = webdriver.ChromeService(executable_path= "C:/Dev/chromedriver.exe")
# control_driver = webdriver.Chrome(service=service)

# control_driver.get(url= "https://www.python.org/")

# doc_element = control_driver.find_element(by= By.CSS_SELECTOR, value= ".small-widget.documentation-widget p a")
# print(doc_element.text)

# report_bug_elem = control_driver.find_element(By.CSS_SELECTOR, ".footer-links.navigation.menu.do-not-print li.tier-1.element-3 a")
# print(f"{report_bug_elem.text}\n{report_bug_elem.get_attribute('href')}")

# report_bug_elem = control_driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(f"{report_bug_elem.text}\n{report_bug_elem.get_attribute('href')}")

# ------------------------------------ 3rd ----------------------------------- #
# service = webdriver.ChromeService(executable_path= "C:/Dev/chromedriver.exe")
# control_driver = webdriver.Chrome(service=service)

# control_driver.get(url= "https://www.python.org/")

# event_list = control_driver.find_elements(by= By.CSS_SELECTOR, value= "div.medium-widget.event-widget.last div.shrubbery ul.menu li")

# upcoming_events = {}
# count = 0
# for i in event_list:
#     event_date = i.find_element(by= By.CSS_SELECTOR, value= "time").text
#     event_name = i.find_element(by= By.TAG_NAME, value= "a").text

#     upcoming_events.update({count: {event_date: event_name}})

#     count += 1

# print(upcoming_events)

# ------------------------ 4th Selenium (Interaction) ------------------------ #
# service = webdriver.ChromeService(executable_path= "C:/Dev/chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get(url= "https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(by= By.CSS_SELECTOR, value= "#articlecount a")

# driver.fullscreen_window()

# driver.find_element(by= By.LINK_TEXT, value= "medical librarian").click()
# sleep(7.0)
# driver.find_element(by= By.LINK_TEXT, value= "MEDLINE").click()
# sleep(7.0)
# driver.find_element(by= By.LINK_TEXT, value= "Internet").click()
# sleep(7.0)
# webdriver.Chrome(service= chrome_service, options= chrome_options)

# ------------------------------- 5th Wikipedia ------------------------------ #
# service = webdriver.ChromeService(executable_path= "C:/Dev/chromedriver.exe")
# options = webdriver.ChromeOptions()
# options = options.add_argument(r"--user-data-dir=C:\Users\Lopez\AppData\Local\Google\Chrome\User Data")

# control_driver = webdriver.Chrome(service= service, options= options)
# control_driver.get(url= "https://en.wikipedia.org/wiki/Main_Page")

# search_form = control_driver.find_element(by= By.CSS_SELECTOR, value= 'input.cdx-text-input__input')
# search_form.send_keys("Python")
# search_form.submit()
# sleep(7.0)

# ------------------- 6th Submit Form with Personal Details ------------------ #
# FULL_NAME = "Mark Zuck"
# EMAIL = "MarkZuck@FB.com"

# service = webdriver.ChromeService(executable_path= "C:/Dev/chromedriver.exe")
# options = webdriver.ChromeOptions()
# options = options.add_argument(r"--user-data-dir=C:\Users\Lopez\AppData\Local\Google\Chrome\User Data")

# control_driver = webdriver.Chrome(service= service, options= options)

# control_driver.get(url= "http://secure-retreat-92358.herokuapp.com/")
# f_name = control_driver.find_element(By.NAME, "fName")
# f_name.send_keys(FULL_NAME.split()[0])

# l_name = control_driver.find_element(By.NAME, "lName")
# l_name.send_keys(FULL_NAME.split()[1])

# email = control_driver.find_element(By.NAME, "email")
# email.send_keys(EMAIL)
# email.submit()
# sleep(7.00

# ----------------------- Final | Cookie Clicker Final ----------------------- #
service = webdriver.ChromeService(executable_path= "C:/Dev/chromedriver.exe")
driver_control = webdriver.Chrome(service= service)

driver_control.get('https://orteil.dashnet.org/cookieclicker/')
sleep(8.00)
select_language = driver_control.find_element(by= By.ID, value= 'langSelect-EN')
select_language.click()

sleep(8.70)
cookie_button = driver_control.find_element(by= By.CSS_SELECTOR, value= 'div#cookieAnchor button')

prices_list = []
while True:
    prices_list = driver_control.find_elements(by= By.CSS_SELECTOR, value= 'div.product.unlocked.enabled span.price')
    current = time.localtime().tm_sec
    
    if len(prices_list) == 0:
        five_secs_after_current = current + 5
        while current <= five_secs_after_current:
            cookie_button.click()
            five_secs_after_current -= 0.1
            

    
    if current % 5 == 0: # Gets prices into a list every 5 seconds

        prices_list = driver_control.find_elements(by= By.CSS_SELECTOR, value= 'div.product.unlocked.enabled span.price')
        most_expensive_item_id_num = prices_list[-1].get_attribute("id")[-1]
        driver_control.find_element(by= By.ID, value= f"product{most_expensive_item_id_num}").click() # Buys the most expensive element available
        

    cookie_button.click()


# ---------------------------- Get Content from MM --------------------------- #
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(r"--user-data-dir=C:\Users\Lopez\AppData\Local\Google\Chrome\User Data")

# service = webdriver.ChromeService(executable_path="C:/Dev/chromedriver.exe")

# driver_control = webdriver.Chrome(service= service, options= chrome_options)

# driver_control.get(url= "https://app.moviemethod.com/moderator/decks/details/622025857afd91390e00ac3e/cards")
# driver_control.
# sleep(10.75)
# elem_list = driver_control.find_elements(by= By.CSS_SELECTOR, value= 'div.card button.video-play-btn')
# print(len(elem_list))

# for elem in elem_list:
#     elem.click()
#     elem_clip = driver_control.find_element(By.CSS_SELECTOR, '#app > div > div > div.dashboard-content > div.container > div > div > div > div > div > div > div.vue-recycle-scroller__item-wrapper > div:nth-child(1) > div > div:nth-child(1) > div.card-video > div > video').get_attribute("src")
#     print(elem_clip)
