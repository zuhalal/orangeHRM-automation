### Created by Zuhal 'Alimul Hadi
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

    def test_quick_launch_my_leave(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu_dashboard_index").click()
        time.sleep(3)

        wait = WebDriverWait(driver, 10)
        elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".quickLaunge a span")))
        time.sleep(3)

        ## idk why stale element reference exception if using element texr
        counter = 0

        for element in elements:
            counter += 1
            if (counter == 5):
                element.click()
                time.sleep(2)

        self.assertIn(driver.current_url, "https://opensource-demo.orangehrmlive.com/index.php/leave/viewMyLeaveList")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
