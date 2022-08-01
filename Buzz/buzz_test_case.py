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

class TestBuzz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def test_update_status(self):
        driver = self.driver
        driver.get(url)
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu_buzz_viewBuzz").click()
        time.sleep(3)

        driver.find_element(By.ID, "createPost_content").send_keys("Hello World")
        time.sleep(0.5)
        driver.find_element(By.ID, "postSubmitBtn").click()
        time.sleep(3)

        elements = driver.find_elements(By.CSS_SELECTOR, ".postContent")

        for el in elements:
            if (el.text == "Hello World"):
                self.assertEqual(el.text, "Hello World")
                return

        self.assertFalse(True)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
