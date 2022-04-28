import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

TARGET_ACCOUNT = 'chefsteps'
INSTAGRAM_URL = "https://www.instagram.com/"
MY_INSTAGRAM_ACCT = "rustleup2"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 30)

    def login(self, user, pw):
        # url = "https://www.instagram.com/login/"
        url = INSTAGRAM_URL+MY_INSTAGRAM_ACCT
        self.driver.get(url)

        # Agree to essential cookies
        gdpr_button = self.driver.find_element(By.XPATH, "/ html / body / div[4] / div / div / button[1]")
        gdpr_button.click()

        time.sleep(10)

        # Suddenly, the login screen changed and now requires a login button
        # be pressed to enter credentials.
        try:
            # Enter username
            username_input = self.driver.find_element(By.NAME, "username")
        except NoSuchElementException:
            login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div["
                                                              "3]/div/span/a[1]/button/div")
            # login_button = self.driver.find_element(By.LINK_TEXT, "Log in")
            login_button.click()
            time.sleep(5)
            username_input = self.driver.find_element(By.NAME, "username")
            username_input.click()
            username_input.send_keys(user)
        else:
            username_input.click()
            username_input.send_keys(user)

        finally:
            # Enter password
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.click()
            password_input.send_keys(pw)
            password_input.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)

        # Don't save login
        not_now_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
        not_now_button.click()


    def find_followers(self):
        # Load the target account
        url = INSTAGRAM_URL+TARGET_ACCOUNT
        self.driver.get(url)

        # Click the followers link
        followers_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.Y8-fY:nth-child(2) > "
                                                                                      "a:nth-child(1) > "
                                                                                      "div:nth-child(1)")))
        # followers_link = self.driver.find_element(By.CSS_SELECTOR, "li.Y8-fY:nth-child(2) > a:nth-child(1) >
        # div:nth-child(1)")
        followers_link.click()

        # Locate the followers pop-up
        pop_up_followers = self.wait.until(EC.presence_of_element_located((By.XPATH, "/ html / body / div[6] / div / "
                                                                                     "div / div / div[2]")))
        # pop_up_followers = self.driver.find_element(By.XPATH, "/ html / body / div[6] / div / div / div / div[2]")

        # Scroll down the list of followers
        for _ in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].offsetHeight', pop_up_followers)
            time.sleep(2)



    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
