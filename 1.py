# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        driver.get("https://www.citrus.ua/")
        driver.find_element_by_xpath("//header[@id='header']/div[3]/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//header[@id='header']/div[3]/div/div/div[2]/div[2]/ul/li/a/span[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_xpath("//img[contains(@src,'https://static.tildacdn.com/tild3839-6162-4331-b862-326435373731/Vector_Smart_Object.svg')]").click()
        driver.find_element_by_xpath("//img[@alt='Realme']").click()
        driver.find_element_by_link_text(u"Наушники").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_2 | ]]
        driver.find_element_by_id("search-input").clear()
        driver.find_element_by_id("search-input").send_keys(u"привет")
        driver.find_element_by_id("search-input").send_keys(Keys.ENTER)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
