from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SearchBkkChinatownHotel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.wotif.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search_bkk_chinatown_hotel(self):
        driver = self.driver
        driver.get(self.base_url + "/?lid=places-beta&utm_expid=60784533-11.MYmjPJQdSJa6MHztR5cHXg.1&utm_referrer=http%3A%2F%2Fwww.wotif.com%2Fsearch%2Fresults%3Fdestinations%3D%26searchTerms%3DBangkok%2BChinatown%26previousSearchTerms%3DBangkok%2BChinatown%26descriptionSearch%3Dtrue%26hotel%3D%26country%3D%26region%3D%26destination%3D%26adults%3D2%26children%3D0%26refine%3DSearch%26accommodationTypeMatch%3D%26roomTypeCategoryMatch%3D%26starRatingMatch%3D%26maximumPrice%3D999999999999999999999%26selectedSuggestionId%3D%26startDay%3D2014-06-30%26formSearch%3Dtrue%26page%3D1%26viewType%3Dall")
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Wotif.com"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("freetext-field").clear()
        driver.find_element_by_id("freetext-field").send_keys("Bangkok Chinatown")
        try: self.assertEqual("Bangkok Chinatown", driver.find_element_by_id("freetext-field").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "search-btn"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("search-btn").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.crumbtrail-wrapper.crumb-levels1"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("maximumPrice").clear()
        driver.find_element_by_name("maximumPrice").send_keys("9999999999999999999999999999")
        try: self.assertEqual("9999999999999999999999999999", driver.find_element_by_name("maximumPrice").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Search", driver.find_element_by_id("search-btn").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("search-btn").click()
        try: self.assertEqual("Accommodation Search for Bangkok Chinatown Bangkok", driver.find_element_by_css_selector("div.crumbtrail-wrapper.crumb-levels1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Found 18 results", driver.find_element_by_css_selector("i.results-count.results-count--staticmap").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#map-button > img"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='matrix-results']/div/div/div[3]/table/thead/tr/th/div/div/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.2.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.3.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.4.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.5.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.6.0 | ]]
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#property-M2502 > th.hotel-name.review-scores > div.hotel-actions > div.details.cf > span.hotel-name > a.name > h3"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.9.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.10.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.11.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.12.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.13.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.15.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.16.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.18.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.19.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | //div[@id='matrix-results']/div/div/div[3]/table.20.0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        try: self.assertEqual("Loftel22 Hostel", driver.find_element_by_css_selector("#property-W552241 > th.hotel-name.review-scores > div.hotel-actions > div.details.cf > span.hotel-name > a.name > h3").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "River View Guest House" == driver.find_element_by_css_selector("#property-W66366 > th.hotel-name.review-scores > div.hotel-actions > div.details.cf > span.hotel-name > a.name > h3").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Wotif.com: hotels, accommodation, motels, serviced apartments, B&B - Online hotel bookings with instant confirmation - select your hotel at Wotif.com", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual("Help", driver.find_element_by_xpath("//li[2]/a/strong").text)
    
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
