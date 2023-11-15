import selenium

PROMISED_DOWN = 15
PROMISED_UP = 3

TWITTER_USERNAME = 'Notdiego_7'
TWITTER_PASSWORD = 'Husbandsistheonlyyellowdog1'

class InterSpeedTwitterBot:
    def __init__(self):
        service = selenium.webdriver.ChromeService(executable_path= 'C:/Dev/chromedriver.exe')
        driver = selenium.webdriver.Chrome(service= service)