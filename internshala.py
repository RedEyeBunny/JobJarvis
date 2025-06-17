import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chrome_profile = '/home/chilltoast/.config/google-chrome/Profile 1'
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile}")  # use chrome profile
options.add_argument("--disable-blink-features=AutomationControlled")  # remove bot detection flag
# options.add_argument("--headless=new") # new headless mode
options.add_argument("--start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
options.add_experimental_option("detach", True)


class internshalaScraper:
    def InitialLoginToInternshala(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://internshala.com/student/applications?referral=header")
        self.email_entry = '//*[@id="email"]'
        self.password_entry = '//*[@id="password"]'
        self.login_button = '//*[@id="login_submit"]'
        with open("login_data.json", "r") as file:  # load password file
            login_data = json.load(file)
        self.driver.find_element(By.XPATH, self.email_entry).send_keys(login_data["internshala"]["username"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.password_entry).send_keys(login_data["internshala"]["password"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(1)

    def scrapeData(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://internshala.com/student/applications?referral=header")
        try:
            table = self.driver.find_element(By.ID, 'application-table')
        except NoSuchElementException:
            old_applications_class_name = 'view_old_application_link'
            self.driver.find_element(By.CLASS_NAME,old_applications_class_name).click()
            table = self.driver.find_element(By.XPATH, '//*[@id="application-table"]')

        time.sleep(5)
        company_name = table.find_elements(By.CLASS_NAME, 'company_name')
        profile = table.find_elements(By.CLASS_NAME, 'profile')
        applied_on = self.driver.execute_script(
            'return document.querySelectorAll("td.applied_on.hide_in_mobile");')  # this method is chosen because the 'find_elements' is not returning anything.
        application_status = table.find_elements(By.CLASS_NAME, 'status-container')
        JobApp_Portal = True
        site = "Internshala"
        company_name_text = []
        profile_text = []
        applied_on_text = []
        application_status_text = []
        for item in company_name:
            company_name_text.append(item.text)
        for item in profile:
            profile_text.append(item.text)
        for item in applied_on:
            applied_on_text.append(item.text)
        for item in application_status:
            application_status_text.append(item.text)

        application_status_text = list(filter(lambda x: x != '', application_status_text))
        with open('data.csv', 'r+') as data:
            for item in zip(company_name_text, profile_text, applied_on_text, application_status_text, site):
                data.write(str(item))
                data.write('\n')
        print(application_status_text)


a = internshalaScraper()
# a.InitialLoginToInternshala()
a.scrapeData()

