package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class ExampleJava {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "http://www.wotif.com/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testExampleJava() throws Exception {
    driver.get(baseUrl + "/?experiments=home&lid=home-responsive&utm_expid=60784533-75.4yKDLqKaRa2gE5zS4pA9MA.1");
    try {
      assertEquals("Wotif.com – Hotels, Flights, Holiday Packages & Holiday Rentals", driver.getTitle());
    } catch (Error e) {
      verificationErrors.append(e.toString());
    }
    driver.findElement(By.linkText("Australia")).click();
    driver.findElement(By.xpath("//ul[@id='regions']/li/label")).click();
    driver.findElement(By.id("1")).click();
    driver.findElement(By.id("hotel-search__submit")).click();
    for (int second = 0;; second++) {
    	if (second >= 60) fail("timeout");
    	try { if ("Wotif.com: Sydney hotels, accommodation, motels, serviced apartments, B&B - Online hotel bookings with instant confirmation - select your hotel at Wotif.com".equals(driver.getTitle())) break; } catch (Exception e) {}
    	Thread.sleep(1000);
    }

    try {
      assertEquals("Amora Jamison Sydney", driver.findElement(By.cssSelector("#property-W1649 > th.hotel-name.review-scores > div.hotel-actions > div.details.cf > span.hotel-name > a.name > h3")).getText());
    } catch (Error e) {
      verificationErrors.append(e.toString());
    }
    driver.findElement(By.cssSelector("#property-W1649 > th.hotel-name.review-scores > div.hotel-actions > div.details.cf > span.hotel-name > a.name > h3")).click();
    for (int second = 0;; second++) {
    	if (second >= 60) fail("timeout");
    	try { if ("Amora Jamison Sydney - Wotif.com".equals(driver.getTitle())) break; } catch (Exception e) {}
    	Thread.sleep(1000);
    }

  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
