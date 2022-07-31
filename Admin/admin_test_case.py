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

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)
    
    def test_search_all_user_by_username_and_role(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)

        self.login(driver)
        
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(3)

        driver.find_element(By.ID, "searchSystemUser_userName").send_keys("Cecil.Bdasdsonaparte")
        Select(driver.find_element(By.ID, "searchSystemUser_userType")).select_by_value("2")
        time.sleep(2)
        driver.find_element(By.NAME, "_search").submit()
        time.sleep(5)
        try:
            # if at least a record found
            is_found = driver.find_element(By.CSS_SELECTOR, ".odd") or driver.find_element(By.CSS_SELECTOR, ".even")
            self.assertTrue(is_found)
        except:
            # if no records found
            is_not_found = driver.find_element(By.CSS_SELECTOR, "td").text
            self.assertTrue(is_not_found)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
