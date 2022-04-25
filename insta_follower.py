import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self, user, pw):
        # url = "https://www.instagram.com/login/"
        url = "https://www.instagram.com/rustleup2/"
        self.driver.get(url)

        # Agree to essential cookies
        gdpr_button = self.driver.find_element(By.XPATH, "/ html / body / div[4] / div / div / button[1]")
        gdpr_button.click()

        time.sleep(10)

        # Enter username
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.click()
        username_input.send_keys(user)

        # Enter password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.click()
        password_input.send_keys(pw)

        password_input.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)




    def find_followers(self):
        pass

    def follow(self):
        pass
