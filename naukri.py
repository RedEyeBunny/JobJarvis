import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chrome_profile = '/home/chilltoast/.config/google-chrome/Profile 1'
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile}")  # use chrome profile
options.add_argument("--disable-blink-features=AutomationControlled")  # remove bot detection flag
# options.add_argument("--headless=new") # new headless mode
options.add_argument("--start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
options.add_experimental_option("detach", True)


class naukriScraper:
    def InitialLoginToNaukri(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.naukri.com/myapply/historypage?src=gnbOpportunities")
        self.email_entry = '//*[@id="usernameField"]'
        self.password_entry = '//*[@id="passwordField"]'
        self.login_button = '//*[@id="loginForm"]/div[2]/div[3]/div/button[1]'

        with open('WebsiteLoginDetails/login_data.json', 'r') as txt:
            login_data = json.load(txt)
        self.driver.find_element(By.XPATH, self.email_entry).send_keys(login_data['naukri']['username'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.password_entry).send_keys(login_data["naukri"]["password"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(1)

    def scrapeData(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.naukri.com/myapply/historypage?src=gnbOpportunities')
        time.sleep(3)
        column_container = self.driver.find_element(By.CLASS_NAME, 'jdTuplesContainer')
        # self.driver.execute_script("arguments[0].style.border='3px solid red'", column_container)
        time.sleep(5)
        #first_tile = column_container.find_element(By.CLASS_NAME, 'ot__jdTupleContainer jdTupleContainer select')
        other_tiles = column_container.find_elements(By.CLASS_NAME, 'ot__jdTupleContainer jdTupleContainer ')

        #print("ft", first_tile)
        for other_tile in other_tiles:
            print("ot", other_tile)
        # tiless = self.driver.find_element(By.CLASS_NAME,'applyHistoryListContainer width410 content')
        # for tile in tiless:
        print(column_container)


a = naukriScraper()
# a.InitialLoginToNaukri()
a.scrapeData()
