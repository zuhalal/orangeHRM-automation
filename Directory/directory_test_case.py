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

class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def test_clear_all_search_query_in_search_dictionary(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu_directory_viewDirectory").click()
        driver.find_element(By.ID, "searchDirectory_emp_name_empName").send_keys("Peter")
        Select(driver.find_element(By.ID, "searchDirectory_job_title")).select_by_value("2")
        Select(driver.find_element(By.ID, "searchDirectory_location")).select_by_value("1,2,5,-1")
        time.sleep(1)

        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(2)

        driver.find_element(By.ID, "resetBtn").click()
        time.sleep(2)

        self.assertIn(driver.find_element(By.ID, "searchDirectory_emp_name_empName").text, "")
        self.assertIn(Select(driver.find_element(By.ID, "searchDirectory_job_title")).first_selected_option.text, "All")
        self.assertIn(Select(driver.find_element(By.ID, "searchDirectory_location")).first_selected_option.text, "All")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
