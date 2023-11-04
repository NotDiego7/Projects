from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

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
service = webdriver.ChromeService(executable_path= "C:/Dev/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url= "https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(by= By.CSS_SELECTOR, value= "#articlecount a")

driver.fullscreen_window()

driver.find_element(by= By.LINK_TEXT, value= "medical librarian").click()
sleep(7.0)
driver.find_element(by= By.LINK_TEXT, value= "MEDLINE").click()
sleep(7.0)
driver.find_element(by= By.LINK_TEXT, value= "Internet").click()
sleep(7.0)
