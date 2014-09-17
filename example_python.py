from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class ExamplePython(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.wotif.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_example_python(self):
        driver = self.driver
        driver.get(self.base_url + "/?experiments=home&lid=home-responsive&utm_expid=60784533-75.4yKDLqKaRa2gE5zS4pA9MA.1")
        try: self.assertEqual(u"Wotif.com – Hotels, Flights, Holiday Packages & Holiday Rentals", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Australia").click()
        driver.find_element_by_xpath("//ul[@id='regions']/li/label").click()
        driver.find_element_by_id("1").click()
        driver.find_element_by_id("hotel-search__submit").click()
        for i in range(60):
            try:
                if "Wotif.com: Sydney hotels, accommodation, motels, serviced apartments, B&B - Online hotel bookings with instant confirmation - select your hotel at Wotif.com" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Amora Jamison Sydney", driver.find_element_by_css_selector("#property-W1649 > th.hotel-name.review-scores > div.hotel-actions > div.details.cf > span.hotel-name > a.name > h3").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#property-W1649 > th.hotel-name.review-scores > div.hotel-actions > div.details.cf > span.hotel-name > a.name > h3").click()
        for i in range(60):
            try:
                if "Amora Jamison Sydney - Wotif.com" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
