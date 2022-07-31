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

class TestPIM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)
    
    def test_add_employee_without_last_name(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)

        self.login(driver)
        
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_pim_addEmployee").click()
        time.sleep(3)

        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Michael")
        time.sleep(0.5)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(3)
        error_text = driver.find_element(By.CSS_SELECTOR, ".validation-error").text
        self.assertIn(error_text, "Required")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
