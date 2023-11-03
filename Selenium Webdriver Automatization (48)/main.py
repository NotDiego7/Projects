from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service(executable_path="C:\Dev\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get(url="https://google.com/")