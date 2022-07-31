### Created by Zuhal 'Alimul Hadi
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
username="Admin"
password="admin123"
url="https://opensource-demo.orangehrmlive.com"

class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
