from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TodoSeleniumTest(StaticLiveServerTestCase):

    def setUp(self):
        chrome_options = Options()
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_full_user_flow(self):
        driver = self.driver

        driver.get(f"{self.live_server_url}/Register/")

        driver.find_element(By.ID, "username").send_keys("darpan")
        driver.find_element(By.ID, "email").send_keys("darpan@example.com")
        driver.find_element(By.ID, "password").send_keys("pass123")
        driver.find_element(By.ID, "password2").send_keys("pass123")
        driver.find_element(By.TAG_NAME, "form").submit()

        WebDriverWait(driver, 10).until(
            EC.url_changes(f"{self.live_server_url}/Register/")
        )

        driver.get(f"{self.live_server_url}/AddTask/")

        driver.find_element(By.ID, "Title").send_keys("Task")
        driver.find_element(By.ID, "Description").send_keys("Created by Selenium")
        driver.find_element(By.ID, "CompletionDate").send_keys("2025-08-12")
        driver.find_element(By.ID, "completionStatus").click()
        driver.find_element(By.NAME, "Submit").click()

        WebDriverWait(driver, 10).until(
            EC.url_changes(f"{self.live_server_url}/AddTask/")
        )

        driver.get(f"{self.live_server_url}/")
        body_text = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Task", body_text)

        delete_links = driver.find_elements(By.LINK_TEXT, "Delete")
        if delete_links:
            delete_links[0].click()
       
            WebDriverWait(driver, 10).until(
                EC.staleness_of(delete_links[0])
            )

        driver.get(f"{self.live_server_url}/Logout/")

    
        WebDriverWait(driver, 10).until(
            EC.url_changes(f"{self.live_server_url}/Logout/")
        )

