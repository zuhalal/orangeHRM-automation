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

class TestTime(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def test_add_project_with_invalid_customer(self):
        driver = self.driver
        driver.get(url)
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        driver.find_element(By.ID, "menu_admin_ProjectInfo").click()
        driver.find_element(By.ID, "menu_admin_viewProjects").click()
        time.sleep(3)

        driver.find_element(By.NAME, "btnAdd").click()
        time.sleep(3)

        driver.find_element(By.NAME, "addProject[customerName]").send_keys("abcddef")
        driver.find_element(By.NAME, "addProject[projectName]").send_keys("Project A")
        time.sleep(1)
        driver.find_element(By.NAME, "btnSave").click()
        time.sleep(1)

        invalid_text = driver.find_element(By.CSS_SELECTOR, ".validation-error").text

        self.assertIn(invalid_text, "Invalid")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
