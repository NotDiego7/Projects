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
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\Down -> {measured_download_speed}\nUp -> {measured_upload_speed}")


    def tweet_at_provider(self):
        self.driver.get(url= 'https://twitter.com/i/flow/login?redirect_after_login=%2Fhome')
        username_form = self.driver.find_element(by= By.XPATH, value= '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username_form.send_keys('notdiego_7')
        username_form.submit()

        password_form = self.driver.find_element(by= By.XPATH, value= '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_form.send_keys('Husbandsistheonlyyellowdog1')
        password_form.submit()
        sleep(15.0)

        compose_tweet = self.driver.find_element(by= By.XPATH, value= '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        compose_tweet.click()
        
        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys("I'm paying for 15MBPS down and 2 up.\nDown is {measured_download_speed} right now.\nUp is {measured_upload_speed}\n\nCome on provider!")

        




# -------------------------------- Main Logic -------------------------------- #
while True:
    bot_object = InternetSpeedTwitterBot()

    bot_object.get_internet_speed()
    bot_object.tweet_at_provider() # Only execute tweets if internet speed is below thresholds
