from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 10
PROMISED_UP = 2

TWITTER_USERNAME = 'Notdiego_7'
TWITTER_PASSWORD = 'Husbandsistheonlyyellowdog1'

class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = webdriver.ChromeService(executable_path= 'C:/Dev/chromedriver.exe')
        self.driver = webdriver.Chrome(service= self.service)
        self.down = None
        self.up = None


    def get_internet_speed(self):
        self.driver.get(url= 'https://www.speedtest.net/')

        start_test_button = self.driver.find_element(by= By.CSS_SELECTOR, value= 'div.start-button a.js-start-test.test-mode-multi')
        start_test_button.click()
        sleep(70.0)
        measured_download_speed = self.driver.find_element(by= By.XPATH, value= '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        measured_upload_speed = self.driver.find_element(by= By.XPATH, value= '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDown -> {measured_download_speed}\nUp -> {measured_upload_speed}")


    def tweet_at_provider(self):
        pass


# -------------------------------- Main Logic -------------------------------- #
while True:
    bot_object = InternetSpeedTwitterBot()

    bot_object.get_internet_speed()
    bot_object.tweet_at_provider() # Only execute tweets if internet speed is below thresholds 
