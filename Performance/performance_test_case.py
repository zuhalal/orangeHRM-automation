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

class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def test_add_kpi_with_invalid_input(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu__Performance").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_performance_Configure").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_performance_searchKpi").click()
        time.sleep(3)

        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(3)

        Select(driver.find_element(By.ID, "defineKpi360_jobTitleCode")).select_by_value("9")
        driver.find_element(By.ID, "defineKpi360_keyPerformanceIndicators").send_keys("Feature Tested")
        driver.find_element(By.ID, "defineKpi360_minRating").send_keys(000)
        time.sleep(1)
        driver.find_element(By.ID, "saveBtn").click()
        time.sleep(3)

        message = driver.find_element(By.CSS_SELECTOR, ".message.error").text

        self.assertIn(message, "An internal error occurred. Please contact your system administrator.")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
