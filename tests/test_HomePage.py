import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class TestHomePage():
    def test_verify_user_is_able_to_book_birthday_gift_from_homepage(self):
        driver=webdriver.Chrome()
        driver.get("https://myfancycrafts.com/")
        driver.maximize_window()
        print(driver.title)
        driver.find_element(By.XPATH,"//h4[text()='Birthday Gifts']").click()
        wait=WebDriverWait(driver,10)
        wait.until(presence_of_element_located((By.XPATH,"//a[text()='Custom Photo Frame With Calendar']"))).click()
        driver.find_element(By.NAME,"add-to-cart").click()
        driver.find_element(By.CLASS_NAME,"icon-shopping-basket").click()
        driver.find_element(By.CLASS_NAME,"icon-shopping-basket").click()

