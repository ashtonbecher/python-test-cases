import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class LogIn(unittest.TestCase):

    def setUp(self):
        # Create new Chrome session/instance
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Navigate to Hudl main website
        self.driver.get('https://www.hudl.com')
        try:
            assert self.driver.title == 'Hudl: We Help Teams and Athletes Win'
        except AssertionError:
            print('Incorrect Page Loaded')

    def test_login_button_present(self):
        # Verify the login button is present on the home page
        try:
            assert self.driver.find_element_by_link_text('Log in')
        except NoSuchElementException as e:
            print(e)
            raise

    def test_navigate_to_login_page(self):
        # Click the "Log In" button from the home page
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        self.driver.implicitly_wait(10)
        try:
            assert self.driver.title == 'Log In - Hudl'
        except AssertionError as e:
            print(e)
            raise

    def test_valid_login(self):
        # Click the "Log In" button from the home page
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        try:
            assert self.driver.title == 'Log In - Hudl'
        except AssertionError as e:
            print(e)
            raise

        # Enter a valid username
        self.username_bar = self.driver.find_element_by_name('username')
        self.username_bar.clear()
        self.username_bar.send_keys()

        # Enter a valid password
        self.password_bar = self.driver.find_element_by_name('password')
        self.password_bar.clear()
        self.password_bar.send_keys()

        # Click the "Log In" button
        self.log_in_button = self.driver.find_element_by_id('logIn')
        self.log_in_button.click()

        # Verify the correct page loaded in a timely manner
        try:
            self.page_title = WebDriverWait(self.driver, 10).until(EC.title_is('Home - Hudl'))
        except TimeoutError as e:
            print(e)
            raise

        # Verify the correct page loaded
        try:
            assert self.driver.title == 'Home - Hudl'
        except AssertionError as e:
            print(e)
            raise

    def test_invalid_login(self):
        # Click the "Log In" button from the home page
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        try:
            assert self.driver.title == 'Log In - Hudl'
        except AssertionError as e:
            print(e)
            raise

        # Enter a valid username
        self.username_bar = self.driver.find_element_by_name('username')
        self.username_bar.clear()
        self.username_bar.send_keys()

        # Enter an invalid (no) password
        self.password_bar = self.driver.find_element_by_name('password')
        self.password_bar.clear()

        # Click the "Log In" button
        self.log_in_button = self.driver.find_element_by_id('logIn')
        self.log_in_button.click()

        # Verify the login error popup appears
        try:
            assert self.driver.find_element_by_xpath("//div[contains(@class, 'login-error')]")
        except AssertionError as e:
            print(e)
            raise

    def test_remember_me(self):
        # Click the "Log In" button from the home page
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        try:
            assert self.driver.title == 'Log In - Hudl'
        except AssertionError as e:
            print(e)
            raise

        # Enter a valid username
        self.username_bar = self.driver.find_element_by_name('username')
        self.username_bar.clear()
        self.username_bar.send_keys()

        # Enter a valid password
        self.password_bar = self.driver.find_element_by_name('password')
        self.password_bar.clear()
        self.password_bar.send_keys()

        # Click the "Log In" button
        self.log_in_button = self.driver.find_element_by_id('logIn')
        self.log_in_button.click()

        # Verify the correct page loaded in a timely manner
        try:
            self.page_title = WebDriverWait(self.driver, 10).until(EC.title_is('Home - Hudl'))
        except TimeoutError as e:
            print(e)
            raise

        # Verify the correct page loaded
        try:
            assert self.driver.title == 'Home - Hudl'
        except AssertionError as e:
            print(e)
            raise

        # Log out
        self.driver.find_element_by_xpath("//div[contains(@class, 'hui-globalusermenu')]").click()
        self.driver.find_element_by_xpath("//a[contains(@data-qa-id, 'webnav-usermenu-logout')]").click()

        # Verify home page is loaded
        try:
            assert self.driver.title == 'Hudl: We Help Teams and Athletes Win'
        except AssertionError:
            print('Incorrect Page Loaded')

        # Click the "Log In" button from the home page
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        try:
            assert self.driver.title == 'Log In - Hudl'
        except AssertionError as e:
            print(e)
            raise

        # Verify username is remembered
        self.username_bar = self.driver.find_element_by_name('username')
        try:
            assert self.username_bar.get_attribute('value') == 'ash.becher@gmail.com'
        except AssertionError as e:
            print(e)
            raise

    def tearDown(self):
        # Close browser session
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


