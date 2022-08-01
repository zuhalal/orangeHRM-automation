### Created by Zuhal 'Alimul Hadi
from lib2to3.pgen2.driver import Driver
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

class TestRecruitment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(3)

    def test_download_resume(self):
        driver = self.driver
        driver.get(url)
        time.sleep(3)

        self.login(driver)

        driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_recruitment_viewCandidates").click()
        time.sleep(3)

        Select(driver.find_element(By.ID, "candidateSearch_jobVacancy")).select_by_value("1")
        Select(driver.find_element(By.ID, "candidateSearch_status")).select_by_value("SHORTLISTED")
        time.sleep(1)
        driver.find_element(By.ID, "btnSrch").click()
        time.sleep(3)

        element = driver.find_elements(By.CSS_SELECTOR, ".odd .left a")

        for el in element:
            if el.text == "Download":
                el.click()
                self.assertIn(el.text, "Download")
                break
        
        time.sleep(2)
        is_not_found = driver.find_element(By.CSS_SELECTOR, "td").text
        self.assertTrue(is_not_found)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
