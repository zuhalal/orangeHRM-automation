### Created by Zuhal 'Alimul Hadi
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

#variable
username="Admin"
password="admin123"
url="https://opensource-demo.orangehrmlive.com"

class TestMyInfo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def test_edit_blood_type(self):
        driver = self.driver
        driver.get(url)
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
        time.sleep(3)

        driver.find_element(By.ID, "btnEditCustom").click()
        Select(driver.find_element(By.NAME, "custom1")).select_by_value("O+")
        time.sleep(0.5)
        driver.find_element(By.ID, "btnEditCustom").click()
        time.sleep(3)

        self.assertIn(Select(driver.find_element(By.NAME, "custom1")).first_selected_option.text, "O+")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
