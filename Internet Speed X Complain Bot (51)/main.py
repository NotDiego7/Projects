from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 10
PROMISED_UP = 2

TWITTER_USERNAME = ''
TWITTER_PASSWORD = ''

class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = webdriver.ChromeService(executable_path= 'C:/Dev/chromedriver.exe')
        self.driver = webdriver.Chrome(service= self.service)
        self.down = None
        self.up = None


    def get_internet_speed(self) -> float:
        self.driver.maximize_window()
        self.driver.get(url= 'https://www.speedtest.net/')

        start_test_button = self.driver.find_element(by= By.CSS_SELECTOR, value= 'div.start-button a.js-start-test.test-mode-multi')
        start_test_button.click()
        print(1)
        sleep(70.0)
        measured_download_speed = float(self.driver.find_element(by= By.XPATH, value= '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        measured_upload_speed = float(self.driver.find_element(by= By.XPATH, value= '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\Down -> {measured_download_speed}\nUp -> {measured_upload_speed}")
        return measured_download_speed, measured_upload_speed


    def tweet_at_provider(self):
        self.driver.get(url= 'https://twitter.com/i/flow/login?redirect_after_login=%2Fhome')
        sleep(8.0) # Long Wait
        username_form = self.driver.find_element(by= By.XPATH, value= '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username_form.send_keys('notdiego_7')
        self.driver.find_element(by= By.XPATH, value= '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()

        sleep(2.5) # Short Wait
        password_form = self.driver.find_element(by= By.NAME, value= 'password')
        password_form.send_keys('Husbandsistheonlyyellowdog1')
        self.driver.find_element(by= By.XPATH, value= '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        
        sleep(15.0) # Long, Long Wait
        compose_tweet = self.driver.find_element(by= By.XPATH, value= '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        compose_tweet.click()
        
        sleep(2.5) # Short Wait
        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys(f"Down is {measured_download_speed} right now.\nUp is {measured_upload_speed}\n\nCome on provider!")
        self.driver.find_element(by= By.XPATH, value= '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]').click()
        sleep(5.00)




# -------------------------------- Main Logic -------------------------------- #
bot_object = InternetSpeedTwitterBot()

measured_download_speed, measured_upload_speed = bot_object.get_internet_speed()

if measured_download_speed < PROMISED_DOWN or measured_upload_speed < PROMISED_UP:
    bot_object.tweet_at_provider() # Only execute tweets if internet speed is below thresholds