import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED'
chrome_profile = '/home/chilltoast/.config/google-chrome/Profile 1'
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile}")  # use chrome profile
options.add_argument("--disable-blink-features=AutomationControlled")  # remove bot detection flag
# options.add_argument("--headless=new") # new headless mode
options.add_argument("--start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
options.add_experimental_option("detach", True)
ph_no = '+91 74287-23247'


class linkedinScraper:
    def initialLoginToLinkedin(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED")
        self.email_entry = '//*[@id="username"]'
        self.password_entry = '//*[@id="password"]'
        self.login_button = '//*[@id="organic-div"]/form/div[4]/button'
        with open('WebsiteLoginDetails/login_data.json', 'r') as txt:
            login_data = json.load(txt)
        self.driver.find_element(By.XPATH, self.email_entry).send_keys(login_data['linkedin']['username'])
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.password_entry).send_keys(login_data["linkedin"]["password"])
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)

    def scrapeData(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED")
        time.sleep(2)
        jobs_container = self.driver.find_element(By.CSS_SELECTOR, 'body > div.application-outlet > '
                                                                   'div.authentication-outlet > div > main > section >'
                                                                   ' div > div:nth-child(4) > div > ul')
        self.driver.execute_script("arguments[0].style.border='3px solid red'", jobs_container)
        info = jobs_container.find_elements(By.CLASS_NAME, 'mb1')
        appliedOnHint = jobs_container.find_elements(By.CLASS_NAME, 'reusable-search-simple-insight__text-container')
        numbers = 'artdeco-pagination__indicator artdeco - pagination__indicator--number active selected ember-view'

        for i,j in zip(info,appliedOnHint):
            first_detail = i.text.split('\n')
            second_detail = j.text
            job_detail_combined = first_detail+[second_detail]
            print('jdc = ', job_detail_combined)


scraper = linkedinScraper()
scraper.scrapeData()
