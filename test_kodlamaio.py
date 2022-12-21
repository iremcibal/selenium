from selenium import webdriver
from pathlib import Path
from datetime import date
from selenium.webdriver.common.by import By
from time import sleep  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import *

class Test_kodlamaio:
    #Her test öncesi çalışır
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #klasör oluşturma
        self.today = str(date.today())
        Path(self.today).mkdir(exist_ok=True)
    #Her test sonrası çalışır
    def teardown_method(self):
        self.driver.quit()

    #class fonksiyonlarının ilk parametresi her zaman "self"tir
    #herhangi bir parametre almasa da self almak zorunda 
    def test_login(self):
        #self.driver = webdriver.Chrome()
        self.driver.get(BASE_DOMAIN_URL)
        lobinBtnXpath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,lobinBtnXpath)))
        loginBtn = self.driver.find_element(By.XPATH,lobinBtnXpath)
        self.driver.save_screenshot(self.today +"/test-login.png")

        #text = "merhaba"
        #if-else gibi düşüncez boolean değer döndürmüş olacak
        assert loginBtn.text == LOGIN_TEXT 

    def test_register(self):
        assert True
