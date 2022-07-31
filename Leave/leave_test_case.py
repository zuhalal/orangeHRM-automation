### Created by Zuhal 'Alimul Hadi
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#variable
username="Admin"
password="admin123"
url="https://opensource-demo.orangehrmlive.com"

class TestLeave(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def test_add_entitlement_with_valid_input(self):
        driver = self.driver
        driver.get(url)
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu_leave_viewLeaveModule").click()
        time.sleep(1)

        driver.find_element(By.ID, "menu_leave_Entitlements").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_leave_addLeaveEntitlement").click()
        time.sleep(3)

        driver.find_element(By.NAME, "entitlements[employee][empName]").send_keys("John Smith")
        driver.find_element(By.NAME, "entitlements[employee][empName]").send_keys(Keys.ENTER)
        time.sleep(1)
        Select(driver.find_element(By.NAME, "entitlements[leave_type]")).select_by_value("3")
        driver.find_element(By.NAME, "entitlements[entitlement]").send_keys(10)
        time.sleep(1)
        driver.find_element(By.ID, "btnSave").submit()
        time.sleep(5)

        self.assertIn(driver.current_url, "https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveEntitlements/savedsearch/1")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
